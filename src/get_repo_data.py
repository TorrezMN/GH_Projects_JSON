#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests

REPOS_URL = "https://api.github.com/users/TorrezMN/repos"

REPO_LANG = None


def get_langs(rep):
    """Gets a list of languagues used in the repo."""
    langs_url = requests.get(f"https://api.github.com/repos/TorrezMN/{rep}/languages")


def save_data():
    with open("repos_data.json", "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)


def get_repos():
    """Gets a full list of my repos."""

    data = requests.get(REPOS_URL)

    new_data = json.loads(data.text)

    for i in new_data:
        if not i["fork"]:
            print("DATA -> ", i["name"])


get_repos()

get_langs("PlaceHolder_FA")
