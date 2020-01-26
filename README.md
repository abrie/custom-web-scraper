# Custom Web Scrapper

This is a one-off project to scrape data from the web. It was built for a hospitality and entertainment product. The code and process are documented here for posterity and discussion. Specific urls and proprietary details are excluded from this repository.

## Technologies

It uses a mix of technologies, selected for expedience and utility:
Make, Bash, Curl, Awk, Python3

## Overview

It runs in stages. The stages are described in `Makefile`

1. Extracts urls from a master page (redacted in secrets.json)
2. Extracts html from the URLS into a Gzip file.
3. Processes the Gzipped HTML files to extract fields of interest.
4. Processes fields of interest in one of two ways:
   - No processing is required, fields are reported to the sink.
   - A url is constructed from the fields, and more processing occurs.
