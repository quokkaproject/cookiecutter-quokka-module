# coding: utf-8

from quokka.core.db import db
from quokka.core.models import Content

    
class Campaign(Content):
    body = db.StringField(required=True)
    