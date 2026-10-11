# Reading Rainbow Books — personal podcast build kit

Turns classic *Reading Rainbow* episodes (LeVar Burton era, 1983–2006) into a private podcast feed of just the
book readings: each episode is LeVar's direct lead-in to the featured book plus the complete reading, with a
chapter marker at the title card so you can skip straight to the story.

**This repo contains no audio, video, transcripts or cover art** — only scripts and an episode spec
(`episodes.tsv`: YouTube video id + short caption phrases marking where to cut). You fetch the media yourself
for personal use; please don't publish the resulting feed.

## Files
- `episodes.tsv` — one row per episode: number, season, air date, book title, credit, YouTube id, cut segments
  (`start phrase|end phrase[|search end after N sec]`, joined by ` ;; `), and the title-card phrase used for the chapter.
- `master.tsv` — episode list parsed from Wikipedia (`parse_wiki.py`); `sources_all.tsv` / `match_sources.py` — how sources were picked.
- `fetch.sh` / `fetch_all.sh` — download original audio (YouTube Opus stream, no re-encode) + English captions into `s<season>/`.
- `show.py <vtt> [from_min] [to_min]` — timestamped transcript; `check.py <rows.tsv>` — dry-run of the cuts, showing
  the words around every cut point.
- `whisper_vtt.py` — local transcription (faster-whisper; GPU via pip CUDA libs, else CPU) for videos without captions.
- `build_all.sh <out_dir> <base_url>` — build every episode one at a time; `status.sh` — list episodes missing audio/captions.
- `build.py` — cuts each episode (single 192 kbps MP3 encode, loudness-normalized), embeds chapters and the book
  cover, and writes `feed.xml` (iTunes tags + Podlove Simple Chapters).
- `covers_auto.py`, `bingimg.mjs` — helpers for finding book covers (put them at `covers_final/<num>.jpg`).
- `rows/INSTRUCTIONS.md` — the rules used to pick cut points.

## Build
Needs python3 (+ Pillow), ffmpeg, [uv](https://docs.astral.sh/uv/) (runs the latest yt-dlp), a static file server
with HTTP range support (e.g. caddy).
1. `./fetch_all.sh` — re-run until nothing is missing (YouTube rate-limits). If a video has disappeared, find another
   upload of the episode, update its id in `episodes.tsv`, and re-check the phrases with `show.py` / `check.py`.
   Episode 137 (`ia-S18E02`) isn't on YouTube; copy its audio track from archive.org without re-encoding:
   `ffmpeg -i 'https://archive.org/download/ReadingRainbowTVSeries/Reading.Rainbow.S18E02.Pet.Stories.You.Dont.Have.to.Walk.480p.AMZN.WEB-DL.DD.2.0.x264-RTN.mkv' -map 0:a:0 -c copy s18/ia-S18E02.orig.mka`,
   then make its captions with `whisper_vtt.py`.
2. Add covers at `covers_final/<num>.jpg` (optional) and a podcast `cover.jpg` in the output folder.
3. `python3 -I build.py episodes.tsv . <out_dir> https://<your-host>/<path>/ [num ...]` (pass `0` to only rewrite feed.xml).
4. Serve `<out_dir>` somewhere only you can reach (or behind an unguessable path) and subscribe to `feed.xml`.
