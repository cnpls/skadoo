import sys

from typing import NamedTuple, Dict, List

from skadoo import utils


def is_called(string: str) -> bool:
    """Checks if string is in sys.argv.

    Args:
        string (str): String to check for.

    Returns:
        bool
    """
    return True if string in sys.argv else False


class Flag(NamedTuple):
    """Flag argument object.

    Attributes:
        name (str): Name of argument.
        flag (str): Long string format of flag (--name)
        description (string): Description of argument.
        called (bool): Boolean of if the argument is called. Defaults to False.
        short (str): Short-hand version of flag name. Defaults to "-[initials]".
        value (str): Value passed with flag argument. Defaults to "False".
    """

    name: str
    flag: str
    description: str
    called: bool
    short: str
    value: str


def create_flag(
    name: str, flag: str = "", description: str = "", short: str = "", value: str = ""
) -> Flag:
    """Create Flag argument.

    Args:
        name (str): Name of argument.
        flag (str, optional): Long version of flag string. Defaults to "--[name]".
        description (str, optional): Description of argument. Defaults to "".
        short (str, optional): Short-hand version of flag string. Defaults to "-[initials]".
        value (str, optional): Value passed with flag argument. Defaults to "False".

    Returns:
        Flag
    """

    # clean "--flag-name", "flag name", "flag_name", "-flag-name"
    flag_parts = (
        flag.replace("--", " ").strip().replace("-", " ").replace("_", " ").split(" ")
    )
    flag = "--" + "-".join(flag_parts)

    called = is_called(name)

    if short == "":
        short = "-" + "".join([_[:1] for _ in flag_parts])

    return Flag(name, flag, description, called, short, value)


class Root(NamedTuple):
    """Root argument object.

    Attributes:
        name (string): Name of argument.
        description (string): Description of argument.
        called (bool): Boolean of if the argument is called. Defaults to False.
        flags (dict): Dictionary of Flags for Root with. Defaults to [].
    """

    name: str
    description: str
    called: bool
    flags: Dict[str, Flag]


def create_root(name: str, description: str = "", flags: List[Flag] = []) -> Root:
    """Create a Root argument.

    Args:
        name (str): Name of argument.
        description (str, optional): Description of argument. Defaults to "".
        flags (list-like): Flag args used by Root arg. Defaults to {}.

    Returns:
        Root
    """
    called = is_called(name)

    return Root(name, description, called, flags={_.name: _.value for _ in flags})
