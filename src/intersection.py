from math import sqrt, tan, pi


def my_round(nb: float) -> str:
    nb_str = str(round(float(nb), 3))
    if nb_str[-2] == ".":
        nb_str += "0"
    if nb_str[-3] == ".":
        nb_str += "0"
    return nb_str


def intersection_sphere(av: list[str]) -> int:
    r: float = int(av[8]) ** 2
    a: float = int(av[5]) ** 2 + int(av[6]) ** 2 + int(av[7]) ** 2
    if a == 0:
        print("There is an infinite number of intersection points.")
        return 0
    b: float = (
        (2 * int(av[5]) * int(av[2]))
        + (2 * int(av[6]) * int(av[3]))
        + (2 * int(av[7]) * int(av[4]))
    )
    c: float = int(av[2]) ** 2 + int(av[3]) ** 2 + int(av[4]) ** 2 - r
    delta: float = b ** 2 - 4 * a * c
    if delta < 0:
        print("No intersection point.")
    elif delta == 0:
        print("1 intersection point:")
        x0: float = -(b / (2 * a))
        print(
            f"({my_round((int(av[5]) * x0) + int(av[2]))}, {my_round((int(av[6]) * x0) + int(av[3]))}, {my_round((int(av[7]) * x0) + int(av[4]))})"
        )
    else:
        print("2 intersection points:")
        x1: float = -(b - sqrt(delta)) / (2 * a)
        x2: float = -(b + sqrt(delta)) / (2 * a)
        print(
            f"({my_round((int(av[5]) * x1) + int(av[2]))}, {my_round((int(av[6]) * x1) + int(av[3]))}, {my_round((int(av[7]) * x1) + int(av[4]))})"
        )
        print(
            f"({my_round((int(av[5]) * x2) + int(av[2]))}, {my_round((int(av[6]) * x2) + int(av[3]))}, {my_round((int(av[7]) * x2) + int(av[4]))})"
        )
    return 0


def intersection_cylinder(av: list[str]) -> int:
    r: float = int(av[8]) ** 2
    a: float = int(av[5]) ** 2 + int(av[6]) ** 2
    if a == 0:
        print("There is an infinite number of intersection points.")
        return 0
    b: float = (2 * int(av[5]) * int(av[2])) + (2 * int(av[6]) * int(av[3]))
    c: float = int(av[2]) ** 2 + int(av[3]) ** 2 - r
    delta: float = b ** 2 - 4 * a * c
    if delta < 0:
        print("No intersection point.")
    elif delta == 0:
        print("1 intersection point:")
        x0: float = -(b / (2 * a))
        print(
            f"({my_round((int(av[5]) * x0) + int(av[2]))}, {my_round((int(av[6]) * x0) + int(av[3]))}, {my_round((int(av[7]) * x0) + int(av[4]))})"
        )
    else:
        print("2 intersection points:")
        x1: float = -(b - sqrt(delta)) / (2 * a)
        x2: float = -(b + sqrt(delta)) / (2 * a)
        print(
            f"({my_round((int(av[5]) * x1) + int(av[2]))}, {my_round((int(av[6]) * x1) + int(av[3]))}, {my_round((int(av[7]) * x1) + int(av[4]))})"
        )
        print(
            f"({my_round((int(av[5]) * x2) + int(av[2]))}, {my_round((int(av[6]) * x2) + int(av[3]))}, {my_round((int(av[7]) * x2) + int(av[4]))})"
        )
    return 0


def intersection_cone(av: list[str]) -> int:
    angle: float = tan((pi / 2) - (int(av[8]) * pi / 180)) ** 2
    a: float = angle * (int(av[5]) ** 2 + int(av[6]) ** 2) - int(av[7]) ** 2
    if a == 0:
        print("There is an infinite number of intersection points.")
        return 0
    b: float = angle * (2 * int(av[2]) * int(av[5]) + 2 * int(av[3]) * int(av[6])) - (
        2 * int(av[4]) * int(av[7])
    )
    c: float = angle * (int(av[2]) ** 2 + int(av[3]) ** 2) - int(av[4]) ** 2
    delta: float = b ** 2 - 4 * a * c
    if delta < 0:
        print("No intersection point.")
    elif delta == 0:
        print("1 intersection point:")
        x0: float = -(b / (2 * a))
        print(
            f"({my_round((int(av[5]) * x0) + int(av[2]))}, {my_round((int(av[6]) * x0) + int(av[3]))}, {my_round((int(av[7]) * x0) + int(av[4]))})"
        )
    else:
        print("2 intersection points:")
        x1: float = -(b - sqrt(delta)) / (2 * a)
        x2: float = -(b + sqrt(delta)) / (2 * a)
        print(
            f"({my_round((int(av[5]) * x1) + int(av[2]))}, {my_round((int(av[6]) * x1) + int(av[3]))}, {my_round((int(av[7]) * x1) + int(av[4]))})"
        )
        print(
            f"({my_round((int(av[5]) * x2) + int(av[2]))}, {my_round((int(av[6]) * x2) + int(av[3]))}, {my_round((int(av[7]) * x2) + int(av[4]))})"
        )
    return 0
