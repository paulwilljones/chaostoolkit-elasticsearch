# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
import pytest
import requests_mock
from elasticmock import elasticmock


from chaostoolkit_elasticsearch.actions import create_index, delete_index

@elasticmock
def test_create_index():
    created = create_index('localhost', 9200, 'test')


def test_create_index_fails():
   created = create_index('localhost', 9200, 'test')


def test_delete_index():
    deleted = delete_index('localhost', 9200, 'test')


def test_delete_index_fails():
    deleted = delete_index('localhost', 9200, 'test')

