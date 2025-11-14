"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

# List of required elements per page
exact_required_elements = [
    ("doctype", 1),
    ("html", 1),
    ("head", 1),
    ("title", 1),
    ("header", 1),
    ("h1", 1),
    ]
min_required_elements = [
    ("nav", 1),
    ("article or section", 1),
    ("h2", 3),
    ("p", 5),
    ("ul", 1),
    ("li", 4),
    ("a", 4),
    ("footer", 1),
    ]

project_path = "project/"

@pytest.fixture
def files():
    files = clerk.get_all_files_of_type(project_path, "html")
    return files


def test_for_minimum_number_of_html_files(files):
    assert len(files) > 3


@pytest.mark.parametrize("element,num", exact_required_elements)
def test_files_for_exact_number_of_elements_per_page(element, num, files):
    if not files:
        assert False
    for file in files:
        if "or" in element:
            options = [opt.strip() for opt in element.split("or")]
            total = 0
            for opt in options:
                total += html.get_num_elements_in_file(opt, file)
            assert total == num
        else:
            actual = html.get_num_elements_in_file(element, file)
            assert actual == num


@pytest.mark.parametrize("element,num", min_required_elements)
def test_files_for_minimum_required_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        if "or" in element:
            options = [opt.strip() for opt in element.split("or")]
            total = 0
            for opt in options:
                total += html.get_num_elements_in_file(opt, file)
            assert total >= num
        else:
            actual = html.get_num_elements_in_file(element, file)
            assert actual >= num
