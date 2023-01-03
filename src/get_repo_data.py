#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests


REPO_LANG = None


repos = []
lista_completa = []


def get_branches(rep):
    """Gets the list of branches of a repo."""
    repo_branches = []
    branches_url = f"https://api.github.com/repos/TorrezMN/{rep}/branches"
    branches_data = json.loads(requests.get(branches_url).text)

    for k, v in enumerate(branches_data):
        repo_branches.append(v["name"])

    return repo_branches


def get_langs(rep):
    """Gets a list of languagues used in the repo."""
    languages_url = f"https://api.github.com/repos/TorrezMN/{rep}/languages"
    langs_data = json.loads(requests.get(languages_url).text)
    if len(langs_data) > 0:
        return [i for i in langs_data.keys()]
    else:
        return None


def get_repos():
    """Gets a full list of my repos."""
    username = "torrez.mn@gmail.com"
    token = "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"
    repos_url = "https://api.github.com/users/TorrezMN/repos"
    data = requests.get(repos_url, auth=(username, token))

    global new_data

    new_data = json.loads(data.text)

    for i, v in enumerate(new_data):
        if not v["fork"]:
            repos.append(v)


#  GETTING REPOS DATA
get_repos()


#  LOADING EXTRA DATA
for i in repos:
    branches = get_branches(i["name"])
    languages = get_langs(i["name"])

    lista_completa.append(
        {
            "nombre": i["name"],
            "data": {
                "url": i["html_url"],
                "DESCRIPCION": i["description"],
                "FORK": i["fork"],
                "URL": i["url"],
                "ESTRELLAS": i["stargazers_count"],
                "branches": branches,
                "languages": languages,
            },
        }
    )


#  SAVE DATA TO JSON FILE
with open("repos_data.json", "w", encoding="utf-8") as f:
    json.dump(lista_completa, f, ensure_ascii=False, indent=4)
