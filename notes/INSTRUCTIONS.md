# Show notes: how to write one

Audience: a parent playing a toddler podcast made from classic Reading Rainbow (LeVar Burton era).
Each podcast episode is only the host's lead-in plus the full book reading; the rest of the TV episode is cut.

Write `notes/<num>.md` (or the path you were given), 450–550 words not counting Sources. Warm, plain, specific.
No hype, no filler, no first person, no comments about the note itself.

## Data you already have (in ~/reading-rainbow-podcast-build)

Look the episode up in all of these before writing:
- `master.tsv`: num, season, air date, title, books, **reader/narrator** (last column). Use this reader name,
  never the captions' spelling.
- `wiki_episodes.txt`: search for the title. `EpisodeNumber` = overall number, `EpisodeNumber2` = number within
  the season, `Aux2` = narrator, `Review Books:` = the books the kids reviewed.
- **What is in the podcast audio:** run `python3 inaudio.py <num>`. It prints exactly the kept transcript text,
  with the cut words just before and after. inaudio.py is the only authority: whatever it prints is in the
  podcast (sometimes including an on-location opening), and everything outside it is not (often a cold open,
  LeVar's reflection after the book's last line, field segments, reviews).
- `sources_all.tsv`, `fan.tsv`, `kidzuko.tsv`, `channel22.tsv`, `official.tsv`: other uploads of the same episode.

## Transcripts

The local caption file is `s<season>/<youtube id>.en.vtt`. Print it with `python3 show.py <vtt>`.
It may cover only the reading (a "STORY" clip, under about 10 minutes). If so, find a full-episode upload in
the tsv files above and fetch only its captions into your scratch directory:

    uvx --from 'yt-dlp[default]@latest' yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs en \
        -o 'subtitle:<scratch>/%(id)s.%(ext)s' -- <id>

The lead-in is LeVar's unless the captions show a speaker change (`- ` or `>>`) before the title; celebrity readers
often read the title card themselves ("read by me, ..."). Name a speaker only when the captions or what is said
make it clear; never write who a line is not spoken by. Auto-captions misspell names (including poets,
contributors and people in field segments): verify spellings outside the captions or leave the name out; correct them from master.tsv, wiki_episodes.txt or web sources, or leave them out.

## Sections (use exactly these headings)

    ## About the book
    (130-170 words) The setup and the first turn, who it suits, what makes it stand out. Don't reveal how the
    problem is solved or what the last pages show. Short attributed reviewer quotes (Kirkus, Booklist,
    Publishers Weekly, School Library Journal, Horn Book) are welcome. If reviews are mixed, lead with the ones
    that match the book's strengths for young listeners and attribute any negative one plainly.

    ## Author and illustrator
    (130-170 words) Short bio for each, plus one or two memorable sourced tidbits: how the book came about,
    awards, other picture books a young listener might like next (by this author or illustrator only, never a
    book a reviewer compared it to). If you're short of material, search further (publisher pages,
    Encyclopedia.com/Gale, Wikipedia, Kirkus, PW) before writing less. If little is known, write what is
    known and stop. Never write about the search ("no biography turned up", "nothing more is claimed here").

    ## In this episode
    (90-150 words) (a) The lead-in, quoting or closely paraphrasing the first in-audio sentence from
    inaudio.py; the audio normally ends on the book's last line, so never describe remarks after it as in the
    podcast. (b) Who reads the book (from master.tsv). (c) The field segment(s) by their concrete content,
    labelled as not in the podcast audio. Never write "a field segment" without saying what it was.
    When inaudio.py prints more than one span, or the episode has no book reading, say what each span is: the
    featured book, another book read aloud (check the credits roll it prints), or LeVar's own narration.
    Never call LeVar's narration the book's last line.
    If the in-audio lead-in refers to cut material ("this neighborhood", "the tragedy"), say so in one
    sentence so the parent knows what the child hears without context.
    Add a one-line content note when the in-audio text includes job loss, crying, fear, separation, death or
    a disaster. Name only what is in the audio.

    ## Also recommended
    The review books from wiki_episodes.txt, confirmed against the full-episode captions, as bullets
    "*Title* by Author" (check authors on Open Library or the publisher). Never add your own picks.
    If you truly can't find them, write "Review books: not found" and say so in your reply.

    ## Episode details
    - Reading Rainbow season S, episode E (episode N overall)   (E from EpisodeNumber2)
    - Original air date: Month D, YYYY
    - Reader: name from master.tsv
    - Open Library: link to the featured book's work page, if you find the right one. openlibrary.org pages may
      show a human check; use https://openlibrary.org/search.json?q=<title>+<author>&fields=key,title,author_name,first_publish_year
      and link https://openlibrary.org<key>

    ## Sources
    Bulleted URLs that each supplied at least one fact in the note. If you used the episode transcript, list
    the YouTube upload (https://www.youtube.com/watch?v=<id>).

## Rules

- Every fact about the book and the people must come from a source you actually read. If you can't source
  it, leave it out. Never guess dates, awards or biographical details.
- Read Wikipedia through the raw wikitext (`https://en.wikipedia.org/w/index.php?title=<Page_name>&action=raw`).
  A sentence ending in `{{cn}}` or `{{citation needed}}` can't be used, not even as "According to Wikipedia".
- Don't call a review praise if it also judges the same thing negatively. Give the negative verdict plainly or
  leave that review out.
- Quote a reviewer's actual word ("newcomer") rather than turning it into a stronger claim ("debut").
  Don't turn "two books" into "several". Don't claim how a book was received unless a named source says so.
- A quote keeps its subject. If PW says the illustrations "endow this touching tale", the tale is touching, not
  the illustrations. An award claim must name this book in the same source sentence.
- For credited names prefer the publisher or Open Library record over captions and fan sites.
- Drop sources that failed to load or weren't used.
- The file starts with `## About the book`; no title line.
- Plain Markdown: headings, paragraphs, bullets, links, italics for titles. No emoji, tables or images.
- Write only your notes file. Don't touch anything else.

## Self-check before finishing

- The reader matches master.tsv.
- The review books match wiki_episodes.txt.
- Every sentence in "In this episode" is clearly either in the podcast audio or labelled as cut, and the
  first and last in-audio sentences match inaudio.py.
- Each quoted reviewer phrase was re-read in its source, with the same subject.
- Every fact in the first two sections can be pointed to in a listed source.
- `python3 lint_notes.py <your file>` prints nothing (section word counts, total 450-550, format).
