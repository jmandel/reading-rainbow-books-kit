# Picking book-segment boundaries for Reading Rainbow episodes

Working dir: ~/reading-rainbow-podcast-build. You get a batch file rows/batchN.in.tsv (one episode per line:
num, season, air date, title, Wikipedia "feature book" line, narrator, youtube id, source kind, source video title).
Captions are at s<season>/<youtube_id>.en.vtt. Do NOT download anything or edit any file except your own outputs.

## Goal
A toddler podcast: each episode = LeVar's DIRECT lead-in to the featured book + the complete book reading, nothing else.

## Rules
- START: the beginning of LeVar's passage that leads directly into the book. If LeVar's opening monologue/skit flows
  straight into the book's title card, start at the beginning of that monologue/skit (after the theme song). If there is
  an unrelated segment (documentary, interview, other topic) between the opening and the book, start at the last LeVar
  passage that sets up the book. Never include the theme song, funding credits, or "previously" material.
  Source kind "official-story" clips are already pre-cut around the story; they usually start right at LeVar's lead-in — still check.
- END: the last line of the book as read by the narrator. Exclude LeVar's reflection afterward, songs, poems, field
  segments, kids' book reviews, credits.
- If the book reading is interrupted by other segments and resumes later, list each book portion as its own segment in
  order (first segment starts with the lead-in). Only do this when the reading truly resumes later in the episode.
- CHAPTER: the phrase where the narrator reads the title card ("<Title> by <Author> ..."). It must fall inside the kept audio.
- Verify the video really is this episode and the feature book is actually read. If not (wrong video, no reading,
  captions unusable), do not invent a row — list it in your notes file with the reason.

## Phrase format
Phrases are matched word-by-word against the captions, ignoring case, punctuation and bracketed sound cues like [music]
or (upbeat music), and ignoring ">>". Copy words EXACTLY as the captions spell them (auto-captions mangle names — match
the captions, not the real spelling). Use 4–8 distinctive words. The end phrase is searched after the start phrase; if
it also occurs earlier inside the kept portion (refrains!), append |<seconds> to search only after that time.

Tools (run from ~/reading-rainbow-podcast-build):
- `python3 -I show.py s<season>/<id>.en.vtt [from_min] [to_min]` — timestamped transcript (~20s lines). Look at the whole
  episode at least through the end of the book (typically minute 0.8–14; book readings run 4–10 min).
- `python3 -I check.py rows/batchN.out.tsv` — dry-run: prints kept spans, story chapter time, and the words right
  around every cut ("START ...prev [[ kept" and "END kept ]] next..."). Every row must pass with no ERROR, and the
  context must show the cut is clean (start not mid-sentence of something else, end right after the book's last words).

## Output
rows/batchN.out.tsv — tab-separated, no header, one line per episode, 8 columns:
num, season, air_date, title, credit, youtube_id, segments, chapter_phrase
- title: the book/episode title, properly capitalized.
- credit: the credit text after the title in the feature-book line, e.g. "by Faith Ringgold" or
  "by Verna Aardema, pictures by Beatriz Vidal" (if missing, "by <author>" if you know it, else empty).
- segments: "start phrase|end phrase[|after_seconds]" ; multiple segments joined with " ;; ".
rows/batchN.notes.md — one line per episode: num, title, start→end (mm:ss), story chapter at, anything notable/uncertain;
plus the list of skipped episodes with reasons.

Example rows (Season 1):
4	1	1983-07-14	Bringing the Rain to Kapiti Plain	a Nandi tale retold by Verna Aardema, pictures by Beatriz Vidal	Hs3VwzUJvzM	a nice cool glass of apple juice|shadowed the ground on Capiti|725	A Nandi tale
9	1	1983-07-21	Three Days on a River in a Red Canoe	by Vera B. Williams	iPg3INochwA	Oh, hi. I'm about to leave|sand as scouring powder ;; After supper, we build|going up to join ;; Sam isn't much of a weather|Sam and I paddle, too ;; We canoe through a town|running over the rocks	Three days on a river in a red canoe by Vera
