#!/usr/bin/env python3

import re
import subprocess


GITHUB_SSH_REGEX = re.compile(r'git@(?P<domain>.+):(?P<owner>.+)/(?P<repo>.+).git')
SSH_PROTOCOL_REGEX = re.compile(r'ssh://git@(?P<domain>.+)/(?P<owner>.+)/(?P<repo>.+).git')


class Remote(object):

    def __init__(self, domain, owner, repo):
        self.domain = domain
        self.owner = owner
        self.repo = repo

    @property
    def url(self):
        return f"https://{self.domain}/{self.owner}/{self.repo}"


def get_remote():
    url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"]).decode("utf-8").strip()
    if ((match := GITHUB_SSH_REGEX.match(url)) is None) and ((match := SSH_PROTOCOL_REGEX.match(url)) is None):
        return None
        exit("Unable to detect repository from remote.")

    domain = match.group("domain")
    owner = match.group("owner")
    repo = match.group("repo")

    return Remote(domain, owner, repo)
