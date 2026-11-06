"""Tests for effects.typewriter."""
import unittest
from unittest.mock import patch, call

import helpers  # noqa: F401  (sets up sys.path)
import effects


class TypewriterTests(unittest.TestCase):
    def test_prints_each_character_then_newline(self):
        with patch("effects.time.sleep"), patch("builtins.print") as prt:
            effects.typewriter("abc")
        self.assertEqual(prt.call_args_list, [
            call("a", end="", flush=True),
            call("b", end="", flush=True),
            call("c", end="", flush=True),
            call(),
        ])

    def test_sleeps_once_per_character_with_given_delay(self):
        with patch("effects.time.sleep") as slp, patch("builtins.print"):
            effects.typewriter("hello", delay=0.05)
        self.assertEqual(slp.call_count, 5)
        slp.assert_called_with(0.05)

    def test_default_delay_is_zero(self):
        with patch("effects.time.sleep") as slp, patch("builtins.print"):
            effects.typewriter("hi")
        slp.assert_called_with(0.0)

    def test_empty_string_only_prints_newline(self):
        with patch("effects.time.sleep") as slp, patch("builtins.print") as prt:
            effects.typewriter("")
        slp.assert_not_called()
        self.assertEqual(prt.call_args_list, [call()])


if __name__ == "__main__":
    unittest.main()
