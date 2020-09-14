from philter_lite import philter
import os
import pytest


def test_filter_from_dict():
    filter_dict = {
        "title": "test_city",
        "type": "regex",
        "filepath": "filters/regex/addresses/city.txt",
        "exclude": "test_ex",
        "notes": "test_notes"
    }

    filter = philter.filter_from_dict(filter_dict)

    assert filter.type == "regex"
    assert filter.title == "test_city"
    assert filter.filepath == os.path.abspath(os.path.join(os.path.dirname(__file__), "../philter_lite", "filters/regex/addresses/city.txt"))
    assert filter.exclude == "test_ex"
    assert filter.notes == "test_notes"
    assert isinstance(filter, philter.RegexFilter)

def test_filter_from_dict_missing_file():
    filter_dict = {
        "type": "regex",
        "filepath": "filters/regex/addresses/non_existent.txt"
    }

    with pytest.raises(Exception):
        philter.filter_from_dict(filter_dict)