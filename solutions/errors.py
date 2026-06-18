"""Reusable notebook error-handling helpers.

These helpers keep notebook exercise cells short while preserving robust
logging and user-friendly error messages.
"""

from __future__ import annotations

import logging
from typing import Callable, Mapping, TypeVar

T = TypeVar("T")
LOGGER_NAME = "tennis_notebooks"


def get_notebook_logger(
    logger_name: str = LOGGER_NAME,
    level: int = logging.INFO,
    fmt: str = "%(levelname)s:%(name)s:%(message)s",
) -> logging.Logger:
    """Configure and return the shared notebook logger."""
    logging.basicConfig(level=level, format=fmt)
    return logging.getLogger(logger_name)


def check_multiple_choice(
    *,
    answer: str,
    options: Mapping[str, str],
    is_correct: Callable[[str, Mapping[str, str]], bool],
    exercise_label: str,
    incorrect_message: str,
    invalid_choice_message: str = "Please choose one of: A, B, C, or D.",
    success_message: str = "Correct.",
    logger: logging.Logger | None = None,
) -> None:
    """Validate a multiple-choice answer with standardized logging/errors."""
    notebook_logger = logger or get_notebook_logger()

    try:
        if answer not in options:
            raise ValueError(invalid_choice_message)
        if not is_correct(answer, options):
            raise ValueError(incorrect_message)
    except Exception as exc:
        notebook_logger.warning("%s validation failed: %s", exercise_label, exc)
        raise

    notebook_logger.info("%s validated successfully.", exercise_label)
    print(success_message)


def run_guarded(
    *,
    step_label: str,
    action: Callable[[], T],
    user_error_message: str,
    logger: logging.Logger | None = None,
) -> T:
    """Run an action with standardized exception logging and user messaging."""
    notebook_logger = logger or get_notebook_logger()

    try:
        result = action()
    except Exception:
        notebook_logger.exception("%s failed.", step_label)
        print(user_error_message)
        raise

    notebook_logger.info("%s completed successfully.", step_label)
    return result
