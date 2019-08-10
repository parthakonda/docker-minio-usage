import boto3
from botocore.client import Config


s3 = boto3.resource('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
                    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

# upload a file from local file system '/home/john/piano.mp3' to bucket 'songs' with 'piano.mp3' as the object name.
s3.Bucket('foo').upload_file('/Users/partha/sendemail.py', 'sendemail.py')

# download the object 'piano.mp3' from the bucket 'songs' and save it to local FS as /tmp/classical.mp3
s3.Bucket('foo').download_file('sendemail.py', '/Users/partha/myfile.py')

print("Downloaded 'sendemail.py' as  'myfile.py'. ")
