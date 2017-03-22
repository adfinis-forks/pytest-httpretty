import functools

import pytest
import httpretty as _httpretty


__version__ = '0.2.0'


def pytest_configure(config):
    config.addinivalue_line('markers',
                            'httpretty: mark tests to activate HTTPretty.')


def pytest_runtest_setup(item):
    marker = item.get_marker('httpretty')
    if marker is not None:
        _httpretty.reset()
        _httpretty.enable()


def pytest_runtest_teardown(item, nextitem):
    marker = item.get_marker('httpretty')
    if marker is not None:
        _httpretty.disable()


@pytest.fixture
def httpretty():
    """
    A thin wrapper of httpretty which enables httpretty during setup
    and disables it while tearing down.
    """
    _httpretty.reset()
    _httpretty.enable()

    yield _httpretty

    _httpretty.disable()


stub_get = functools.partial(_httpretty.register_uri, _httpretty.GET)

last_request = _httpretty.last_request
