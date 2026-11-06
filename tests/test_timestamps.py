"""Tests for timestamps.timed_input (the optional timed prompt)."""
import time
import unittest
from unittest.mock import patch

import helpers  # noqa: F401
import timestamps


class TimedInputTests(unittest.TestCase):
    def test_returns_stripped_lowercase_answer(self):
        with patch("builtins.input", return_value="  PuSh  "):
            self.assertEqual(timestamps.timed_input("Action: ", timeout=1), "push")

    def test_passes_prompt_through(self):
        with patch("builtins.input", return_value="x") as inp:
            timestamps.timed_input("Your move: ", timeout=1)
        inp.assert_called_once_with("Your move: ")

    def test_returns_none_when_time_runs_out(self):
        def slow_input(prompt):
            time.sleep(0.3)
            return "late"

        with patch("builtins.input", side_effect=slow_input):
            start = time.monotonic()
            result = timestamps.timed_input("Action: ", timeout=0.05)
            elapsed = time.monotonic() - start
        self.assertIsNone(result)
        self.assertLess(elapsed, 0.25)  # returned at the timeout, not after


if __name__ == "__main__":
    unittest.main()
