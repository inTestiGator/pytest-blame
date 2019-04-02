""" Collects data from GitHub """

from git import Repo

# create github instance


def get_commits():
    """ Query git commit log and return a list of commits """
    PATH = "."

    # get the repo from the current dir
    repo = Repo(PATH)

    # get commit log
    commits = list(repo.iter_commits())

    return commits


def print_commits(commits):
    """ Prints relevant info for commit history """
    for commit in commits:
        print(commit, commit.author, ":", commit.message)


print_commits(get_commits())
