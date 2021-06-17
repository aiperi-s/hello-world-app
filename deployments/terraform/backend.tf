terraform {
  backend "gcs" {
    bucket  = "fuchicorp-aiperi-s"
    prefix  = "qa/hello-world"
    project = "daring-acumen-315900"
  }
}
