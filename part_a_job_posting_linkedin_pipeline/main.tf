terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.26.0"
    }
  }
}

provider "google" {
  credentials = "./airflow/include/.gc/airflow_to_gcs_bigquery.json"
  project     = "cedar-style-412618"
  region      = "us-central1"
}

resource "google_storage_bucket" "zoomcamp_bucket" {
  name          = "de-zoomcamp-xiangivyli"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 365
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_storage_bucket_object" "folder_2024_03_31" {
  name   = "2024-03-31/"
  bucket = google_storage_bucket.zoomcamp_bucket.name
  content = "placeholder"
  content_type = "application/x-directory"
}

resource "google_storage_bucket_object" "folder_parquet" {
  name   = "2024-03-31/parquet/"
  bucket = google_storage_bucket.zoomcamp_bucket.name
  content = "placeholder"
  content_type = "application/x-directory"
}

resource "google_storage_bucket_object" "folder_raw" {
  name   = "2024-03-31/raw/"
  bucket = google_storage_bucket.zoomcamp_bucket.name
  content = "placeholder"
  content_type = "application/x-directory"
}


