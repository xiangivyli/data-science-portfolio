terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.26.0"
    }
  }
}

provider "google" {
  credentials = var.credentials
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "zoomcamp_bucket" {
  name          = var.gcs_bucket_name
  location      = var.location

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
  name   = "final_project/2024-03-31/"
  bucket = google_storage_bucket.zoomcamp_bucket.name
  content = "placeholder"
  content_type = "application/x-directory"
}

resource "google_storage_bucket_object" "folder_parquet" {
  name   = "final_project/2024-03-31/parquet/"
  bucket = google_storage_bucket.zoomcamp_bucket.name
  content = "placeholder"
  content_type = "application/x-directory"
}

resource "google_storage_bucket_object" "folder_raw" {
  name   = "final_project/2024-03-31/raw/"
  bucket = google_storage_bucket.zoomcamp_bucket.name
  content = "placeholder"
  content_type = "application/x-directory"
}




