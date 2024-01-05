from datetime import datetime
import os

from . import app, db


class URLMap(db.Model):
    __tablename__ = 'url_map'

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2000), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
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
