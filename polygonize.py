#!/usr/bin/python3

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Polygonize a raster file.')
    parser.add_argument(
        '-i', '--input',
        action='append',
        nargs='+',
        required=True,
        help='input file name(s)')
    parser.add_argument(
        '-o', '--output',
        action='append',
        nargs='+',
        required=True,
        help='output file name(s)')
    args = parser.parse_args()
    print(args.input)
