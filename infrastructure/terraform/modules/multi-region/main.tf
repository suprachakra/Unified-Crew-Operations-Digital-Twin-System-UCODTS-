provider "aws" {
  region = var.region
}

resource "aws_instance" "ucodts_node" {
  ami           = var.ami_id
  instance_type = var.instance_type
  count         = var.instance_count
  tags = {
    Name = "UCODTS_Node"
  }
}
