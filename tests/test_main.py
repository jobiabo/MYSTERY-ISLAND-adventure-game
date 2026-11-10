"""Tests for main.py (the outer play / replay / quit loop).

main.py calls main() at import time, so we run it with runpy while
game_play.start_game is replaced by a fake.
"""
import os
import runpy
import unittest
from unittest.mock import patch

import helpers
from helpers import console
import config

MAIN_PATH = os.path.join(helpers.ROOT, "main.py")


def run_main():
    runpy.run_path(MAIN_PATH, run_name="main_under_test")


def finish_game():
    config.PLAYER_STATE["game_progress"] = "completed"


class MainLoopTests(unittest.TestCase):
    def setUp(self):
        helpers.reset_state()

    def test_completed_game_then_no_quits(self):
        with patch("game_play.start_game", side_effect=finish_game) as sg, \
                console(["no"]) as c:
            run_main()
        sg.assert_called_once()
        self.assertIn("Would you like to play again?", c.output)
        self.assertIn("Goodbye", c.output)

    def test_completed_game_then_yes_replays(self):
        with patch("game_play.start_game", side_effect=finish_game) as sg, \
                console(["yes", "no"]) as c:
            run_main()
        self.assertEqual(sg.call_count, 2)
        self.assertIn("Welcome back", c.output)

    def test_invalid_replay_answer_is_reprompted(self):
        with patch("game_play.start_game", side_effect=finish_game), \
                console(["maybe", "no"]) as c:
            run_main()
        self.assertIn("Invalid response", c.output)
        self.assertIn("Goodbye", c.output)

    def test_unfinished_game_restarts_automatically(self):
        """Game over (not completed) -> main loops and starts a fresh game."""
        calls = {"n": 0}

        def fake_start():
            calls["n"] += 1
            if calls["n"] == 2:
                finish_game()

        with patch("game_play.start_game", side_effect=fake_start), \
                console(["no"]):
            run_main()
        self.assertEqual(calls["n"], 2)

    def test_ctrl_c_then_yes_quits(self):
        with patch("game_play.start_game", side_effect=KeyboardInterrupt), \
                console(["yes"]) as c:
            run_main()
        self.assertIn("Do you want to quit?", c.output)
        self.assertIn("Quiting", c.output)

    def test_ctrl_c_twice_force_quits(self):
        with patch("game_play.start_game", side_effect=KeyboardInterrupt), \
                console([KeyboardInterrupt]):
            with self.assertRaises(SystemExit):
                run_main()


if __name__ == "__main__":
    unittest.main()
