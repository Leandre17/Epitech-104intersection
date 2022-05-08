def display_usage() -> int:
    print("USAGE\n\t./104intersection opt xp yp zp xv yv zv p\n\n")
    print(
        "DESCRIPTION\n\topt\t\tsurface option: 1 for a sphere, 2 for a cylinder, 3 for a cone"
    )
    print(
        "\t(xp, yp, zp)\tcoordinates of a point by which the light ray passes through"
    )
    print("\t(xv, yv, zv)\tcoordinates of a vector parallel to the light ray")
    print("\tp\t\tparameter: radius of the sphere, radius of the cylinder, or")
    print("\t\t\tangle formed by the cone and the Z-axis")
    return 0
