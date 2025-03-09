provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "ucodts_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "UCODTS-VPC"
  }
}

resource "aws_subnet" "ucodts_subnet" {
  vpc_id     = aws_vpc.ucodts_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "UCODTS-Subnet"
  }
}

resource "aws_security_group" "ucodts_sg" {
  name        = "ucodts-sg"
  description = "Security group for UCODTS"
  vpc_id      = aws_vpc.ucodts_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "ucodts_instance" {
  ami           = "ami-0c94855ba95c71c99" # Example AMI (Amazon Linux 2)
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.ucodts_subnet.id
  security_groups = [aws_security_group.ucodts_sg.name]
  tags = {
    Name = "UCODTS-Instance"
  }
}
