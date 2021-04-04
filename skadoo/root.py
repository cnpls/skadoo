import sys

from typing import NamedTuple, Dict, List

from skadoo.flag import Flag
from skadoo import utils


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

    def __str__(self) -> str:
        """
        Create string of Root contents.

        Returns:
            str
        """
        return "\n ".join(
            [
                f"Root ({self.root})",
                f"Name: {self.name}",
                f"Description: {self.description}",
            ]
            + [f"{self.flags[_].__str__()}" for _ in self.flags]
        )

    def describe(self):
        """Print Root content descriptions"""
        print("~~~~~ Help ~~~~~~\n" + self.__str__())


def create_root(
    name: str, root: str = "", description: str = "", flags: List[Flag] = []
) -> Root:
    """
    Create a Root argument.

    Args:
        name (str): Name of argument.
        root (str): Command line identifier of root argument.
        description (str, optional): Description of argument. Defaults to "".
        flags (list-like): Flag args used by Root arg. Defaults to {}.

    Returns:
        Root
    """

    if root == "":
        root = "_".join(utils.get_name_parts(name))

    called = utils.is_called(root)

    result = Root(name, root, description, called, flags={_.name: _ for _ in flags})

    if called and utils.want_help():
        result.describe()
        sys.exit()

    return result
