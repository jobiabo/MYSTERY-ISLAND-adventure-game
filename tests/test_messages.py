"""Tests for messages.py: every challenge function and every phase wrapper."""
import unittest
from unittest.mock import patch, call

import helpers
from helpers import console
import config
import messages


def _letters(s):
    return sorted(s.strip().rstrip(":").strip().upper())


# --------------------------------------------------------------------------
# Small wrappers
# --------------------------------------------------------------------------
class SmallWrapperTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_main_menu_types_out_the_menu(self):
        with patch("messages.typewriter") as tw:
            messages.main_menu()
        tw.assert_called_once_with(config.get_main_menu())

    def test_start_game_types_out_the_welcome(self):
        with patch("messages.typewriter") as tw:
            messages.start_game()
        tw.assert_called_once_with(config.get_start_message())

    def test_hollow_embrace_returns_the_fatal_text(self):
        text = messages.hollow_embrace()
        self.assertIn("FATAL MISTAKE", text)
        self.assertEqual(text, config.get_hollow_embrace())


# --------------------------------------------------------------------------
# Phase 1: find_map
# --------------------------------------------------------------------------
class FindMapTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_losing_options_cost_one_energy(self):
        for answer in ("1", "drowned secrets", "2", "treacherous steps",
                       "  DROWNED SECRETS  "):
            with self.subTest(answer=answer), console([answer]) as c:
                self.assertEqual(messages.find_map(5), (4, False))
                self.assertIn("lost 1 energy", c.output)

    def test_winning_option(self):
        for answer in ("3", "sealed fortune", "Sealed Fortune"):
            with self.subTest(answer=answer), console([answer]) as c:
                self.assertEqual(messages.find_map(5), (5, True))
                self.assertIn("secured the map", c.output)

    def test_invalid_input_costs_energy(self):
        with console(["banana"]) as c:
            self.assertEqual(messages.find_map(3), (2, False))
        self.assertIn("Invalid option", c.output)

    def test_shows_the_scenario(self):
        with console(["3"]) as c:
            messages.find_map(5)
        self.assertIn("THE FADING MAP", c.output)


# --------------------------------------------------------------------------
# Phase 2: jungle path
# --------------------------------------------------------------------------
class JunglePathSelectionTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_left_path_loses_energy(self):
        for answer in ("1", "left", "LEFT", "hollow embrace"):
            with self.subTest(answer=answer), console([answer]) as c:
                self.assertEqual(messages.jungle_path_selection(5), (4, False))
                self.assertIn("FATAL MISTAKE", c.output)

    def test_right_path_succeeds(self):
        for answer in ("2", "right", "Right"):
            with self.subTest(answer=answer), console([answer]):
                self.assertEqual(messages.jungle_path_selection(5), (5, True))

    def test_invalid_input_reprompts_without_penalty(self):
        with console(["up", "", "right"]) as c:
            self.assertEqual(messages.jungle_path_selection(5), (5, True))
        self.assertEqual(c.input.call_count, 3)
        self.assertIn("Enter valid response", c.output)


# --------------------------------------------------------------------------
# Phase 2b: beast fight
# --------------------------------------------------------------------------
class PredatorEngageTests(unittest.TestCase):
    ALL_CORRECT = ["dodge", "move", "attack", "strike", "slash", ""]

    def setUp(self):
        helpers.reset_state()

    def test_perfect_run_wins_the_rope(self):
        with console(self.ALL_CORRECT) as c:
            self.assertEqual(messages.predator_engage(5), (5, True))
        self.assertIn("CONQUERED THE BEAST", c.output)
        self.assertIn("PICKED UP A ROPE", c.output)

    def test_answers_are_case_and_space_insensitive(self):
        answers = ["  DoDgE ", "MOVE", "Attack", " strike", "SLASH ", ""]
        with console(answers):
            self.assertEqual(messages.predator_engage(5), (5, True))

    def test_wrong_dodge_costs_energy_and_skips_attack_round(self):
        with console(["jump", "move"]) as c:
            self.assertEqual(messages.predator_engage(5), (4, False))
        self.assertEqual(c.input.call_count, 2)
        self.assertIn("You are hit", c.output)

    def test_dodge_words_in_wrong_order_fail(self):
        with console(["move", "dodge"]):
            self.assertEqual(messages.predator_engage(5), (4, False))

    def test_wrong_attack_costs_energy(self):
        with console(["dodge", "move", "attack", "strike", "slice"]) as c:
            self.assertEqual(messages.predator_engage(5), (4, False))
        self.assertIn("devoured", c.output)

    def test_attack_words_in_wrong_order_fail(self):
        with console(["dodge", "move", "strike", "attack", "slash"]):
            self.assertEqual(messages.predator_engage(5), (4, False))

    def test_scrambles_are_real_anagrams_of_the_answers(self):
        with console(self.ALL_CORRECT) as c:
            messages.predator_engage(5)
        scrambles = [p for p in c.prompts if "PRESS ENTER" not in p]
        answers = ["dodge", "move", "attack", "strike", "slash"]
        self.assertEqual(len(scrambles), 5)
        for scr, ans in zip(scrambles, answers):
            with self.subTest(scramble=scr):
                self.assertEqual(_letters(scr), _letters(ans))


# --------------------------------------------------------------------------
# Phase 3: bridge puzzle
# --------------------------------------------------------------------------
class OldBridgePuzzleTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_correct_answers(self):
        with console(["rope", "pull", "place"]) as c:
            self.assertEqual(messages.old_bridge_puzzle(5), (5, True))
        self.assertIn("SUCCESSFUL CROSSING", c.output)

    def test_case_insensitive(self):
        with console(["ROPE", " Pull ", "PlAcE"]):
            self.assertEqual(messages.old_bridge_puzzle(5), (5, True))

    def test_one_wrong_word_fails_whole_puzzle(self):
        with console(["rope", "pull", "plane"]) as c:
            self.assertEqual(messages.old_bridge_puzzle(5), (4, False))
        self.assertIn("Bridge was not placed", c.output)

    def test_wrong_order_fails(self):
        with console(["pull", "rope", "place"]):
            self.assertEqual(messages.old_bridge_puzzle(5), (4, False))

    def test_scrambles_are_real_anagrams(self):
        with console(["rope", "pull", "place"]) as c:
            messages.old_bridge_puzzle(5)
        for scr, ans in zip(c.prompts, ["rope", "pull", "place"]):
            with self.subTest(scramble=scr):
                self.assertEqual(_letters(scr), _letters(ans))


# --------------------------------------------------------------------------
# Phase 4: find the key
# --------------------------------------------------------------------------
class FindKeyTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_losing_options(self):
        for answer in ("1", "the silent guardian", "2", "THE BRITTLE RELIC"):
            with self.subTest(answer=answer), console([answer]):
                self.assertEqual(messages.find_key(5), (4, False))

    def test_winning_option(self):
        for answer in ("3", "the keeper's fortune", "The Keeper's Fortune"):
            with self.subTest(answer=answer), console([answer]) as c:
                self.assertEqual(messages.find_key(5), (5, True))
                self.assertIn("KEY SECURED", c.output)

    def test_invalid_input_costs_energy(self):
        with console(["4"]) as c:
            self.assertEqual(messages.find_key(5), (4, False))
        self.assertIn("invalid input", c.output)


# --------------------------------------------------------------------------
# Phase 5: torch puzzle
# --------------------------------------------------------------------------
class IgniteTorchPuzzleTests(unittest.TestCase):
    ANSWERS = ["stick", "gas", "flame", "torch", "light"]

    def setUp(self):
        helpers.reset_state()

    def test_correct_answers(self):
        with console([""] + self.ANSWERS) as c:
            self.assertEqual(messages.ignite_touch_puzzle(5), (5, True))
        self.assertIn("SUCCESSFULLY IGNITED", c.output)

    def test_any_wrong_word_fails(self):
        for i in range(5):
            wrong = list(self.ANSWERS)
            wrong[i] = "nope"
            with self.subTest(wrong_index=i), console([""] + wrong) as c:
                self.assertEqual(messages.ignite_touch_puzzle(5), (4, False))
                self.assertIn("Puzzle failed", c.output)

    def test_wrong_order_fails(self):
        with console([""] + list(reversed(self.ANSWERS))):
            self.assertEqual(messages.ignite_touch_puzzle(3), (2, False))

    def test_scrambles_are_real_anagrams(self):
        with console([""] + self.ANSWERS) as c:
            messages.ignite_touch_puzzle(5)
        scrambles = [p for p in c.prompts if "PRESS ENTER" not in p]
        for scr, ans in zip(scrambles, self.ANSWERS):
            with self.subTest(scramble=scr):
                self.assertEqual(_letters(scr), _letters(ans))


# --------------------------------------------------------------------------
# Phase 6: jammed door
# --------------------------------------------------------------------------
class JamDoorActionTests(unittest.TestCase):
    ANSWERS = ["push", "pull", "blast"]

    def setUp(self):
        helpers.reset_state()

    def test_correct_answers(self):
        with console([""] + self.ANSWERS) as c:
            self.assertEqual(messages.jam_door_action(5), (5, True))
        self.assertIn("ACCESS GRANTED", c.output)

    def test_wrong_word_fails(self):
        with console(["", "push", "pull", "explode"]) as c:
            self.assertEqual(messages.jam_door_action(5), (4, False))
        self.assertIn("Puzzle failed", c.output)

    def test_wrong_order_fails(self):
        with console(["", "pull", "push", "blast"]):
            self.assertEqual(messages.jam_door_action(5), (4, False))

    def test_scrambles_are_real_anagrams(self):
        with console([""] + self.ANSWERS) as c:
            messages.jam_door_action(5)
        scrambles = [p for p in c.prompts if "PRESS ENTER" not in p]
        for scr, ans in zip(scrambles, self.ANSWERS):
            with self.subTest(scramble=scr):
                self.assertEqual(_letters(scr), _letters(ans))


# --------------------------------------------------------------------------
# Phase 7: final beacon
# --------------------------------------------------------------------------
class ActivateRescueBeaconTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_marks_game_completed_and_shows_ending(self):
        self.assertEqual(config.PLAYER_STATE["game_progress"], "not completed")
        with console([""]) as c:
            messages.activate_rescue_beacon()
        self.assertEqual(config.PLAYER_STATE["game_progress"], "completed")
        self.assertIn("RESCUE SUCCESSFUL", c.output)
        self.assertIn("THE END", c.output)


# --------------------------------------------------------------------------
# Phase wrappers: welcome + energy/retry loop (shared behaviour)
# --------------------------------------------------------------------------
#            wrapper                  inner challenge           next phase
WRAPPERS = [
    ("jungle_welcome",          "jungle_path_selection",  "predator_trial_welcome"),
    ("predator_trial_welcome",  "predator_engage",        "old_bridge_welcome"),
    ("old_bridge_welcome",      "old_bridge_puzzle",      "lighthouse_welcome"),
    ("lighthouse_welcome",      "find_key",               "ignite_torch_welcome"),
    ("ignite_torch_welcome",    "ignite_touch_puzzle",    "jam_door_welcome"),
    ("jam_door_welcome",        "jam_door_action",        "activate_rescue_beacon"),
]
INTRO = ["", ""]  # "boost your energy" + "continue" prompts


class PhaseWrapperTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def _run(self, wrapper, inner, nxt, inner_results, inputs):
        """Run one wrapper with the challenge and next phase mocked out."""
        fn = getattr(messages, wrapper)
        with patch.object(messages, inner, side_effect=inner_results) as inner_m, \
                patch.object(messages, nxt) as next_m, \
                console(inputs) as c:
            try:
                fn()
                exc = None
            except SystemExit as e:
                exc = e
        return inner_m, next_m, c, exc

    def test_success_on_first_try_moves_to_next_phase(self):
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                inner_m, next_m, c, _ = self._run(
                    wrapper, inner, nxt, [(5, True)], INTRO)
                inner_m.assert_called_once_with(5)
                next_m.assert_called_once()
                self.assertIn("ENERGY LEVEL BOOSTED", c.output)
                self.assertIn("ENERGY REMAINING: 5/5", c.output)

    def test_energy_is_refilled_to_five_at_phase_start(self):
        config.PLAYER_STATE["health"] = 1
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                inner_m, _, _, _ = self._run(
                    wrapper, inner, nxt, [(5, True)], INTRO)
                self.assertEqual(inner_m.call_args_list[0], call(5))

    def test_failure_then_yes_retries_with_remaining_energy(self):
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                inner_m, next_m, c, _ = self._run(
                    wrapper, inner, nxt, [(4, False), (4, True)], INTRO + ["yes"])
                self.assertEqual(inner_m.call_args_list, [call(5), call(4)])
                next_m.assert_called_once()
                self.assertIn("ENERGY REMAINING: 4/5", c.output)
                self.assertIn("You gather your strength", c.output)

    def test_running_out_of_energy_is_game_over(self):
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                _, next_m, c, exc = self._run(
                    wrapper, inner, nxt, [(0, False)], INTRO)
                next_m.assert_not_called()
                self.assertIsNone(exc)
                self.assertIn("RUN OUT OF ENERGY", c.output)
                self.assertIn("GAME OVER", c.output)

    def test_declining_retry_exits_the_game(self):
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                _, next_m, c, exc = self._run(
                    wrapper, inner, nxt, [(4, False)], INTRO + ["no"])
                self.assertIsInstance(exc, SystemExit)
                next_m.assert_not_called()
                self.assertIn("You have chosen to give up", c.output)

    def test_invalid_retry_answer_reprompts_the_challenge(self):
        """Current behaviour: a bad yes/no answer just loops back into the challenge."""
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                inner_m, next_m, c, _ = self._run(
                    wrapper, inner, nxt, [(4, False), (4, True)], INTRO + ["maybe"])
                self.assertIn("Invalid response", c.output)
                self.assertEqual(inner_m.call_count, 2)
                next_m.assert_called_once()

    def test_each_phase_shows_its_welcome_story(self):
        story = {
            "jungle_welcome": "PHASE II",
            "predator_trial_welcome": "PREDATOR'S TRIAL",
            "old_bridge_welcome": "PHASE III",
            "lighthouse_welcome": "PHASE IV",
            "ignite_torch_welcome": "PHASE V",
            "jam_door_welcome": "JAMMED DOOR",
        }
        for wrapper, inner, nxt in WRAPPERS:
            with self.subTest(phase=wrapper):
                _, _, c, _ = self._run(wrapper, inner, nxt, [(5, True)], INTRO)
                self.assertIn(story[wrapper], c.output)


if __name__ == "__main__":
    unittest.main()
