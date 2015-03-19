#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git_hooks.checks as checks
import git_hooks.common.output as output


@checks.Check('Specification is valid')
def check(user_configuration, repository_configuration, commit_message):
    """
    Check if the specification is valid.

    >>> import git_hooks.models.message as message
    >>> commit1 = message.CommitMessage('something', 'CD-1 m€sságe', 'jira')
    >>> result1 = check(None, None, commit1)
    >>> result1.successful
    True
    >>> result1.details
    []

    >>> commit2 = message.CommitMessage('something', 'invalid-1', 'jira')
    >>> result2 = check(None, None, commit2)
    >>> result2.successful
    False
    >>> result2.details
    ['invalid-1 is not a valid Jira specification id.']

    >>> commit3 = message.CommitMessage('something', 'invalid-1', None)
    >>> result3 = check(None, None, commit3)
    >>> result3.successful
    True
    >>> result3.details
    []

    :param user_configuration: User specific configuration
    :type user_configuration: git_hooks.common.config.UserConfiguration
    :param repository_configuration: Repository specific configuration
    :type repository_configuration: dict
    :param commit_message:
    :type commit_message: git_hooks.models.message.CommitMessage
    :return: If check passed or not
    :rtype: git_hooks.checks.CheckResult
    """

    logger = output.get_sub_logger('commit-msg', 'specification')
    logger.debug('Starting specification check...')
    logger.debug('Commit Message: %s', commit_message.message)

    result = checks.CheckResult()
    specification = commit_message.specification
    is_valid = specification.is_valid()

    logger.debug('Specification format: %s', specification.format)
    logger.debug("Specification is valid: %s", is_valid)

    result.successful = is_valid
    if not is_valid:
        result.add_detail('{spec} is not a valid {spec.format} specification id.'.format(spec=specification))

    return result
