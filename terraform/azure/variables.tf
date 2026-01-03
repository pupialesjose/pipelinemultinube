variable "location" {
  default = "East US 2"
}

variable "resource_group_name" {
  default = "rg-vm-github-actions"
}


#variable "resource_group_name" {
#  description = "Nombre del grupo de recursos."
#  type        = string
#  default     = ""
#}


variable "vm_size" {
  default = "Standard_B1s"
}

variable "admin_username" {
  default = "azureuser"
}

variable "ssh_public_key" {}
