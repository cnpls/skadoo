"""Example use-case for skadoo"""
import skadoo


def add(x: str, y: str, z: str):
    print(float(z) + float(y) + float(z))


def subtract(x: str, y: str, z: str):
    print(float(z) - float(y) - float(z))


def multiply(x: str, y: str, z: str):
    print(float(z) * float(y) * float(z))


# create flag args
x_flag = skadoo.create_flag(name="x", description="x flag arg")
y_flag = skadoo.create_flag(name="y", description="y flag arg")
z_flag = skadoo.create_flag(name="z", description="z flag arg")

# create root arguments
add_arg = skadoo.create_root(
    name="add numbers",
    description="add numbers passed with flags",
    flags=(x_flag, y_flag, z_flag),
)
subtract_arg = skadoo.create_root(
    name="subtract numbers",
    description="subtract numbers passed with flags",
    flags=(x_flag, y_flag, z_flag),
)
multiply_arg = skadoo.create_root(
    name="multiply numbers",
    description="multiply numbers passed with flags",
    flags=(x_flag, y_flag, z_flag),
)


# TODO: create root-less commands
# rootless = skadoo.create_arg(name="rootless", description="arguments without a root", flags=(x_flag, y_flag, z_flag))


def main():

    if add_arg.called:
        add(
            x=add_arg.flags["x"].value,
            y=add_arg.flags["y"].value,
            z=add_arg.flags["z"].value,
        )

        return

    elif subtract_arg.called:
        subtract(
            x=subtract_arg.flags["x"].value,
            y=subtract_arg.flags["y"].value,
            z=subtract_arg.flags["z"].value,
        )

        return

    elif multiply_arg.called:
        multiply(
            x=multiply_arg.flags["x"].value,
            y=multiply_arg.flags["y"].value,
            z=multiply_arg.flags["z"].value,
        )

        return

    print("Commands not recognized")


if __name__ == "__main__":
    main()
