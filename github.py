""" Collects data from GitHub """

from git import Repo

#create github instance

def get_commits():
    PATH="."
        
    #get the repo from the current dir
    repo = Repo(PATH)

    #get commit log
    commits = list(repo.iter_commits())

    return commits


def print_commits(commits):
    for commit in commits:
        print(commit)

print_commits(get_commits())
