resource "aws_s3_bucket" "bucket1" {
  bucket = "my-tf-test"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "bucket2" {
  bucket = ""

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}