output "vpc_id" {
  description = "The ID of the created VPC"
  value       = aws_vpc.ucodts_vpc.id
}

output "instance_public_ip" {
  description = "Public IP address of the UCODTS instance"
  value       = aws_instance.ucodts_instance.public_ip
}
