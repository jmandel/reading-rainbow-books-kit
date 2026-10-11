#!/bin/bash
# usage: ./status.sh — list episodes (episodes.tsv + queue/fixqueue leftovers) missing source audio or captions.
{ awk -F'\t' '!/^#/ && NF>=6 {print $1"\t"$2"\t"$6}' episodes.tsv; awk -F'\t' '{print $1"\t"$2"\t"$3}' queue.tsv fixqueue.tsv; } | sort -t$'\t' -k1,1n -u |
while IFS=$'\t' read -r n s id; do
  a=$(ls s$s/$id.orig.webm s$s/$id.orig.m4a 2>/dev/null | head -1); v=$([ -f s$s/$id.en.vtt ] && echo y || echo n)
  [ -z "$a" ] || [ $v = n ] && echo "$n s$s $id audio:${a:+y}${a:-n} vtt:$v"
done
