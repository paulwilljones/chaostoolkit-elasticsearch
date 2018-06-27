# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
import pytest
import requests_mock

from chaostoolkit_elasticsearch.actions import create_index


def test_create_index():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:9200/test",
            status_code=200,
            text="""
                 {
                "acknowledged": "true",
                "shards_acknowledged": "true",
                "index": "test"}
                """
        )

        created = create_index(
            base_url="http://localhost:9200",
            index_name="test",
            num_of_shards=1,
            num_of_replicas=1
        )

    assert created == """
                 {
                "acknowledged": "true",
                "shards_acknowledged": "true",
                "index": "test"}
                """


def test_create_index_fails():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:9200/test",
            status_code=404)

        with pytest.raises(FailedActivity) as ex:
            create_index(
                base_url="http://localhost:9200",
                index_name="test",
                num_of_shards=1,
                num_of_replicas=1
            )

        assert "Create index failed" in str(ex)
