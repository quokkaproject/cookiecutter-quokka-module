#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from quokka.core.templates import render_template

from .models import {{cookiecutter.module_name|title}}

import logging
logger = logging.getLogger(__name__)


class ListView(MethodView):

    def get(self):
        logger.info('getting list of {{cookiecutter.module_name}}')
        {{cookiecutter.module_name}}s = {{cookiecutter.module_name|title}}.objects.all()
        return render_template('{{cookiecutter.module_name}}/list.html', {{cookiecutter.module_name}}s={{cookiecutter.module_name}}s)


class DetailView(MethodView):

    def get_context(self, slug):
        {{cookiecutter.module_name}} = {{cookiecutter.module_name|title}}.objects.get_or_404(slug=slug)

        context = {
            "{{cookiecutter.module_name}}": {{cookiecutter.module_name}}
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('{{cookiecutter.module_name}}s/detail.html', **context)
