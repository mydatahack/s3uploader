import boto3

class S3:
    """
    S3 class with upload and download methods
    For Python package demo
    """

    def __init__ (self, bucket, key, local_file):
        """Initialising s3 object with bucket & key"""
        self.bucket = bucket
        self.key = key
        self.local_file = local_file
        self.s3 = boto3.resource('s3')
        self.s3_path = bucket + '/' + key

    def upload(self):
        """Upload file from local machine"""

        print('Uploading {} to {}'.format(self.local_file, self.s3_path))
        self.s3.meta.client.upload_file(self.local_file, self.bucket, self.key)
        print('Upload Completed')

    def download(self):
        """Download file to local machine"""

        print('Downloading {} to {}'.format(self.s3_path, self.local_file))
        self.s3.Bucket(self.bucket).download_file(self.key, self.local_file)
        print('Download Completed')

        

