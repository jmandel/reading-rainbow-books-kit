#!/bin/bash
# usage: fetch.sh queue.tsv — download original audio (Opus 251, else AAC 140, never DRC) + English captions into s<season>/
Y='uvx --from yt-dlp[default]@latest yt-dlp'
while IFS=$'\t' read -r num season id kind title; do
  d="s$season"; mkdir -p "$d"
  ls -- "$d/$id".orig.* >/dev/null 2>&1 && [ -f "$d/$id.en.vtt" ] && continue
  for try in 1 2 3 4; do
    $Y -q --no-warnings -f "251/140/bestaudio[format_note!*=DRC]/bestaudio" --write-subs --write-auto-subs --sub-langs "en,en-orig" --sub-format vtt -o "$d/$id.orig.%(ext)s" -o "subtitle:$d/$id.%(ext)s" -- "$id" </dev/null 2>&1 | tail -1
    ls -- "$d/$id".orig.* 2>/dev/null | grep -qv part && break; sleep $((try*20))
  done
  echo "$num $d $id $(ls -- "$d/$id".orig.* 2>/dev/null | grep -v part | head -1 || echo FAIL) vtt:$([ -f "$d/$id.en.vtt" ] && echo y || echo n)"
  sleep 3
done < "$1"
