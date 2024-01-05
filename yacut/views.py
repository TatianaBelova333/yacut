from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id, short_duplicate_exists


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original_url = form.original_link.data
        custom_url = form.custom_id.data

        if not custom_url:
            custom_url = get_unique_short_id()
        else:
            if short_duplicate_exists(custom_url):
                flash(
                    message=('Предложенный вариант короткой ссылки '
                             'уже существует.'),
                    category='duplicate-short',
                )
                return render_template('index.html', form=form)

        new_url_map = URLMap(
            original=original_url,
            short=custom_url,
        )
        db.session.add(new_url_map)
        db.session.commit()
        flash(message='Ваша новая ссылка готова:', category='url-success')
        return render_template('index.html', form=form, url_map=new_url_map)

    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def short_url_view(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
