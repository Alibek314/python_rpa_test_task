import tempfile
import pytest
import os
from solution import categorize_files_by_type


@pytest.fixture(scope='module')
def create_test_root_directory():
    # This function creates temporary directory for tests.
    temp_dir = tempfile.mkdtemp()

    with open(os.path.join(temp_dir, 'file_1.txt'), 'w') as f:
        f.write("File number 1")

    with open(os.path.join(temp_dir, 'file_2.txt'), 'w') as f:
        f.write("File number 2")

    with open(os.path.join(temp_dir, 'file_1.pdf'), 'w') as f:
        f.write("PDF_File number 1")

    with open(os.path.join(temp_dir, 'file_1.jpg'), 'w') as f:
        f.write("Image number 1")

    inner_folder = os.path.join(temp_dir, 'inner_folder')
    os.makedirs(inner_folder)
    with open(os.path.join(inner_folder, 'file_2.pdf'), 'w') as f:
        f.write("PDF_File number 2")
    return temp_dir


def test_empty_dir():
    temp_dir = tempfile.mkdtemp()
    result = categorize_files_by_type(temp_dir)
    assert result == {}


def test_base_correctness(create_test_root_directory):
    temp_dir = create_test_root_directory

    result = categorize_files_by_type(temp_dir)

    expect = {
        '.txt': [
            os.path.join(temp_dir, 'file_1.txt'),
            os.path.join(temp_dir, 'file_2.txt')
        ],
        '.pdf': [
            os.path.join(temp_dir, 'file_1.pdf'),
            os.path.join(temp_dir, 'inner_folder','file_2.pdf')
        ],
        '.jpg': [
            os.path.join(temp_dir, 'file_1.jpg')
        ]
    }

    assert expect == result
