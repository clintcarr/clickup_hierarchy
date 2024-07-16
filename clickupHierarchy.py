#!/usr/bin/env python
""" 
Small script to generate a basic view of a Clickup Hierarchy
Version: 0.1
Date: 16/07/24
Author: Clint Carr
"""
import json, requests

# Use the Clickup console to create a personal token
token = "pk_###"
# Get your teamId from the url
teamId = "###"
url = "https://api.clickup.com/api/v2/team/" + teamId + "/space"
headers = {"Authorization": token}
query = {"archived": "false"}

def get_space():
    """
    Function that performs GET to collect spaces
    """
    response = requests.get(url.format (teamId),headers=headers, params=query)
    data = response.json()
    clSpaces = {}
    for i in data['spaces']:
        clSpaces.update({i['id']: i['name']})
    return(clSpaces)

def get_folders(spaceId):
    """
    Function to return folders from defined space
    """
    clFolders = {}
    
    url = "https://api.clickup.com/api/v2/space/"+ spaceId+ "/folder"
    response = requests.get(url, headers=headers, params=query)
    data = response.json()
    for i in data['folders']:
        clFolders.update({i['id']: i['name']})
    return(clFolders)


def get_lists(folderId):
    """
    Function to return lists from defined folders
    """
    clLists = {}

    url = "https://api.clickup.com/api/v2/folder/" + folderId + "/list"
    response = requests.get(url, headers=headers, params=query)
    data = response.json()
    for i in data['lists']:
        clLists.update({i['id']: i['name']})
    return clLists

def get_tasks(listId):
    """
    Function to return tasks from defined lists
    """
    cltasks = {}
    url = "https://api.clickup.com/api/v2/list/" + listId + "/task"
    response = requests.get(url, headers=headers, params=query)
    data = response.json()
    for i in data['tasks']:
        cltasks.update({i['id']: i['name']})
    return cltasks

if __name__ == '__main__':
    clSpace = get_space()
    for keys,values in clSpace.items():
        print(values+ ' (space)')
        clFolders = get_folders(keys)
        for fkeys,fvalues in clFolders.items():
            print('\t' +fvalues+ ' (folder)')
            clLists = get_lists(fkeys)
            for lkeys,lvalues in clLists.items():
                print('\t\t'+ lvalues+ ' (list)')
                clTasks = get_tasks(lkeys)
                for tkeys,tvalues in clTasks.items():
                    print('\t\t\t'+tvalues+ ' (task)')