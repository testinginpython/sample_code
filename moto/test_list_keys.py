from list_keys import list_keys

from mock import patch, Mock

def test_list_keys():
    mocked_keys = [Mock(key='mykey1'), Mock(key='key2')]
    mocked_connection = Mock()
    # Start with patching connect_s3
    with patch('boto.connect_s3', Mock(return_value=mocked_connection)):
        mocked_bucket = Mock()
        # Mock get_bucket() call
        mocked_connection.get_bucket = Mock(return_value=mocked_bucket)
        # Mock the list() call to return the keys you want
        mocked_bucket.list = Mock(return_value=mocked_keys)
        keys = list_keys()

        assert keys == mocked_keys
