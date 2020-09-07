module "vpc" {
  source = "./vpc_module"
  cidr_block = var.vpc_cidr_block
  name = var.vpc_name
  environment = var.vpc_environment
}