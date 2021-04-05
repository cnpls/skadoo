![tests](https://github.com/cnpls/skadoo/workflows/tests/badge.svg)

This project is under development.

# skadoo

Python library for building command line programs.

## Installation

`pip install skadoo`

## Usage

In your Python script use `skadoo` to create command line arguments.

_my_script.py_
```py
import skadoo


# create flag args
my_flag = skadoo.create_flag(name="my flag", description="my flag argument")

# create root arguments
my_root = skadoo.create_root(
    name="My Root", description="my root argument", flags=(my_flag)
)

if __name__ == "__main__":
    flag = my_root.flags["my flag"].flag
    flag_value = my_root.flags["my flag"].value
    
    print("root used:", my_root.root, f"flag ({flag}) value: {flag_value}")
```

Run `python my_script.py my_root --my-flag="value"`
