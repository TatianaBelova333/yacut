from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .constants import (ID_MAX_LENGTH, SHORT_ID_REQS,
                        URL_MAX_LENGTH, URL_MIN_LENGTH)


class URLMapForm(FlaskForm):
    original_link = TextAreaField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(URL_MIN_LENGTH, URL_MAX_LENGTH),
            URL(message='Некорректный URL'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(URL_MIN_LENGTH, ID_MAX_LENGTH),
            Regexp(
                regex=SHORT_ID_REQS,
                message=('Ссылка может включать до 16 знаков, включающих '
                         'латинские буквы и цифры.')
            )
        ]
    )
    submit = SubmitField('Создать')
