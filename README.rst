.. image:: https://travis-ci.org/zalando/turnstile.svg?branch=master
   :target: https://travis-ci.org/zalando/turnstile
   :alt: Build Status

.. image:: https://coveralls.io/repos/zalando/turnstile/badge.svg?branch=master
  :target: https://coveralls.io/r/zalando/turnstile?branch=master
  :alt: Code Coverage

.. image:: https://pypip.in/version/turnstile-core/badge.svg
   :target: https://pypi.python.org/pypi/turnstile-core
   :alt: Latest Version

.. image:: https://pypip.in/status/turnstile/badge.svg
   :target: https://pypi.python.org/pypi/turnstile-core
   :alt: Development Status

.. image:: https://img.shields.io/pypi/l/turnstile.svg
   :target: https://github.com/zalando/turnstile/blob/master/LICENSE
   :alt: License


Turnstile - Zalando Local Git Hooks
===================================

Configurable local git hooks.

Installation
------------
You can install turnstile using pip:

    # pip install zalando-turnstile

Alternative you can install it using setup.py

    # setup.py install

Adding and removing turnstile from a repository
-----------------------------------------------
To use turnstile in a repository you have to run `turnstile install` inside the repository.

To remove turnstile from a repository you have to run `turnstile remove` inside the repository.

Configuring turnstile
---------------------
You can configure the global hook behaviour by running `turnstile config`.

Currently you can only configure the hook verbosity.

Repository Configuration
------------------------
To use Turnstile you need to add a configuration file named `.turnstile.yml` to your repository.

You can find an example configuration in `turnstile repository <turnstile.yml.example>`_ and you can read can learn more
about the configuration options in the `documentation <docs/user/configuration.md>`_.

Other subcommands
-----------------
Turnstile has several useful subcommands available. You can check them in the
`subcommand list <docs/user/subcommands.md>`_.

Adding subcommands
------------------
Turnstile looks for command extensions in 'turnstile.commands' entry points.

To make a new subcommand create a 'click <http://click.pocoo.org>`_ command named `cmd` and add the module with command
to your setup.py entry points in the 'turnstile.commands' group.

Known Issues
------------
When you run turnstile in a new repository (i.e. a repository without commits) the hooks will not see any file changes.

License
-------
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
