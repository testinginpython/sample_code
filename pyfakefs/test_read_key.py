from read_key import read_key
from mock import patch

# We will use pyfakefs to create a file in the
# location read_key() expects
import fake_filesystem

def test_read_key():

    # Create a fake filesystem
    fakefs = fake_filesystem.FakeFilesystem()
    # Create a file our code expects to find
    fakefs.CreateFile('/var/keys/1.pub', contents='$3432adsd')

    # The FakeFileOpen class patches the built-in open()
    # function
    fake_open = fake_filesystem.FakeFileOpen(fakefs)
    with patch('read_key.open', fake_open):
        assert read_key()
