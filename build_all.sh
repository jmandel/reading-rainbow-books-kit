#!/bin/bash
# usage: ./build_all.sh out_dir base_url — build every episode in episodes.tsv one at a time (one failure doesn't stop the rest),
# skipping episodes whose MP3 is newer than their spec row would require (i.e. already built), then write feed.xml.
cd "$(dirname "$0")"; out=$1; base=$2
for n in $(awk -F'\t' '!/^#/ && NF>=8 {print $1}' episodes.tsv); do
  python3 -I build.py episodes.tsv . "$out" "$base" $n 2>&1 | grep -v '^feed.xml' | sed 's/ <- .*//'
done
python3 -I build.py episodes.tsv . "$out" "$base" 0
