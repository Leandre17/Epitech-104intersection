from argparse import ArgumentParser, ArgumentError


def check_error(av: list[str]) -> int:
    if len(av) != 9:
        print("Not enough or too more arguments")
        return 84
    parser = ArgumentParser(exit_on_error=False)
    parser.add_argument("opt", type=int)
    parser.add_argument("xp", type=int)
    parser.add_argument("yp", type=int)
    parser.add_argument("zp", type=int)
    parser.add_argument("xv", type=int)
    parser.add_argument("yv", type=int)
    parser.add_argument("zv", type=int)
    parser.add_argument("p", type=int)
    try:
        args = parser.parse_args()
    except ArgumentError:
        print("Error: Bad argument retry with -h")
        return 84
    if int(av[8]) < 0:
        print("Error : bad radius or angle (inferior as 0)")
        return 84
    if int(av[8]) > 90 and int(av[1]) == 3:
        print("Error: bad angle (superior as 90)")
        return 84
    if int(av[5]) == 0 and int(av[6]) == 0 and int(av[7]) == 0:
        print("Error: null direction vector")
        return 84
    return 0
