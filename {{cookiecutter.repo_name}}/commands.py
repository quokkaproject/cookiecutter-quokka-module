# coding: utf-8

from flask.ext.script import Command, Option
from .models import {{cookiecutter.repo_name|title}}


class List{{cookiecutter.repo_name|title}}(Command):
    "prints a list of {{cookiecutter.repo_name}}s"

    command_name = 'list_{{cookiecutter.repo_name}}s'

    option_list = (
        Option('--title', '-t', dest='title'),
    )

    def run(self, title=None):

        {{cookiecutter.repo_name}}s = {{cookiecutter.repo_name|title}}.objects
        if title:
            {{cookiecutter.repo_name}}s = {{cookiecutter.repo_name}}s(title=title)

        for {{cookiecutter.repo_name}} in {{cookiecutter.repo_name}}s:
            print({{cookiecutter.repo_name}})
