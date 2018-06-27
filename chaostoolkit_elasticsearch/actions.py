# -*- coding: utf-8 -*-
import json

from chaoslib.exceptions import FailedActivity
import requests


def create_index(base_url: str, index_name: str, num_of_shards: int = 3, num_of_replicas: int = 2) -> str:
    """

    :param base_url:
    :param index_name:
    :param num_of_shards:
    :param num_of_replicas:
    :return:
    """

    url = "{base_url}/{index_name}".format(base_url=base_url, index_name=index_name)

    params = {}

    payload = {
        "num_of_replicas": num_of_replicas,
        "num_of_shards": num_of_shards
    }

    r = requests.post(
            url, headers={"Accept": "application/json",
                          "Content-Type": "application/json"},
            data=json.dumps(payload), params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "Create index failed: {m}".format(
                m=r.text))

    return r.text
