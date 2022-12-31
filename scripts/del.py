#!/usr/bin/env python3

# Copyright (c) 2021 Jason Barrie Morley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import signal
import subprocess
import sys

import pick


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Interactive branch deletion")
    options = parser.parse_args()

    signal.signal(signal.SIGINT, signal_handler)

    branches = subprocess.check_output(["git", "for-each-ref", "--format", "%(refname:short)", "refs/heads/"]).decode('utf-8').split("\n")
    branch, _ = pick.pick(branches, "Select branch to delete:")
    subprocess.check_call(["git", "branch", "-D", branch])


if __name__ == "__main__":
    main()
