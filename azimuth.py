#!/usr/bin/env python3

"""calculate azimuth with equirectangular approximation"""

from math import pi, sin, cos, atan2, degrees, radians


def main() -> None:
    """main entry point"""

    # points latitude and longitude
    p0_lat = 48.85791635773563
    p0_lon = 2.29451518225098
    p1_lat = 48.85008835764399
    p1_lon = 2.3333844212875388

    p0_lat = radians(p0_lat)
    p0_lon = radians(p0_lon)
    p1_lat = radians(p1_lat)
    p1_lon = radians(p1_lon)

    d_lon = p1_lon - p0_lon
    y = sin(d_lon) * cos(p1_lat)
    x = cos(p0_lat) * sin(p1_lat) - sin(p0_lat) * cos(p1_lat) * cos(d_lon)

    azimuth = degrees(atan2(y, x))  # -180 .. 180
    azimuth = (azimuth + 360) % 360  # 0 .. 360

    print(azimuth)


if __name__ == '__main__':
    main()