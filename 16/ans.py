import boto3
from botocore.exceptions import NoCredentialsError

AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def create_bucket(bucket_name):
    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'
            }
        )
        acl_resp = s3.put_bucket_acl(
            Bucket=bucket_name,
            ACL='private'
        )

    except NoCredentialsError:
        print("Credentials error")

if __name__ == '__main__':
    bucket_name = 'your-unique-bucket-name'
    create_bucket(bucket_name)
