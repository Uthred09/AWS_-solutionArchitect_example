terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.21.0"
    }
  }

  required_version = ">= 1.2"
}
provider "aws" {
    region = "us-east-1"
    endpoints {s3= "http://s3.localhost.localstack.cloud:4566"}
}

resource "aws_s3_bucket" "example-tf-bucket" {
}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.example-tf-bucket.id
  key    = "test_sucessfull.txt"
  source = "test.txt"
  
  etag= filemd5("test.txt")
}
