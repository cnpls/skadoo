import sys

from typing import NamedTuple, Dict, List

from skadoo import utils


def get_command_parts() -> List[str]:
    """
    Parse command line arguments and return cleaned for "=" flags.

    Returns:
        List[str]
    """
    clean_args = []
    for _ in sys.argv:
        clean_args += _.lower().split("=")

    return clean_args


def get_name_parts(name: str) -> List[str]:
    """
    Get name parts from name of argument for constructing internal arg name or 
    flag identity.

    Args:
        name (str): String of name for arugment (ex: "My Argument").

    Returns:
        List[str]
    """
    return (
        name.lower().replace("--", " ").strip().replace("-", " ").replace("_", " ").split(" ")
    )


def is_called(name: str, abbreviation: str = None) -> bool:
    """
    Checks if string is in sys.argv.

    Args:
        name (str): Full string to check for.
        abbreviation (str): Abbreviation to check for.

    Returns:
        bool
    """
    parts = get_command_parts()

    found = True if name in parts else False

    if abbreviation and not found:
        found = True if abbreviation in parts else False

    return found


class Flag(NamedTuple):
    """
    Flag argument object.

    Attributes:
        name (str): Name of argument.
        flag (str): Long string format of flag (--name)
        description (string): Description of argument.
        called (bool): Boolean of if the argument is called. Defaults to False.
        short (str): Short-hand version of flag name. Defaults to "-[initials]".
        value (str): Value passed with flag argument. Defaults to "False".
        empty (bool): True if no value should be expected. Defaults to True.
    """

    name: str
    flag: str
    description: str
    called: bool
    short: str
    value: str
    empty: bool


def parse_flag(flag: str, short: str, empty: bool = False) -> str:
    """
    Parse flag argumnet for value. Defaults to True if exists but no falue passed.

    Args:
        flag (str): Flag passed via command line.
        short (str): Short version of flag argument.
        empty (bool): True if no value should be expected. Defaults to True.

    Returns:
        str
    """
    index = None
    parts = get_command_parts()

    if flag not in parts and short not in parts:
        return "False"

    if empty:
        return "True"

    if flag in parts:
        index = parts.index(flag)

    if short in parts:
        index = parts.index(short)

    return parts[index + 1]


def create_flag(
    name: str,
    flag: str = "",
    description: str = "",
    short: str = "",
    value: str = "",
    empty: bool = False,
) -> Flag:
    """
    Create Flag argument.

    Args:
        name (str): Name of argument.
        flag (str, optional): Long version of flag string. Defaults to "--[name]".
        description (str, optional): Description of argument. Defaults to "".
        short (str, optional): Short-hand version of flag string. Defaults to "-[initials]".
        value (str, optional): Value passed with flag argument. Defaults to "False".
        empty (str, optional): True if no value should be expected. Defaults to True.

    Returns:
        Flag
    """

    # clean "--flag-name", "flag name", "flag_name", "-flag-name"
    flag_parts = get_name_parts(name)
    flag = "--" + "-".join(flag_parts)

    if short == "":
        short = "-" + "".join([_[:1] for _ in flag_parts])

    called = is_called(name=flag, abbreviation=short)

    if called:
        value = parse_flag(flag, short, empty)

    return Flag(name, flag, description, called, short, value, empty)


class Root(NamedTuple):
    """
    Root argument object.

    Attributes:
        name (string): Name of argument.
        description (string): Description of argument.
        called (bool): Boolean of if the argument is called. Defaults to False.
        flags (dict): Dictionary of Flags for Root with. Defaults to [].
    """

    name: str
    root: str
    description: str
    called: bool
    flags: Dict[str, Flag]


def create_root(name: str, description: str = "", flags: List[Flag] = []) -> Root:
    """
    Create a Root argument.

    Args:
        name (str): Name of argument.
        description (str, optional): Description of argument. Defaults to "".
        flags (list-like): Flag args used by Root arg. Defaults to {}.

    Returns:
        Root
    """
    root = "_".join(get_name_parts(name))

    called = is_called(root)

    return Root(name, root, description, called, flags={_.name: _ for _ in flags})
