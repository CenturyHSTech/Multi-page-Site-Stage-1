"""
Test for a bullet or number list with at least 3 list items.
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_layout_elements = [("h2", 2),
                            ("header", 1),
                            ("article or section", 1),
                            ("nav", 1),
                            ("ul", 1),
                            ("li", 4),
                            ("a", 4),
                            ("header", 1),
                            ("footer", 1)]
project_path = "project/"
project_path = "tests/test_project/"


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type(project_path, "html")
    return files


@pytest.mark.parametrize("element,num", required_layout_elements)
def test_files_for_required_layout_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        num_article_or_sections = html.get_num_elements_in_file("article",
                                                                file)
        num_article_or_sections += html.get_num_elements_in_file("section",
                                                                 file)
        if element == "article or section":
            assert num_article_or_sections >= num
        else:
            actual = html.get_num_elements_in_file(element, file)
            expected = num
            assert actual >= expected
