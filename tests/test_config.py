"""Tests for config.py: player state, signup and every story-text getter."""
import unittest

import helpers
from helpers import console
import config


class PlayerHealthTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_default_health_is_five(self):
        self.assertEqual(config.get_player_health(), 5)

    def test_reflects_changes_to_state(self):
        config.PLAYER_STATE["health"] = 2
        self.assertEqual(config.get_player_health(), 2)


class PlayerStateDefaultsTests(unittest.TestCase):
    def test_expected_keys_and_types(self):
        helpers.reset_state(name="")
        s = config.PLAYER_STATE
        self.assertEqual(s["player_name"], "")
        self.assertEqual(s["health"], 5)
        self.assertIs(s["has_map"], False)
        self.assertEqual(s["current_location"], "beach")
        self.assertIs(s["has_rope"], False)
        self.assertIs(s["has_lantern"], False)
        self.assertEqual(s["game_progress"], "not completed")


class PlayerSignupTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state(name="")

    def test_valid_name_is_saved_lowercased_and_stripped(self):
        with console(["  Joel  "]):
            self.assertTrue(config.player_signup())
        self.assertEqual(config.PLAYER_STATE["player_name"], "joel")

    def test_empty_name_is_rejected(self):
        with console([""]):
            self.assertFalse(config.player_signup())
        self.assertEqual(config.PLAYER_STATE["player_name"], "")

    def test_whitespace_only_name_is_rejected(self):
        with console(["     "]):
            self.assertFalse(config.player_signup())
        self.assertEqual(config.PLAYER_STATE["player_name"], "")


class StoryTextTests(unittest.TestCase):
    """Every getter returns a non-empty string; personalised ones use the name."""

    NAME = "Zelda"
    PERSONALISED = [
        "get_start_message", "get_game_intro", "get_the_lost_map",
        "get_phase_jungle", "get_hollow_embrace", "get_predator_welcome",
        "get_old_bridge_welcome", "get_bridge_success", "get_light_house_welcome",
        "get_find_key_puzzle", "get_find_key_success", "get_ignite_torch_welcome",
        "get_ignite_torch_success", "get_jammed_door_welcome",
        "get_jammed_door_success", "get_rescue_beacon_welcome",
        "get_rescue_beacon_success",
    ]

    def setUp(self):
        helpers.reset_state(name=self.NAME)

    def test_main_menu_is_a_title_screen(self):
        text = config.get_main_menu()
        self.assertIsInstance(text, str)
        self.assertIn("MYSTERY ISLAND ADVENTURE", text)
        self.assertIn("THE LOST", text)
        self.assertIn("PRESS ENTER", text)

    def test_personalised_getters_return_text_containing_player_name(self):
        for fn_name in self.PERSONALISED:
            with self.subTest(getter=fn_name):
                text = getattr(config, fn_name)()
                self.assertIsInstance(text, str)
                self.assertTrue(text.strip())
                self.assertIn(self.NAME, text)

    def test_text_updates_when_name_changes(self):
        config.PLAYER_STATE["player_name"] = "Link"
        self.assertIn("Link", config.get_start_message())
        self.assertNotIn(self.NAME, config.get_start_message())

    def test_lost_map_lists_the_three_options(self):
        text = config.get_the_lost_map()
        for option in ("Drowned Secrets", "Treacherous Steps", "Sealed Fortune"):
            self.assertIn(option, text)

    def test_jungle_text_offers_left_and_right(self):
        text = config.get_phase_jungle()
        self.assertIn("LEFT", text)
        self.assertIn("RIGHT", text)

    def test_find_key_puzzle_lists_the_three_options(self):
        text = config.get_find_key_puzzle()
        for option in ("The Silent Guardian", "The Brittle Relic",
                       "The Keeper's Fortune"):
            self.assertIn(option, text)

    def test_jammed_door_welcome_shows_scrambled_words(self):
        text = config.get_jammed_door_welcome()
        for scramble in ("HSUP", "LLUP", "TSALB"):
            self.assertIn(scramble, text)

    def test_final_success_text_confirms_rescue(self):
        text = config.get_rescue_beacon_success()
        self.assertIn("RESCUE CONFIRMED", text)
        self.assertIn("THE END", text)


if __name__ == "__main__":
    unittest.main()
