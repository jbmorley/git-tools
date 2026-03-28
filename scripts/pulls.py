#!/usr/bin/env python3

import webbrowser

import common


def main():
    if (remote := common.get_remote()) is None:
        exit("Unable to parse remote.")
    webbrowser.open(f"{remote.url}/pulls")


if __name__ == "__main__":
   main()
