terraform {
  required_version = ">= 0.1, 2"
  required_providers {
    aws = ">= 1.0"
    Source = "hashcor/aws"    
  }
    azurerm = {
        version = "2.0"
       Source = "hashcorp/azurerm"       
    }

  
}
