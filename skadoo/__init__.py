import sys

from typing import NamedTuple


__version__ = "0.0.0"


class Arg(NamedTuple):
    name: str
    description: str
    value: str


class Root(Arg):

    def update_value(self, value: str):
        self.value = value


def create_root(name: str, description: str = "", value: str = "") -> Root:
    return Root(name, description, value)


class Flag(Arg):
    short: str
    do: str


def create_flag(
    name: str,
    short: str = "",
    description: str = "",
    do: str = "set_true",
    value: str = "",
) -> Flag:

    # clean "--flag-name", "flag name", "flag_name", "-flag-name"
    name_parts = (
        name.replace("--", " ").strip().replace("-", " ").replace("_", " ").split(" ")
    )
    name = "--" + "-".join(name_parts)

    if short == "":
        short = "-" + "".join([_[:1] for _ in name_parts])

    return Flag(name, short, description, do, value)
