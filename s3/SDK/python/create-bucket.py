import boto3
import os

#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
def create_bucket(bucket_name, region='us-east-1'):
    # Create S3 client
    s3_client = boto3.client(
        's3',
        endpoint_url=os.getenv("LOCALSTACK_ENDPOINT"),
        region_name=region
    )
    # Only set LocationConstraint for non-us-east-1 regions
    # bucket_config = {}
    # if region != 'us-east-1':
    #     bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}

    #create s3 bucket
    response = s3_client.create_bucket(
        Bucket= bucket_name,
        #**bucket_config,
    )
    print(f"Bucket Successfully created...", bucket_name, "on region", region )

#get bucket name from user
bucket_name = input("Enter Buckert Name: ")
create_bucket(bucket_name)




    



