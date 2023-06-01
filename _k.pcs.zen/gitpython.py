from git import Repo

import os

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with

# REDACTAR POST:

# CONFIG

EMAIL = "alesteba@unirioja.com"
NAME = "alesteba"

path = os.getcwd()

publish_path = os.path.join(path, '_k.pcs.zen','publish')

print(publish_path)

repo = Repo(publish_path)

print(repo)

assert not repo.bare

# check dirty files:

if repo.is_dirty(untracked_files=True):

    print('Changes detected.')

untracked_items = repo.untracked_files

untracked_items

# Check differences between current files and last commit

if len(untracked_items) > 0:

    diff = repo.git.diff(repo.head.commit.tree)

    print(diff)

## configue user name and email

with repo.config_writer() as git_config:
    
    git_config.set_value('user', 'email', EMAIL)
    git_config.set_value('user', 'name', NAME)

# To check configuration values, use `config_reader()`

with repo.config_reader() as git_config:

    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))

# List all branches

for branch in repo.branches:
    
    print(branch)

# List remotes

print('Remotes:')
for remote in repo.remotes:
    print(f'- {remote.name} {remote.url}')


# Reference a remote by its name as part of the object

print(f'Remote name: {repo.remotes.origin.name}')
print(f'Remote URL: {repo.remotes.origin.url}')

# genereate commit message here:

import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))

id_generator()


commit_des = id_generator()

# link repo and commit

repo.git.add(all=True)

repo.git.commit('-m', commit_des)

# push 

repo.remotes.origin.push()