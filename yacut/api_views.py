from flask import jsonify, request, Blueprint

from . import db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import (get_unique_short_id, short_duplicate_exists,
                    short_id_is_valid)


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/', methods=['POST'])
def generate_short_id():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage(
            'Отсутствует тело запроса',
        )
    if 'url' not in data:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!',
        )

    custom_id = data.get('custom_id')

    if not custom_id:
        short_id = get_unique_short_id()
    else:
        short_id = custom_id
        if not short_id_is_valid(custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
            )
        if short_duplicate_exists(custom_id):
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.',
            )

    original_url = data['url']

    url_map = URLMap(
        original=original_url,
        short=short_id,
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@api_blueprint.route('/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage(
                'Указанный id не найден',
                404,
            )
    return jsonify({"url": url_map.original}), 200
