from typing import Dict

from django.conf import settings
from pymongo import MongoClient


class MongoPageViewCounter:
    """
    Вспомогательный класс для хранения и получения числа просмотров страниц
    """

    def __init__(self,
                 host: str = settings.MONGODB_HOST,
                 port: int = settings.MONGODB_PORT,
                 username: str = settings.MONGODB_USERNAME,
                 password: str = settings.MONGODB_PASSWORD,
                 db_name: str = settings.MONGODB_DATABASE,
                 collection_name: str = 'page_view_counter',
                 counter_field_name: str = 'counter') -> None:
        client = MongoClient(host=host, port=port,
                             username=username, password=password)
        self.collection = client[db_name][collection_name]
        self.counter_field_name = counter_field_name

    def increment_page_view_counter(self, query_dict: Dict) -> None:
        """
        Инкрементирует число просмотров страницы, подходящей под поисковый
        запрос query_dict
        """
        self.collection.update_one(
            query_dict,
            {'$inc': {self.counter_field_name: 1}},
            upsert=True
        )

    def get_page_view_counter(self, query_dict: Dict) -> int:
        """
        Возвращает число просмотров страницы, подходящей под поисковый
        запрос query_dict
        """
        if matched_object := self.collection.find_one(query_dict):
            return matched_object[self.counter_field_name]
        return 0


page_view_counter = MongoPageViewCounter()
