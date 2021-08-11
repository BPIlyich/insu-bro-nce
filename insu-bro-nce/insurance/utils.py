from urllib.parse import urlencode
from typing import Optional, Dict

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.conf import settings
from pymongo import MongoClient

from django_tables2.utils import AttributeDict


def build_link(url: str, get: Optional[dict] = None, text: Optional[str] = None,
               attrs: Optional[dict] = None, as_is: bool = False) -> str:
    """
    Возвращает экранированный html тег <a> для использования в шаблонах django
    """
    if get:
        url = '?'.join([url, urlencode(get)])
    if not text:
        text = url
    elif text and not as_is:
        text = escape(text)
    attrs = AttributeDict(attrs if attrs else {})
    attrs['href'] = url
    html = f'<a {attrs.as_html()}>{text}</a>'
    return mark_safe(html)


def update_page_counter(query_dict: Dict[str, str],
                        counter_field_name: str = 'counter',
                        mongo_host: str = settings.MONGODB_HOST,
                        mongo_port: int = settings.MONGODB_PORT,
                        mongo_username: str = settings.MONGODB_USERNAME,
                        mongo_password: int = settings.MONGODB_PASSWORD,
                        mongo_db_name: str = settings.MONGODB_DATABASE,
                        collection_name: str = 'page_view_counter') -> None:
    """
    Инкрементируем счетчик просмотров страницы
    """
    client = MongoClient(host=mongo_host, port=mongo_port,
                         username=mongo_username, password=mongo_password)
    client[mongo_db_name][collection_name].update_one(
        query_dict,
        {'$inc': {counter_field_name: 1}},
        upsert=True
    )


def get_page_counter(query_dict: Dict[str, str],
                     counter_field_name: str = 'counter',
                     mongo_host: str = settings.MONGODB_HOST,
                     mongo_port: int = settings.MONGODB_PORT,
                     mongo_username: str = settings.MONGODB_USERNAME,
                     mongo_password: int = settings.MONGODB_PASSWORD,
                     mongo_db_name: str = settings.MONGODB_DATABASE,
                     collection_name: str = 'page_view_counter') -> int:
    """
    Возвращает список просмотров страницы
    """
    client = MongoClient(host=mongo_host, port=mongo_port,
                         username=mongo_username, password=mongo_password)
    if doc := client[mongo_db_name][collection_name].find_one(query_dict):
        return doc[counter_field_name]
    return 0
