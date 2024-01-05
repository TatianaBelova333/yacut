from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .constants import SHORT_ID_REQS


class URLMapForm(FlaskForm):
    original_link = TextAreaField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 2000),
            URL(message='Некорректный URL'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Regexp(
                regex=SHORT_ID_REQS,
                message=('Ссылка может включать до 16 знаков, включающих '
                         'латинские буквы и цифры.')
            )
        ]
    )
    submit = SubmitField('Создать')
