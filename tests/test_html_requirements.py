"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

# List of required elements per page
required_elements = [("doctype", 1),
                     ("html", 1),
                     ("head", 1),
                     ("title", 1),
                     ("header", 1),
                     ("article or section", 1),
                     ("footer", 1),
                     ("h1", 1),
                     ("h2", 2),
                     ("p", 5),
                     ("nav", 1),
                     ("ul", 1),
                     ("li", 4),
                     ("a", 4),
                     ]

project_path = "project/"
project_path = "tests/test_project/"

@pytest.fixture
def files():
    files = clerk.get_all_files_of_type(project_path, "html")
    return files


def test_for_presence_of_html_files(files):
    assert len(files) > 3


@pytest.mark.parametrize("element,num", required_elements)
def test_files_for_required_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        actual = html.get_num_elements_in_file(element, file)
        assert actual >= num
