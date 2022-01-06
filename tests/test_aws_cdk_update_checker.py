import pytest

from aws_cdk_update_checker import __version__
from aws_cdk_update_checker import main


def test_version():
    assert __version__ == '0.1.0'


def test_fetch_latest_version(mocker):
    mock_dict = [
        {'name': 'v1.1.0'},
        {'name': 'v1.1.1'},
    ]
    mocker.patch(
        'aws_cdk_update_checker.main.fetch_aws_cdk_all_releases',
        return_value=mock_dict
    )
    result = main.fetch_aws_cdk_latest_version()
    assert result == 'v1.1.1'


def test_thrown_exception_when_github_http_status_not_valid(mocker):
    mocker.patch(
        'aws_cdk_update_checker.main.get_aws_cdk_url',
        return_value='https://api.github.com/repos/morning-code/foo-bar/releases'
    )
    try:
        main.fetch_aws_cdk_latest_version()
        assert False
    except RuntimeError as ex:
        assert True
        assert str(ex) == '[404] could not fetch releases from github...please try again later!'


@pytest.mark.smoke
def test_smoke(capfd):
    result = main.fetch_aws_cdk_latest_version()
    assert isinstance(result, str)
    assert result.startswith('v')
