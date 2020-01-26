import os
import gzip
import re
import json
import sys
import pathlib

nameRegx = re.compile(r"'restaurantName': \"(.*?)\"")
topicsRegx = re.compile(r"'restaurantTopics': \"(.*?)\"")
phoneRegx = re.compile(r'id="restaurant-phone-\d+">(.*?)</a>')
addressRegx = re.compile(r'PostalAddress.*?mapa/">(.*?)<')
webRegx = re.compile(r'button-link track-restaurant-web" href="(.*?)"')

input_dir = sys.argv[1]
output_dir = sys.argv[2]

pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

for file in os.listdir(input_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".gz"):
        outfilename = os.path.join(output_dir, filename.split(".")[0])
        with open(outfilename, "wt+", encoding="utf-8") as outfile:
            with gzip.open(os.path.join(input_dir, filename), "rt", encoding="utf-8") as file:
                obj = {}
                html = str(file.read())
                obj['name'] = nameRegx.findall(html)
                obj['href'] = webRegx.findall(html)
                obj['tags'] = list(
                    map(lambda topics: topics.split(","), topicsRegx.findall(html)))
                obj['post'] = addressRegx.findall(html)
                obj['tels'] = list(
                    map(lambda tel: tel.replace("&nbsp;", ""), phoneRegx.findall(html)))
                outfile.write(json.dumps(obj, ensure_ascii=False))
