#!/usr/bin/env python3

import re
import subprocess
import urllib.parse
import webbrowser


GITHUB_SSH_REGEX = re.compile(r'git@(?P<domain>.+):(?P<owner>.+)/(?P<repo>.+).git')
SSH_PROTOCOL_REGEX = re.compile(r'ssh://git@(?P<domain>.+)/(?P<owner>.+)/(?P<repo>.+).git')


def main():
    url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"]).decode("utf-8").strip()
    if ((match := GITHUB_SSH_REGEX.match(url)) is None) and ((match := SSH_PROTOCOL_REGEX.match(url)) is None):
        exit("Unable to detect repository from remote '%s'." % (url, ))      
    domain = match.group("domain")
    owner = match.group("owner")
    repo = match.group("repo")
    web_url = f"https://{domain}/{owner}/{repo}"
    webbrowser.open(web_url)


if __name__ == "__main__":
   main()
