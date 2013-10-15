# coding: utf-8

from flask import Blueprint
module = Blueprint("{{cookiecutter.repo_name}}", __name__, template_folder="templates")

# Register the urls if needed
# from .views import ListView, DetailView
# module.add_url_rule('/{{cookiecutter.repo_name}}/', view_func=ListView.as_view('list'))
# module.add_url_rule('/{{cookiecutter.repo_name}}/<slug>/', view_func=DetailView.as_view('detail'))

                   