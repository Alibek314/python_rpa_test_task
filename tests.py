import tempfile

import pytest
import os
from solution import categorize_files_by_type


def test_empty_dir():
    assert '/empty_directory' == {}


def test_root_file():
    pass