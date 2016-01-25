from list_keys import get_s3_conn, list_keys
from moto import mock_s3

def test_list_keys():

    expected_keys = ['key1', 'key2']

    moto = mock_s3()
    # We enter "moto" mode using this
    moto.start()

    # Get the connection object
    conn = get_s3_conn()

    # Set up S3 as we expect it to be
    conn.create_bucket('bucket_name')
    for name in expected_keys:
        k = conn.get_bucket('bucket_name').new_key(name)
        k.set_contents_from_string('abcdedsd')

    # Now call the actual function
    keys = list_keys()
    assert expected_keys == [k.name for k in keys]

    # get out of moto mode
    moto.stop()
