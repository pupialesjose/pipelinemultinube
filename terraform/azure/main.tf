resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  #name     = var.resource_group_name != "" ? var.resource_group_name : "rg-vm-github-actions-${formatdate("YYYYMMDDHHMMSS", timestamp())}"
  location = var.location
}
