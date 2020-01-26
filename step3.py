import urllib.request
import gzip
import os.path
import sys
import pathlib


input_file = sys.argv[1]
output_dir = sys.argv[2]

pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

with open(input_file, "r") as sites:
    for line in sites:
        id, url = line.split(" ")
        filepath = f'{output_dir}/{id}.gz'
        if not os.path.exists(filepath):
            try:
                with urllib.request.urlopen(url) as page:
                    html = page.read()
                    compressed = gzip.compress(html)
                    with open(filepath, "wb+") as outfile:
                        outfile.write(compressed)
                        print(line)
            except urllib.error.HTTPError as err:
                print(f'{id} : Exeception {err}')
        else:
            print(f'skipping {id}')
