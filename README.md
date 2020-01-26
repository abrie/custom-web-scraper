# Custom Web Scraper

This is a one-off project to scrape data from the web. Built for a hospitality and entertainment product. Documented here for posterity and discussion. Specific urls and proprietary details are excluded from this repository.

## Technologies

It uses a mix of technologies, selected for expedience and utility:
Make, Bash, [cURL](https://curl.haxx.se/), [awk](https://www.gnu.org/software/gawk/manual/gawk.html), Python3, [jq](https://stedolan.github.io/jq/).

## Overview

The scraper runs in a series of stages. Each stage takes an input generates an output. Outputs are cached on the filesystem. The stages invoked through a `Makefile`

| Stage | Input      | Action                                                                                        | Ouput                                            |
| ----- | ---------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 1     | **secret** | [Bash scripts cURL to query a list of urls](step1.sh)                                         | A list indexed 'location' headers                |
| 2     | stage 1    | [Awk extracts url from location header](Makefile#L14)                                         | A list of indexed Urls                           |
| 3     | stage 2    | [Python iterates through list and caches url content](step3.py)                               | Directory of .gz files named by index value      |
| 4     | stage 3    | [Python iterates through cached .gz files and applies regex for fields of interest](step4.py) | Directory of JSON files named by index           |
| 5     | stage 4    | Bash and jq filter json files according to tuned selection criteria                           | A file with a list of indexes relevant to search |
