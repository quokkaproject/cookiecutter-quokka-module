#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask.views import MethodView
from quokka.core.templates import render_template

from .models import {{cookiecutter.repo_name|title}}

import logging
logger = logging.getLogger()


class ListView(MethodView):

    def get(self):
        logger.info('getting list of posts')
        {{cookiecutter.repo_name}}s = {{cookiecutter.repo_name|title}}.objects.all()
        return render_template('{{cookiecutter.repo_name}}/list.html', {{cookiecutter.repo_name}}s={{cookiecutter.repo_name}}s)


class DetailView(MethodView):

    def get_context(self, slug):
        {{cookiecutter.repo_name}} = {{cookiecutter.repo_name|title}}.objects.get_or_404(slug=slug)

        context = {
            "{{cookiecutter.repo_name}}": {{cookiecutter.repo_name}}
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('{{cookiecutter.repo_name}}s/detail.html', **context)
        