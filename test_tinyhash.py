# coding: utf-8
"""
Test TinyHash
"""

from tinyhash import small_hash


def test_small_all():
    string = '19690114_1830'
    assert type(small_hash(string)) is str
    assert len(small_hash(string)) == 6
