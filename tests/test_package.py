import os
import sys
import logging
import subprocess

import skadoo
from . import test_dir
from .examples import expected_result


def test_root():
    python = sys.executable

    result = subprocess.check_output([python, os.path.join(test_dir, "examples.py"), "a"])

    assert str(expected_result) in str(result)
    assert "Commands not recognized" not in str(result)