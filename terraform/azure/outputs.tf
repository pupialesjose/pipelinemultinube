output "vm_public_ip" {
  description = "IP pública de la VM en Azure"
  value       = azurerm_public_ip.pip.ip_address
}
