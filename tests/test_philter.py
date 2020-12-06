import os

import pytest

from philter_lite import philter


def test_filter_from_dict():
    filter_dict = {
        "title": "test_city",
        "type": "regex",
        "keyword": "addresses.city",
        "exclude": "test_ex",
        "notes": "test_notes",
    }

    filter = philter.filter_from_dict(filter_dict)

    assert filter.type == "regex"
    assert filter.title == "test_city"
    assert filter.data is not None
    assert filter.exclude == "test_ex"
    assert isinstance(filter, philter.RegexFilter)

    filter_dict = {
        "title": "Find Names 1",
        "type": "regex_context",
        "exclude": True,
        "context": "right",
        "context_filter": "Firstnames Blacklist",
        "keyword": "regex_context.names_regex_context1",
    }

    filter = philter.filter_from_dict(filter_dict)

    assert filter.type == "regex_context"
    assert filter.title == "Find Names 1"
    assert filter.data is not None
    assert filter.exclude is True
    assert filter.context == "right"
    assert filter.context_filter == "Firstnames Blacklist"
    assert isinstance(filter, philter.RegexContextFilter)

    filter_dict = {
        "title": "Whitelist 1",
        "type": "set",
        "exclude": False,
        "keyword": "nonames",
        "pos": [],
    }

    filter = philter.filter_from_dict(filter_dict)

    assert filter.type == "set"
    assert filter.title == "Whitelist 1"
    assert filter.data is not None
    assert filter.exclude is False
    assert filter.pos == []
    assert isinstance(filter, philter.SetFilter)

    filter_dict = {
        "title": "POS MATCHER",
        "type": "pos_matcher",
        "exclude": False,
        "pos": ["CD",],
    }

    filter = philter.filter_from_dict(filter_dict)

    assert filter.type == "pos_matcher"
    assert filter.title == "POS MATCHER"
    assert filter.exclude is False
    assert filter.pos == ["CD"]
    assert isinstance(filter, philter.PosFilter)


def test_filter_from_dict_missing_file():
    filter_dict = {
        "type": "regex",
        "filepath": "filters/regex/addresses/non_existent.txt",
    }

    with pytest.raises(Exception):
        philter.filter_from_dict(filter_dict)
