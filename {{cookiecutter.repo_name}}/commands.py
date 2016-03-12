# coding: utf-8

from __future__ import print_function

from flask.ext.script import Command, Option
from .models import {{cookiecutter.module_name|title}}


class List{{cookiecutter.module_name|title}}(Command):
    "prints a list of {{cookiecutter.module_name}}s"

    command_name = 'list_{{cookiecutter.module_name}}s'

    option_list = (
        Option('--title', '-t', dest='title'),
    )

    def run(self, title=None):

        {{cookiecutter.module_name}}s = {{cookiecutter.module_name|title}}.objects
        if title:
            {{cookiecutter.module_name}}s = {{cookiecutter.module_name}}s(title=title)

        for {{cookiecutter.module_name}} in {{cookiecutter.module_name}}s:
            print({{cookiecutter.module_name}})
