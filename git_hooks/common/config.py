#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

import logging

import gitconfig

logger = logging.getLogger('githooks.config')


def is_valid_log_verbosity(verbosity):
    """
    >>> is_valid_log_verbosity('WARNING')
    True

    >>> is_valid_log_verbosity('INFO')
    True

    >>> is_valid_log_verbosity('DEBUG')
    True

    >>> is_valid_log_verbosity('SOMETHINGELSE')
    False

    :type verbosity: str|int
    :rtype: bool
    """
    try:
        logging._checkLevel(verbosity)
        return True
    except (ValueError, TypeError):
        return False


class UserConfiguration(object):
    """
    User specific options


    >>> config=UserConfiguration()
    >>> config.store = dict()  # Don't mess up with real config
    >>> config.verbosity = 'DEBUG'
    >>> config.verbosity
    'DEBUG'
    >>> config.verbosity = 'INFO'
    >>> config.verbosity
    'INFO'
    >>> config.verbosity = 'OTHER'
    Traceback (most recent call last):
        ...
    ValueError: "OTHER" is not a valid verbosity
    >>> config.store['zalando.hooks.verbosity'] = 'BREAKSTUFF'
    >>> config.verbosity
    'INFO'
    """

    def __init__(self, level='global'):
        self.store = gitconfig.GitConfig(level)

    @property
    def verbosity(self):
        """
        Tries to get logging level from git config, falling back to INFO if it is not set or is an invalid value

        :return: Log Level
        :rtype: str
        """
        verbosity = self.store.get('zalando.hooks.verbosity', 'INFO')
        if not is_valid_log_verbosity(verbosity):
            logger.warning('Invalid Verbosity "%s" falling back to INFO', verbosity)
            verbosity = 'INFO'
        return verbosity

    @verbosity.setter
    def verbosity(self, value):
        """
        Store git hook verbosity in git config

        :type value: str | int
        :param value: new verbosity
        """
        if is_valid_log_verbosity(value):
            self.store['zalando.hooks.verbosity'] = value
        else:
            raise ValueError('"{}" is not a valid verbosity'.format(value))