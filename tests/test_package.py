import os

import skadoo
from . import test_dir


def test_root():
    venv = os.path.join(os.path.dirname(test_dir), "venv")
    python = os.path.join(venv, "scripts", "python.exe")

    os.chdir(test_dir)
    os.system(f"{python} examples.py test")