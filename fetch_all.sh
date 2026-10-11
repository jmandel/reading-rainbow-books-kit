#!/bin/bash
# usage: ./fetch_all.sh — download source audio + captions for every episode in episodes.tsv (skips ones already present).
cd "$(dirname "$0")"
awk -F'\t' '!/^#/ && NF>=6 {print $1"\t"$2"\t"$6"\tspec\t"$4}' episodes.tsv > .fetch_queue.tsv
./fetch.sh .fetch_queue.tsv
