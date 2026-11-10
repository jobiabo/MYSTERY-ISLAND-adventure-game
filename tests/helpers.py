"""Shared helpers for the Mystery Island test-suite.

* Puts the project root on sys.path so tests can `import config`, `messages`...
* Provides `console()` to fake keyboard input and capture printed output.
* Provides `reset_state()` so tests never leak PLAYER_STATE into each other.
"""
import copy
import os
import sys
from contextlib import contextmanager
from unittest.mock import patch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import config  # noqa: E402

_DEFAULT_STATE = copy.deepcopy(config.PLAYER_STATE)


def reset_state(name="tester"):
    """Restore PLAYER_STATE to its defaults (in place, same dict object)."""
    config.PLAYER_STATE.clear()
    config.PLAYER_STATE.update(copy.deepcopy(_DEFAULT_STATE))
    config.PLAYER_STATE["player_name"] = name


class Console:
    def __init__(self, input_mock, print_mock):
        self.input = input_mock
        self.print = print_mock

    @property
    def output(self):
        """Everything printed, joined into one string."""
        return "\n".join(
            " ".join(str(a) for a in call.args) for call in self.print.call_args_list
        )

    @property
    def prompts(self):
        """Every prompt string passed to input(), in order."""
        return [c.args[0] if c.args else "" for c in self.input.call_args_list]


@contextmanager
def console(inputs=()):
    """Fake the terminal: input() returns `inputs` in order, print() is captured.

    If the code asks for more input than supplied the mock raises StopIteration,
    which makes the test fail loudly instead of hanging.
    """
    with patch("builtins.input", side_effect=list(inputs)) as inp, \
            patch("builtins.print") as prt:
        yield Console(inp, prt)
