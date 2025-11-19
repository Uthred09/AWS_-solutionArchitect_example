Step that I followed while learning checksums


"Created a s3 bucket name checksum-bucket"
./s3/bashscript/create-bucket checksum-bucket

#createa txt file to upload on this bucket

#use the respective method for respective checksums algorithms to find actual value of cheksums 
openssl dgst -sha1 -binary checksum-test.txt | base64


#https://docs.aws.amazon.com/AmazonS3/latest/API/API_Checksum.html

#upload the test file in s3 bucket with cheksum enable
awslocal s3api put-object \
--bucket checksum-bucket \
--key checksum-test.txt \
--body checksum-test.txt \
--checksum-algorithm="SHA1" \
--checksum-sha1="n3wfUUCIFf2yutSq3Vna9obKCaQ="

#get the uploaded file from s3 to local

awslocal s3api get-object \
--bucket checksum-bucket \
--key checksum-test.txt \
checksum-test-verify.txt

#Output of the get object, here the you can verify the file integrity
(awslocal) uthred09@UthredO9:~/AWS_-solutionArchitect_example/s3/checksum$ awslocal s3api get-object \
--bucket checksum-bucket \
--key checksum-test.txt \
checksum-test-verify.txt
{
    "AcceptRanges": "bytes",
    "LastModified": "Wed, 19 Nov 2025 10:12:50 GMT",
    "ContentLength": 27,
    "ETag": "\"c92eac5cb2ec1704a6f6af51a180659a\"",
    "ChecksumSHA1": "n3wfUUCIFf2yutSq3Vna9obKCaQ=",
    "ChecksumType": "FULL_OBJECT",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}
