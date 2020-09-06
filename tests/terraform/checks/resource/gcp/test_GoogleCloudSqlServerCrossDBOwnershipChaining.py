import unittest

import hcl2

from checkov.terraform.checks.resource.gcp.GoogleCloudSqlServerCrossDBOwnershipChaining import check
from checkov.common.models.enums import CheckResult


class TestCloudSQLServerCrossDBOwnershipChaining(unittest.TestCase):

    def test_failure(self):
        hcl_res = hcl2.loads("""    
            resource "google_sql_database_instance" "tfer--gilad-002D-sqlserver12" {
            database_version = "SQLSERVER_2017_STANDARD"
            name             = "gilad-sqlserver12"
            project          = "gcp-bridgecrew-deployment"
            region           = "us-central1"
            
            settings {
                activation_policy = "ALWAYS"
                availability_type = "ZONAL"
            
                backup_configuration {
                  binary_log_enabled             = "false"
                  enabled                        = "true"
                  location                       = "us"
                  point_in_time_recovery_enabled = "false"
                  start_time                     = "00:00"
                }
            
                crash_safe_replication = "false"
            
                database_flags {
                  name  = "cross db ownership chaining"
                  value = "on"
                }
            
                database_flags {
                  name  = "contained database authentication"
                  value = "off"
                }
            
                disk_autoresize = "true"
                disk_size       = "20"
                disk_type       = "PD_SSD"
            
                ip_configuration {
                  ipv4_enabled    = "false"
                  private_network = "projects/gcp-bridgecrew-deployment/global/networks/default"
                  require_ssl     = "false"
                }
            
                location_preference {
                  zone = "us-central1-a"
                }
            
                maintenance_window {
                  day  = "0"
                  hour = "0"
                }
            
                pricing_plan     = "PER_USE"
                replication_type = "SYNCHRONOUS"
                tier             = "db-custom-1-4096"
              }
            }

                """)
        resource_conf = hcl_res['resource'][0]['google_sql_database_instance']['tfer--gilad-002D-sqlserver12']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        hcl_res = hcl2.loads("""
            resource "google_sql_database_instance" "tfer--gilad-002D-sqlserver12" {
            database_version = "SQLSERVER_2017_STANDARD"
            name             = "gilad-sqlserver12"
            project          = "gcp-bridgecrew-deployment"
            region           = "us-central1"
            
            settings {
                activation_policy = "ALWAYS"
                availability_type = "ZONAL"
            
                backup_configuration {
                  binary_log_enabled             = "false"
                  enabled                        = "true"
                  location                       = "us"
                  point_in_time_recovery_enabled = "false"
                  start_time                     = "00:00"
                }
            
                crash_safe_replication = "false"
            
                database_flags {
                  name  = "cross db ownership chaining"
                  value = "off"
                }
            
                database_flags {
                  name  = "contained database authentication"
                  value = "off"
                }
            
                disk_autoresize = "true"
                disk_size       = "20"
                disk_type       = "PD_SSD"
            
                ip_configuration {
                  ipv4_enabled    = "false"
                  private_network = "projects/gcp-bridgecrew-deployment/global/networks/default"
                  require_ssl     = "false"
                }
            
                location_preference {
                  zone = "us-central1-a"
                }
            
                maintenance_window {
                  day  = "0"
                  hour = "0"
                }
            
                pricing_plan     = "PER_USE"
                replication_type = "SYNCHRONOUS"
                tier             = "db-custom-1-4096"
              }
            }
                        """)
        resource_conf = hcl_res['resource'][0]['google_sql_database_instance']['tfer--gilad-002D-sqlserver12']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)

    def test_success_2(self):
        hcl_res = hcl2.loads("""
            resource "google_sql_database_instance" "tfer--gilad-002D-sqlserver12" {
            database_version = "SQLSERVER_2017_STANDARD122"
            name             = "gilad-sqlserver12"
            project          = "gcp-bridgecrew-deployment"
            region           = "us-central1"
            
            settings {
                activation_policy = "ALWAYS"
                availability_type = "ZONAL"
            
                backup_configuration {
                  binary_log_enabled             = "false"
                  enabled                        = "true"
                  location                       = "us"
                  point_in_time_recovery_enabled = "false"
                  start_time                     = "00:00"
                }
            
                crash_safe_replication = "false"
            
                database_flags {
                  name  = "cross db ownership chaining"
                  value = "on"
                }
            
                database_flags {
                  name  = "contained database authentication"
                  value = "off"
                }
            
                disk_autoresize = "true"
                disk_size       = "20"
                disk_type       = "PD_SSD"
            
                ip_configuration {
                  ipv4_enabled    = "false"
                  private_network = "projects/gcp-bridgecrew-deployment/global/networks/default"
                  require_ssl     = "false"
                }
            
                location_preference {
                  zone = "us-central1-a"
                }
            
                maintenance_window {
                  day  = "0"
                  hour = "0"
                }
            
                pricing_plan     = "PER_USE"
                replication_type = "SYNCHRONOUS"
                tier             = "db-custom-1-4096"
              }
            }
                        """)
        resource_conf = hcl_res['resource'][0]['google_sql_database_instance']['tfer--gilad-002D-sqlserver12']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)

    def test_success_3(self):
        hcl_res = hcl2.loads("""
             resource "google_sql_database_instance" "tfer--gilad-002D-sqlserver12" {
            database_version = "SQLSERVER_2017_STANDARD"
            name             = "gilad-sqlserver12"
            project          = "gcp-bridgecrew-deployment"
            region           = "us-central1"           
            settings {
                activation_policy = "ALWAYS"
                availability_type = "ZONAL"
            
                backup_configuration {
                  binary_log_enabled             = "false"
                  enabled                        = "true"
                  location                       = "us"
                  point_in_time_recovery_enabled = "false"
                  start_time                     = "00:00"
                }
                crash_safe_replication = "false"
                database_flags {
                  name  = "contained database authentication"
                  value = "off"
                }
            
                disk_autoresize = "true"
                disk_size       = "20"
                disk_type       = "PD_SSD"
            
                ip_configuration {
                  ipv4_enabled    = "false"
                  private_network = "projects/gcp-bridgecrew-deployment/global/networks/default"
                  require_ssl     = "false"
                }
            
                location_preference {
                  zone = "us-central1-a"
                }
            
                maintenance_window {
                  day  = "0"
                  hour = "0"
                }
            
                pricing_plan     = "PER_USE"
                replication_type = "SYNCHRONOUS"
                tier             = "db-custom-1-4096"
              }
            }
                        """)
        resource_conf = hcl_res['resource'][0]['google_sql_database_instance']['tfer--gilad-002D-sqlserver12']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)

    def test_success_4(self):
        hcl_res = hcl2.loads("""
             resource "google_sql_database_instance" "tfer--gilad-002D-sqlserver12" {
            database_version = "SQLSERVER_2017_STANDARD"
            name             = "gilad-sqlserver12"
            project          = "gcp-bridgecrew-deployment"
            region           = "us-central1"           
            }
                        """)
        resource_conf =hcl_res['resource'][0]['google_sql_database_instance']['tfer--gilad-002D-sqlserver12']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == '__main__':
    unittest.main()
