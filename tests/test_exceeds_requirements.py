"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html


exact_num_elements_per_page = [
    ("main", 1),
]
min_required_elements_per_page = [
    ("hgroup", 1),
    ("article or section", 3),
    ("aside", 1),
    ("figure or div", 2),
    ("img", 2),
    ("p", 6),
    ("ul", 2),
    ("li", 8),
    ("a", 8),
    ]

project_path = "project/"

@pytest.fixture
def files():
    files = clerk.get_all_files_of_type(project_path, "html")
    return files


@pytest.mark.parametrize("element,num", exact_num_elements_per_page)
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


@pytest.mark.parametrize("element,num", min_required_elements_per_page)
def test_files_for_minimum_number_of_elements_per_page(element, num, files):
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
