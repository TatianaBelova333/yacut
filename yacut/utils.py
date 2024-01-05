from random import sample
import re
from string import ascii_letters, digits
from typing import Any

from .constants import SHORT_ID_REQS
from .models import URLMap


def get_unique_short_id(lenght: int = 6) -> str:
    """
    Generate a unique random id of given length (6 symbols by default)
    containing digits and ascii letters.

    """
    while True:
        unique_short_id: str = generate_unique_short_id(lenght)
        if not short_duplicate_exists(unique_short_id):
            break
    return unique_short_id


def generate_unique_short_id(lenght: int = 6) -> str:
    """
    Generate a random id of given length (6 symbols by default)
    containing digits and ascii letters.

    """
    allowed_symbols: str = ascii_letters + digits
    random_symbols: list[str] = sample(allowed_symbols, lenght)
    unique_id: str = ''.join(random_symbols)
    return unique_id


def short_duplicate_exists(short_id) -> bool:
    """
    Check if the given short_id has a duplicate in the db.
    Return True if the duplicate exists. False, otherwise.

    """
    url_short = URLMap.query.filter_by(
        short=short_id,
    ).first()
    return bool(url_short)


def short_id_is_valid(short_id: Any) -> bool:
    """
    Return True, if the short_id is valid.
    False, otherwise.

    """
    return (isinstance(short_id, str)
            and bool(re.fullmatch(SHORT_ID_REQS, short_id)))
