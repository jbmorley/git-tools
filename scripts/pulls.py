#!/usr/bin/env python3

import argparse
import webbrowser

import common


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("remote", default="origin")
    options = parser.parse_args()
    if (remote := common.get_remote(options.remote)) is None:
        exit("Unable to parse remote.")
    webbrowser.open(f"{remote.url}/pulls")


if __name__ == "__main__":
   main()
