#!/bin/bash
mkdir -p $(dirname $OUTPUT)

for i in {1..20000}
do
  url=$START=$i
  location=$( curl -i $url 2>/dev/null | grep -e location )
  echo $i $location >> $OUTPUT
done
