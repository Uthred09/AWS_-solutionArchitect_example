import boto3
import os

#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket.html
def delete_bucket(bucket_name):
    # Create S3 client
    s3_client = boto3.client(
        's3',
        endpoint_url=os.getenv("LOCALSTACK_ENDPOINT"),
    )
    s3_client.delete_bucket(Bucket= bucket_name)
    print(f"Bucket Successfully deleted...", bucket_name)

#get bucket name from user
bucket_name = input("Enter Buckert Name: ")
delete_bucket(bucket_name)




    



