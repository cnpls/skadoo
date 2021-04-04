import os
import sys
import logging
import subprocess

import skadoo
from . import test_dir


def test_add():
    python = sys.executable

    x = 1
    y = 1
    z = 1

    result = subprocess.check_output(
        [
            python,
            os.path.join(test_dir, "examples.py"),
            "add_numbers",
            f"-x",
            str(x),
            f"-y={y}",
            "--z",
            str(z),
        ]
    ).decode(sys.stdout.encoding)

    print(result)

    assert str(x + y + z) in str(result)
    assert "Commands not recognized" not in str(result)


def test_subtract():
    python = sys.executable

    x = 1
    y = 1
    z = 1

    result = subprocess.check_output(
        [
            python,
            os.path.join(test_dir, "examples.py"),
            "subtract_numbers",
            f"-x",
            str(x),
            f"-y={y}",
            "--z",
            str(z),
        ]
    ).decode(sys.stdout.encoding)

    print(result)

    assert str(x - y - z) in str(result)
    assert "Commands not recognized" not in str(result)


def test_multiply():
    python = sys.executable

    x = 1
    y = 1
    z = 1

    result = subprocess.check_output(
        [
            python,
            os.path.join(test_dir, "examples.py"),
            "multiply_numbers",
            f"-x",
            str(x),
            f"-y={y}",
            "--z",
            str(z),
        ]
    ).decode(sys.stdout.encoding)

    print(result)

    assert str(x * y * z) in str(result)
    assert "Commands not recognized" not in str(result)
