#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests

repos_url = "https://api.github.com/users/TorrezMN/repos"

REPO_LANG = None


repos = []


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
            repos.append(i)


get_repos()


for i in repos:
    print("NOMBRE -> ", i["name"])
    print("URL -> ", i["html_url"])
    print("DESCRIPCION : ", i["description"])
    print("FORK : ", i["fork"])
    print("URL : ", i["url"])
    print("ESTRELLAS : ", i["stargazers_count"])
