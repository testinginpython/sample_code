import boto

def get_s3_conn():
    return boto.connect_s3('<aws-access-key', '<aws-secret-key>')

def list_keys():
    s3_conn = get_s3_conn()
    b = s3_conn.get_bucket('bucket_name')
    keys = b.list()
    return keys
