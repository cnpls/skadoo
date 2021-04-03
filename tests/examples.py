"""Example use-case for skadoo"""
import skadoo


def a_function(x: str, y: str, z: str):
    print("a", f"x={x}", f"y={y}", f"z={z}")


def b_function(x: str, y: str, z: str):
    print("b", f"x={x}", f"y={y}", f"z={z}")


def c_function(x: str, y: str, z: str):
    print("c", f"x={x}", f"y={y}", f"z={z}")


# create flag args
x_flag = skadoo.create_flag(name="x", description="x flag arg")
y_flag = skadoo.create_flag(name="y", description="y flag arg")
z_flag = skadoo.create_flag(name="z", description="z flag arg")

# create root arguments
a = skadoo.create_root(
    name="a", description="a root arg", flags=(x_flag, y_flag, z_flag)
)
b = skadoo.create_root(
    name="b", description="b root arg", flags=(x_flag, y_flag, z_flag)
)
c = skadoo.create_root(
    name="c", description="c root arg", flags=(x_flag, y_flag, z_flag)
)


# create root-less commands
# rootless = skadoo.create_arg(name="rootless", description="arguments without a root", flags=(x_flag, y_flag, z_flag))


def main():

    if a.called:
        a_function(x=a.flags["x"], y=a.flags["y"], z=a.flags["z"])

        return

    elif b.called:
        b_function(x=b.flags["x"], y=b.flags["y"], z=b.flags["z"])

        return

    elif c.called:
        c_function(x=c.flags["x"], y=c.flags["y"], z=c.flags["z"])

        return

    print("Commands not recognized")


if __name__ == "__main__":
    main()
