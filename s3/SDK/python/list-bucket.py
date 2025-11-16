import boto3
import os


# Retrieve the list of existing buckets
s3 = boto3.client('s3',endpoint_url=os.getenv("LOCALSTACK_ENDPOINT"))
response = s3.list_buckets()

# Output the bucket names
print(f"{'Name':<20} {'CreationDate':<30} {'Region':<15}")
print("-" * 65)
for bucket in response['Buckets']:
    name = bucket['Name']
    date = bucket['CreationDate']
    region = bucket['BucketRegion']
    print(f"{name:<20} {str(date):<30} {region:<15}")