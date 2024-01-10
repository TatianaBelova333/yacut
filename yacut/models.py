from datetime import datetime
import os

from . import app, db
from .constants import ID_MAX_LENGTH, URL_MAX_LENGTH


class URLMap(db.Model):
    __tablename__ = 'url_map'

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(URL_MAX_LENGTH), nullable=False)
    short = db.Column(db.String(ID_MAX_LENGTH), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.short} - {self.original[:50]}'

    def to_dict(self):
        host = app.config['HOST']
        short_link = os.path.join(host, self.short)
        return dict(
            url=self.original,
            short_link=short_link,
        )
