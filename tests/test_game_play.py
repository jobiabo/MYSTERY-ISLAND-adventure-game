"""Tests for game_play.py: start_game, game_progress (phase 1) and decide_replay."""
import unittest
from unittest.mock import patch

import helpers
from helpers import console
import config
import game_play


class DecideReplayTests(unittest.TestCase):
    def test_yes(self):
        self.assertEqual(game_play.decide_replay("yes", "Play again?"), ("yes", True))

    def test_no(self):
        self.assertEqual(game_play.decide_replay("no", "Play again?"), ("no", False))

    def test_invalid_then_valid_reprompts(self):
        with console(["maybe", "yes"]) as c:
            result = game_play.decide_replay("what", "Play again?")
        self.assertEqual(result, ("yes", True))
        self.assertIn("Invalid response", c.output)
        # the re-prompt includes the original message
        self.assertTrue(all("Play again?" in p for p in c.prompts))

    def test_keyboard_interrupt_while_reprompting(self):
        with console([KeyboardInterrupt]):
            msg, ok = game_play.decide_replay("nope", "Play again?")
        self.assertFalse(ok)
        self.assertIn("forcefully ended", msg)


class StartGameTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state(name="")

    def test_valid_signup_starts_adventure(self):
        with patch("game_play.player_signup", return_value=True), \
                patch("game_play.game_progress", return_value="ran") as gp, \
                console(["", ]) as c:
            result = game_play.start_game()
        self.assertEqual(result, "ran")
        gp.assert_called_once()
        self.assertIn("MYSTERY ISLAND ADVENTURE", c.output)

    def test_missing_username_reprompts_until_valid(self):
        with patch("game_play.player_signup", side_effect=[False, True]) as su, \
                patch("game_play.game_progress") as gp, \
                console(["", ""]) as c:
            game_play.start_game()
        self.assertEqual(su.call_count, 2)
        self.assertIn("Please provide a username", c.output)
        gp.assert_called_once()


class GameProgressTests(unittest.TestCase):
    """Phase 1: saving the map (energy loop lives in game_play.game_progress)."""

    def setUp(self):
        helpers.reset_state()
        # typewriter animation is irrelevant here
        p = patch("game_play.typewriter")
        self.typewriter = p.start()
        self.addCleanup(p.stop)

    def test_success_on_first_try_goes_to_jungle(self):
        with patch("game_play.find_map", return_value=(5, True)), \
                patch("game_play.jungle_welcome") as jungle, \
                console(["", ""]) as c:
            game_play.game_progress()
        jungle.assert_called_once()
        self.assertIn("ENERGY REMAINING: 5/5", c.output)
        self.assertEqual(config.PLAYER_STATE["health"], 5)

    def test_story_is_shown_before_the_challenge(self):
        with patch("game_play.find_map", return_value=(5, True)), \
                patch("game_play.jungle_welcome"), console(["", ""]):
            game_play.game_progress()
        self.assertEqual(self.typewriter.call_count, 2)  # start message + intro

    def test_fail_then_retry_then_success(self):
        with patch("game_play.find_map", side_effect=[(4, False), (4, True)]) as fm, \
                patch("game_play.jungle_welcome") as jungle, \
                console(["", "", "yes"]) as c:
            game_play.game_progress()
        self.assertEqual(fm.call_args_list[0].args, (5,))
        self.assertEqual(fm.call_args_list[1].args, (4,))   # energy carries over
        jungle.assert_called_once()
        self.assertIn("You gather your strength", c.output)
        self.assertEqual(config.PLAYER_STATE["health"], 4)

    def test_out_of_energy_is_game_over(self):
        with patch("game_play.find_map", return_value=(0, False)), \
                patch("game_play.jungle_welcome") as jungle, \
                console(["", ""]) as c:
            game_play.game_progress()
        jungle.assert_not_called()
        self.assertIn("RUN OUT OF ENERGY", c.output)
        self.assertIn("GAME OVER", c.output)

    def test_declining_retry_exits(self):
        with patch("game_play.find_map", return_value=(4, False)), \
                patch("game_play.jungle_welcome") as jungle, \
                console(["", "", "no"]) as c:
            with self.assertRaises(SystemExit):
                game_play.game_progress()
        jungle.assert_not_called()
        self.assertIn("You have chosen to give up", c.output)

    def test_invalid_retry_answer_ends_the_round(self):
        with patch("game_play.find_map", return_value=(4, False)) as fm, \
                patch("game_play.jungle_welcome") as jungle, \
                console(["", "", "perhaps"]) as c:
            game_play.game_progress()
        self.assertEqual(fm.call_count, 1)
        jungle.assert_not_called()
        self.assertIn("Invalid response", c.output)


if __name__ == "__main__":
    unittest.main()
