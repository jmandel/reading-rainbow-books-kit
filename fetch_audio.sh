#!/bin/bash
# usage: fetch_audio.sh queue.tsv — like fetch.sh but audio only (use when caption requests get 429s; transcribe with whisper_vtt.py)
Y='uvx --from yt-dlp[default]@latest yt-dlp'
while IFS=$'\t' read -r num season id kind title; do
  d="s$season"; mkdir -p "$d"
  aud() { ls -- "$d/$id".orig.* 2>/dev/null | grep -Ev '\.(part|vtt)$'; }  # leftover captions can be named <id>.orig.en.vtt
  aud | grep -q . && continue
  for try in 1 2 3 4; do
    $Y -q --no-warnings -f "251/140/bestaudio[format_note!*=DRC]/bestaudio" -o "$d/$id.orig.%(ext)s" -- "$id" </dev/null 2>&1 | tail -1
    aud | grep -q . && break; sleep $((try*20))
  done
  echo "$num $d $id $(aud | head -1 | grep . || echo FAIL) vtt:$([ -f "$d/$id.en.vtt" ] && echo y || echo n)"
  sleep 15
done < "$1"
