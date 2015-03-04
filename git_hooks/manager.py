#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

from pathlib import Path
import logging

from click import Group, command
import click
import git

from .version import version

# TODO move this to module
output = logging.getLogger('githooks')
output.setLevel(logging.DEBUG)
output.addHandler(logging.StreamHandler())


@command('install')
def cmd_install():
    """
    Install git hooks in repository
    """

    output.info('Installing Git Hooks')
    try:
        repository = git.Repo()
    except git.InvalidGitRepositoryError:
        # TODO ERROR function
        output.error('This command should be run inside a git repository')
        exit(-1)

    hook_dir = Path(repository.git_dir) / 'hooks'
    pre_commit_path = hook_dir / 'pre-commit'
    commit_msg_path = hook_dir / 'commit-msg'
    install_hook('Pre-Commit', pre_commit_path, 'zalando-local-git-hooks-pre-commit')
    install_hook('Commit-Msg', commit_msg_path, 'zalando-local-git-hooks-commit-msg $1')


def install_hook(name, path, wrapper_command):
    """
    Installs a hook in path

    :type name: str
    :type path: Path
    :type wrapper_command: str
    """

    output.debug('Installing %s hook.', name)
    if not path.exists() or click.confirm('{} hook already exists. Do you want to overwrite it?'.format(name)):
        with path.open('wb+') as pre_commit_hook:
            pre_commit_hook.write(wrapper_command)
        path.chmod(0o755)  # -rwxr-xr-x
        output.info('Installed %s hook', name)
    else:
        output.info('Skipped %s hook installation.', name)


@command('remove')
def cmd_remove():
    """
    Remove git hooks from repository
    """

    output.info('Remove Git Hooks')
    try:
        repository = git.Repo()
    except git.InvalidGitRepositoryError:
        # TODO ERROR function
        output.error('This command should be run inside a git repository')
        exit(-1)

    hook_dir = Path(repository.git_dir) / 'hooks'
    pre_commit_path = hook_dir / 'pre-commit'
    commit_msg_path = hook_dir / 'commit-msg'
    remove_hook('Pre-Commit', pre_commit_path)
    remove_hook('Commit-Msg', commit_msg_path)


def remove_hook(name, path):
    """
    Installs a hook in path

    :type name: str
    :type path: Path
    """

    output.debug('Removing %s hook.', name)
    if not path.exists():
        output.debug('%s Hook doesn\'t exist.', name)
    elif click.confirm('Are you sure you want to remove {} hook?'.format(name)):
        path.unlink()
        output.info('Removed %s hook', name)
    else:
        output.info('Kept %s hook.', name)


@command('version')
def cmd_version():
    """
    Print Git Hook version
    """

    output.info('Zalando Local Git Hooks - %s', version)

manager = Group()
manager.add_command(cmd_install)
manager.add_command(cmd_remove)
manager.add_command(cmd_version)

if __name__ == '__main__':
    manager()
