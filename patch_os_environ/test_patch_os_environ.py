import mock
import os

def test_patch_os_environ():

    # Original os.environ
    before_patch = os.environ
    # Custom os.environ
    my_os_environ = {'key': 'value'}

    with mock.patch('os.environ', my_os_environ):
        assert os.environ == my_os_environ
    # Assert that the origianl os.environ is preserved
    assert os.environ == before_patch
