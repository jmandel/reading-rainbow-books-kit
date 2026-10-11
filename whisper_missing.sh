#!/bin/bash
# usage: whisper_missing.sh queue.tsv — transcribe (GPU) every queued episode that has audio but no <id>.en.vtt;
# keeps looping while fetch_audio.sh/fetch.sh is still running so late downloads get picked up.
W="uv run -q --with faster-whisper --with av>=14,<16 --with nvidia-cublas-cu12 --with nvidia-cudnn-cu12>=9,<10 python whisper_vtt.py"
while :; do
  did=0
  while IFS=$'\t' read -r num season id kind title; do
    d="s$season"; a=$(ls -- "$d/$id".orig.* 2>/dev/null | grep -Ev '\.(part|vtt)$' | head -1)
    [ -n "$a" ] && [ ! -f "$d/$id.en.vtt" ] || continue
    echo "$num $id: transcribing $a"; $W "$a" "$d/$id.en.vtt" </dev/null && did=1
  done < "$1"
  [ $did = 1 ] && continue
  pgrep -f 'fetch(_audio)?\.sh ' >/dev/null || break; sleep 60
done
echo done
