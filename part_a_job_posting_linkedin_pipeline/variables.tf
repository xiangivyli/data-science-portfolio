variable "project" {
    description = "Project"
    default = "cedar-style-412618"
}

variable "region" {
    description = "Region"
    default = "us-central1"
}


variable "credentials" {
    description = " GCP credentials"
    default = "./airflow/include/.gc/airflow_to_gcs_bigquery.json"
}


variable "location" {
    description = "Project Location"
    default = "US"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}

variable "gcs_bucket_name" {
    description = "My Project Bucket"
    default = "de-zoomcamp-xiangivyli"
}