# -*- coding: utf-8 -*-

from chaoslib.exceptions import FailedActivity
from elasticsearch import Elasticsearch


def create_index(base_url: str, port: int, index_name: str) -> str:
    """

    :param base_url:
    :param index_name:
    :param port:
    :return:
    """

    es = Elasticsearch(hosts=[{'host': base_url, 'port': port}])

    r = es.indices.create(index=index_name, ignore=400)

    if r.status_code != 200:
        raise FailedActivity(
            "Create index failed: {m}".format(
                m=r.text))

    return r.text


def delete_index(base_url: str, port: int, index_name: str) -> str:
    """

    :param base_url:
    :param index_name:
    :param port:
    :return:
    """

    es = Elasticsearch(hosts=[{'host': base_url, 'port': port}])

    r = es.indices.delete(index=index_name, ignore=400)

    if r.status_code != 200:
        raise FailedActivity(
            "Delete index failed: {m}".format(
                m=r.text))

    return r.text

