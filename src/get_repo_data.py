#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests

repos_url = "https://api.github.com/users/TorrezMN/repos"

REPO_LANG = None


def get_branches(rep):
    """Gets the list of branches of a repo."""
    branches_url = f"https://api.github.com/repos/TorrezMN/{rep}/branches"
    branches_data = requests.get(branches_url)
    return json.loads(branches_data.text)


def get_langs(rep):
    """Gets a list of languagues used in the repo."""
    languages_url = f"https://api.github.com/repos/TorrezMN/{rep}/languages"
    langs_data = requests.get(languages_url)
    return json.loads(langs_data.text)


def save_data():
    with open("repos_data.json", "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)


def get_repos():
    """Gets a full list of my repos."""

    data = requests.get(repos_url)

    global new_data

    new_data = json.loads(data.text)

    for i in new_data:
        if not i["fork"]:
            print("DATA -> ", i["name"])


#  GET REPOS
get_repos()
#  SAVE REPO DATA
#  save_data()
#  GET REPO LANGS
print(get_langs("PlaceHolder_FA"))
#  GET BRANCHES OF A REPO
print(get_branches("Data_Science"))
