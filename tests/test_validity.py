"""
Test for HTML and CSS validity
"""
from file_clerk import clerk
import pytest
from webcode_tk import validator_tools as validator

project_path = "project/"
project_path = "tests/test_project/"
html_results = []
html_files = clerk.get_all_files_of_type(project_path, "html")
for file in html_files:
    report = validator.get_markup_validity(file)
    expected = f"{file}: No Errors Found."
    if not report:
        result = expected
        html_results.append((result, expected))
    else:
        for error in report:
            error_message = error.get("message")
            result = f"{file}: {error_message}"
            html_results.append((result, expected))


@pytest.mark.parametrize("result,expected", html_results)
def test_html_validity(result, expected):
    assert result == expected
