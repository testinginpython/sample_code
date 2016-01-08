# A program which expects a file to exist


def read_key():
    with open('/var/keys/1.pub') as f:
        return f.read()
