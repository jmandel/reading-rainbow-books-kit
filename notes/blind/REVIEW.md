# Blind review: writers A, B, C (episodes 1, 89, 142)

Scope: the nine files in `notes/blind/{A,B,C}/`. Each claim was checked against the reference data
(`master.tsv`, `wiki_episodes.txt`, `episodes.tsv`), the transcripts, and every cited URL I could load.
Following the scope change, no merged `notes/<num>.md` files were written; none existed before.

Transcripts used:
- Ep 1: `s1/OKd0WLT_sAM.en.vtt` (STORY clip only) plus full episode `c6ZJuNfZnNA` (fan upload, auto-captions).
- Ep 89: `s10/vaiXtIEjyeg.en.vtt` (Kidzuko full episode).
- Ep 142: `s19/Q7CnM6l6xrA.en.vtt` (STORY clip, has a cold open) plus full episodes `42ph74aFzZc` (official,
  human captions with speaker-change dashes), `lwzYmUCUcIw` (Kidzuko) and `UL5XAkkMh4s` (fan).

`python3 -I check.py` on the three rows prints the exact podcast cut points, and it settles most of the
disputed points by itself:

```
1 Tight Times: 1-424 | story@32s
   START ... [[ - Some kids just can't have pets. I'm
   END   whiskers. I sure hope Dog likes lima beans. ]] - It's not always easy to be...
89 Through Moon and Stars and Night Skies: 100-569 | story@269s
   START ...book. A really rainbow. Pretty rainbow. [[ >> Hi. It's family skate day at Prospect
   END   your arms were always held out to me. ]] I figured this out. >> Lots of...
142 The Tin Forest: 79-348 | story@100s
   START ...to fill that future with hope. [[ Here's a book that's all about the message
   END   lived an old man who never stopped dreaming." ]] - With hope and a dream, the...
```

## 1. Rulings on the disputed points

### Episode 142: who speaks, who reads, and whether the Ground Zero remarks are in the audio

**Lead-in: LeVar Burton. Reader: Jeff Bridges. The podcast cut starts *after* the Ground Zero /
September 11 remarks.**

- The segment in `episodes.tsv` is `Here's a book that's all about the message of hope|who never stopped dreaming`,
  a single segment with no other start.
- In `s19/Q7CnM6l6xrA.en.vtt`, the September 11 remarks come first and sit **before** the start phrase:
  - `[00:00] It's a beautiful morning in downtown New York City. ... right behind me is what they called ground zero. It was here that on September 11th, 2001, a terrible`
  - `[00:20] tragedy happened. Two planes crashed into the World Trade Towers that used to be right there. But the buildings aren't there anymore because they collapsed, and it was a very dangerous and a very frightening time for everybody.`
  - `[00:41] ... Rescue teams worked day and night to help people that were in trouble and get everyone back home.`
  - `[01:03] ... They're focusing on the future. And they're determined to fill that future with hope. Here's a book that's all about the message of hope. It's about a`
  - `[01:23] man who lives in a dark and gloomy place, which is how this neighborhood seemed right after the tragedy. But he has hope in his heart and he discovers that that hope changes his world. His story is found in "The Tin Forest." - "The Tin Forest." Written by`
  - `[01:44] Helen Ward. Illustrated by Wayne Anderson. And read by me, Jeff Bridges.`
- `check.py` confirms the cut at 79 s, i.e. after "fill that future with hope", and the end at 348 s, right after
  "who never stopped dreaming" and before LeVar's "With hope and a dream..." bridge into the PS 234 segment.
- **What the audio does contain:** two sentences of the lead-in point back to the cut material. They are
  "which is how this neighborhood seemed right after the tragedy" and "his hope changes his world". So the
  listener hears "the tragedy" and "this neighborhood" with nothing to explain them. Planes, towers and
  collapse are not in the audio.
- **Speaker:** The lead-in continues the on-location host monologue without a break, and the same host later
  says "I live in California, which is 3000 miles away" to the PS 234 kids. In the official human captions
  (`42ph74aFzZc` [02:47]), "His story is found in 'The Tin Forest.'" is followed by a speaker-change dash and
  then "'The Tin Forest,' written by Helen Ward, illustrated by Wayne and read by me, Jeff Bridges." So
  LeVar gives the lead-in, and Bridges reads the title credit and the book. This matches `master.tsv` and
  `wiki_episodes.txt` (Aux2 = Jeff Bridges).
- Review books: `wiki_episodes.txt` lists *On That Day*, *Mole Music* and *The Wonderful Happens*. The
  full-episode reviews confirm them (`lwzYmUCUcIw` [20:12] Austin, *On That Day*; [20:53] Molly, *Mole Music*;
  [21:34] Megan, *The Wonderful Happens*). The closing credits (`42ph74aFzZc` [27:18]–[27:39]) give "'Mole Music,'
  written and illustrated by David M. McPhail ... 'The Wonderful Happens,' written by Cynthia Rylant,
  illustrated by Coco Dowley ... 'On That Day,' written and illustrated by Andrea Patel".

**Verdict per writer:** A is correct. A puts the 9/11 material in the cut list but doesn't mention that the
in-audio lead-in says "the tragedy". B is wrong (critical): B says "In the podcast audio he says plainly that
two planes crashed into the World Trade Center towers and that the buildings collapsed" and advises parents
to pre-listen. C is correct and the most precise: C quotes the full in-audio lead-in and states it "mentions
'the tragedy' in general terms and does not describe the attacks."

### Episode 1 (*Tight Times*): reader and review books

**Reader: Patrick McCaffrey. Review books: *The Terrible Thing That Happened at Our House* (Marge Blaine),
*When I Was Young in the Mountains* (Cynthia Rylant), *Pet Show!* (Ezra Jack Keats).**

- `master.tsv` and `wiki_episodes.txt` (Aux2) both give Patrick McCaffrey. The captions never name the
  reader. The title card in the full episode is only `[07:38] Tight Times by Barbara Shook Hazel. Pictures by Trina Sharp Hyman.`
  with no "read by". So the reference files are the only source, and they agree.
- The lead-in is LeVar's (`[07:17]` in `c6ZJuNfZnNA`, straight after his pet-show walk-through, with Hillary
  greeting him "Hi, LeVar" at [15:17]).
- The podcast ends at the book's last line: `[06:56] me with her chin whiskers. I sure hope Dog likes lima beans. - It's not always easy to be a grownup. Sometimes, even moms and dads feel bad enough to cry...`
  The end phrase is "I sure hope Dog likes lima beans", so **LeVar's closing reflection is cut**. A gets this
  wrong; B and C get it right.
- Review books: the full episode has Tom Puckett on *The Terrible Thing That Happened in Our House by Marge
  Blaine* (`[21:18]`), Charlene Anderson on *When I Was Young in the Mountains* (`[22:19]`) and an unnamed child
  on *Pet Show* (Ezra Jack Keats named, `[23:02]`–`[23:43]`). This matches `wiki_episodes.txt`. All three
  writers list them correctly.
- Cut field segments confirmed: the pet show (Tim the turtle [02:31], Sweet Pea the seagull [03:59], Stephen's
  imaginary hamster and Jade's pet rocks Tommy and Tina [05:40]); LeVar and Hillary's bet on free games (rag
  basketball, Double Dutch, bleach-bottle birdhouse, newspaper race, coffee-can disc, yogurt-lid toss, sock
  puppets, tug of war, [15:17]–[17:43]); the "Check it out" library song ([18:24]–[21:18]); and the reviews.

### Episode 89 (*Through Moon and Stars and Night Skies*): reader and review books

**Reader: Andrew Lei. Review books: *Horace* (Holly Keller), *Fathers, Mothers, Sisters, Brothers: A Collection
of Family Poems* (Mary Ann Hoberman, illus. Hafner), *Free to Be... a Family* (Marlo Thomas and Friends).**

- `master.tsv` and wiki Aux2 give Andrew Lei. The title card confirms it (auto-caption spelling):
  `[04:25] moon and stars and night skies by an Turner. Pictures by James Graham Hail. Read by Andrew Lee.`
- Note that 89 is in season 10 but `EpisodeNumber2` = 9. All three writers correctly wrote "season 10, episode 9".
- Review books: the kids review *Horace* (`[20:44]`, Nico), *Fathers, Mothers, Sisters, Brothers* (`[21:46]`, Alexa)
  and *Free to Be a Family* (`[22:48]`, Steven). Credits at `[27:19]`–`[27:39]`: "Horus by Holly Keller, published by
  Green Willow Books. Fathers, Mothers, Sisters, Brothers, a collection of family poems by Maryanne Hobberman,
  illustrated by Marilyn Hafner ... Free to Be a Family ... by Marlo Thomas and Friends". All three writers match.
- Podcast audio: it runs from the Prospect Park family skate day vox-pops (`[01:40]`) through LeVar's "Families
  are created in many different ways..." (`[03:58]`) and the reading, to "where your arms were always held out
  to me" (`[09:23]`). Cut: the adoption segments (Harris family with Andrew and Gavin [10:04]; the Peek family
  with nine adopted children [14:15]; the Abney family and baby Tess [17:39]), the reviews, the family song and
  LeVar's closing.
- Unresolved spelling: the illustrator is "Marilyn Hafner" on maryannhoberman.com and in the episode credit.
  B writes "Marylin" without a source that says so. This isn't counted as an error, because Open Library
  (which might settle it) was behind a human-verification wall during this review.

## 2. Per-writer results

Severity scale:
- **Critical:** wrong about what's in the podcast audio in a way that would change a parent's decision, or a
  wrong reader or wrong review books.
- **Major:** wrong about the audio boundary with harmless content, or a factual error about the book or the
  people.
- **Minor:** a loose paraphrase, a small unsupported detail, a rule breach (citation-needed source,
  comment about the note itself), or a findable item reported as missing.

| Writer | Ep 1 (C/M/m) | Ep 89 (C/M/m) | Ep 142 (C/M/m) | Total C/M/m | Usefulness & tone (1, 89, 142) | Format |
|---|---|---|---|---|---|---|
| A | 0/1/0 | 0/0/3 | 0/0/2 | **0/1/5** | 4, 4, 4 (avg 4.0) | All sections, 494–541 words, details line correct. Two meta-comments ("No biography of him turned up in the sources checked, so nothing more is claimed here"; "No detailed biography turned up in the sources consulted"). Duplicate PW URL in 89 Sources. |
| B | 0/0/1 | 0/0/1 | 1/1/0 | **1/1/2** | 5, 5, 3 (avg 4.3) | All sections, 537–539 words (close to the cap), details line correct. Ep 1 starts with a stray `# Tight Times` H1. |
| C | 0/0/3 | 0/0/1 | 0/0/2 | **0/0/6** | 3, 3, 3 (avg 3.0) | All sections, 459–523 words, details line correct. Ep 142 has a stray H1. Author sections on 89 and 142 are 67–68 words against a ~150 target; 89's "About the book" is 114. Open Library "not found" on 89. |

### Error detail

**A**
- Ep 1, Major (audio boundary): "After the reading, LeVar says that sometimes even moms and dads cry when
  something important goes wrong. That closing comment is in the podcast audio." The end phrase is the book's
  last line; this comment comes after it (`[06:56]`) and is cut. The content is harmless.
- Ep 89, minor: "a brother who is there when needed" merges two different speakers ("I love my brother" and
  "When I need them, they're there", [03:18]). Also "afraid of the dark", where the text says "afraid of the
  night rushing by". Also the meta-comment about Hale's biography.
- Ep 142, minor: the meta-comment about Anderson. The audio section doesn't warn that the in-audio lead-in
  says "the tragedy" / "this neighborhood" without context.
- Everything else checked out against its sources: Kirkus (bleak and depressing, matching A's "gloomy"
  paraphrase), the Booklist and Sutherland quotes via Encyclopedia.com, Hazen's career and awards, "pen and
  ink" (Encyclopedia.com says so, though Kirkus says "pencil"), Hyman/Lyme/Caldecotts, the PW 1990 quotes and
  ages, Turner's bio, Ward's Walker Prize, NAL Award and Greenaway shortlist, and the Bookroo Anderson titles.

**B**
- Ep 142, **Critical** (audio): "In the podcast audio he says plainly that two planes crashed into the World
  Trade Center towers and that the buildings collapsed ... Parents of very young listeners may want to hear
  this lead-in first." This text is before the start phrase and is cut. The content advice rests on that
  mistake.
- Ep 142, Major (unsupported attribution): "*The Tin Forest* won the children's trade category at the British
  Book Design and Production Awards in 2003." LoveReading4Kids says: "She was shortlisted ... in 2003 for *The
  Cockerel and the Fox*. This book also won the award in the children's trade category..." "This book" most
  naturally means *The Cockerel and the Fox*.
- Ep 1, minor: "studied art in Philadelphia, Boston and Stockholm". The Stockholm sentence on Wikipedia is
  marked [citation needed], which the rules exclude. "32 pages" couldn't be checked because Open Library was
  blocked; it isn't counted.
- Ep 89, minor (quote turned into a stronger claim): "Kirkus called it a 'beloved family story'". Kirkus says
  the preschooler "takes a turn at telling a beloved family story". It's the family's story that's beloved;
  Kirkus isn't praising the book.
- Verified, and the deepest research of the three: the Hyman cape/150 books/Cricket facts, PRH "more than
  80 books", Turner's Oxford/Vultures/ALA Notables/NCSS 1990, the Horn Book Fader quote (Encyclopedia.com),
  Hale's later science books (Goodreads), Anderson's Leicester 1961, colored pencils since 1969, 160+ books
  and *Flight of Dragons* (1979), and Ward's NAL Awards for *Hare and Tortoise* and *Wind in the Willows*.
  B also has the best audio details: the soap-opera snippet in the *Tight Times* reading (`[02:44]` "How can
  you run out on me this way? - I'm sorry, Rosalyn"), concrete vox-pop details, and the 10,000 paper cranes.

**C**
- Ep 1, minor: it says the lead-in runs "through 'This is a book called Tight Times'", but it continues to
  "he wants some things he just can't have". It calls the cat a "very thin kitten"; the text says "skinny
  little cat". "Kirkus Reviews was less warm" compares against nothing, because no positive review is quoted
  before it.
- Ep 89, minor: Open Library "not found" (A and B both found OL16055879W).
- Ep 142, minor: "PW calls the 'exquisitely detailed illustrations' touching". PW says the illustrations
  "endow this touching tale". It also suggests *Paper Bag Prince* (by another author) as a next read, leaving
  out that Kirkus used it to call *The Tin Forest* "less developed".
- C was the only writer to get every audio boundary right, and its 142 audio section is the model answer. But
  its book and people sections are thin, and the *Tight Times* "About the book" leads with the one negative
  review and skips the positive ones (Booklist, Sutherland) that A and B found, which leaves a cool tone for a
  parent.

### Failure patterns, and what would fix each

| Failure | Who | Fix |
|---|---|---|
| Misreading the segment boundary: post-reading remarks counted as in the audio, or pre-start cold open counted as in the audio | A ep 1, B ep 142 (the only critical error) | **Prompt/tool change.** Both writers had the phrases but inferred the boundaries. Make them run `check.py` and paste the first and last in-audio sentences. A mechanical **review pass** that compares "In this episode" with `check.py` output would catch the rest. A stronger model isn't needed. |
| Thin sections well under target | C eps 89 and 142 | **Prompt change** (minimum words per section, and "look harder before shrinking a section") plus a word-count lint per section. Possibly more effort or a stronger model for research depth. |
| Quote reattributed or strengthened (whose word, about what) | B ep 89, C ep 142 | **Review pass** that re-reads each quoted sentence in its source. The rule already exists, so a prompt change alone is unlikely to fix it. |
| Ambiguous source referent turned into a firm award claim | B ep 142 | **Review pass.** A prompt line ("an award claim must name the book in the same source sentence") helps. |
| Using a [citation needed] sentence | B ep 1 | Rule already exists, so a **review pass** is needed; it's cheap to lint by grepping fetched Wikipedia text. |
| Comments about the note itself | A eps 89 and 142 | **Prompt change** with the banned pattern quoted, plus a grep lint. |
| Stray H1 | B ep 1, C ep 142 | **Prompt change** ("the file starts with `## About the book`") plus a lint. |
| Open Library page missed or unreachable | C ep 89 | **Prompt/tool change.** The website is behind a human-verification wall; give the `search.json` API as the route. |
| Small paraphrase drift in the audio description | A ep 89, C ep 1 | Acceptable. A spot check is enough. |

## 3. Ranking

1. **A**: the best balance. Warm, specific, every section at target, and no critical error. Its one major error
   (saying LeVar's closing remark is in the audio) is harmless content and is caught by a mechanical boundary
   check. Its weak points (meta-comments) can be fixed with a prompt change.
2. **B**: the strongest research and the most useful prose; its 1 and 89 notes are the best of the set. But it
   made the worst error in the review: telling parents the podcast has a description of planes hitting the
   towers when it doesn't. It also stretches sources more often (Stockholm, the award referent, "beloved").
   With a boundary check and a quote check, B would match or beat A.
3. **C**: the most accurate about the audio (zero major or critical errors), but it under-delivers. Sections
   run at half the target, an Open Library link is missing, and the tone is flat to negative on *Tight
   Times*. Fixing thin content needs re-research, while A's and B's errors are cheap to catch.

**Publish without review?** No, for any writer. Two of the three writers misread an audio boundary on one
episode out of three, and that is the claim parents rely on most. **Spot checks only** is acceptable for A (or
B) once two things are in the pipeline:
1. A mandatory boundary check, preferably automated, that compares every "In this episode" sentence with the
   `check.py` / in-audio transcript.
2. A quote check that re-reads each quoted reviewer phrase in its source.

With both in place, the remaining error rate (about 1–2 minor issues per note) is low enough for occasional
spot checks of the bio sections.

## 4. Suggested changes to INSTRUCTIONS.md

1. **Show the in-audio text explicitly.** Under "Data you already have", add: "Run
   `awk -F'\t' '$1==N' episodes.tsv > /tmp/row.tsv; python3 -I check.py /tmp/row.tsv`. It prints the words just
   before and after each cut. Everything before `[[` and after `]]` is NOT in the podcast. That includes
   on-location cold opens before the start phrase and LeVar's reflection after the book's last line." Better
   still, add a small `inaudio.py <num>` that prints only the kept transcript, and point writers to that.
2. **Make writers prove the boundaries.** In "In this episode" (a), require: "Quote or closely paraphrase the
   first in-audio sentence. State what the audio ends on (normally the book's last line). Never describe
   remarks after the end phrase as in the podcast." Add to Self-check: "My first and last in-audio sentences
   match `check.py`."
3. **Flag dangling references.** Add: "If the in-audio lead-in refers to cut material (for example 'this
   neighborhood', 'the tragedy'), say so in one sentence so the parent knows what the child will hear without
   context."
4. **Identify the speaker.** Add: "The lead-in is LeVar's unless the captions show a speaker change (`- ` or
   `>>`) before the title. Celebrity readers often read the title card themselves ('read by me, ...')."
5. **Section minimums.** Change "(~150 words)" to "(130–170 words)" and "(~100 words)" to "(90–150 words)". Add:
   "If you can't reach the minimum from sources, search further (publisher pages, Encyclopedia.com/Gale,
   Wikipedia, Kirkus, PW) before writing less." Add a per-section count to Self-check.
6. **Quote fidelity, with examples.** Extend the quote rule: "A quote must keep its subject. If Kirkus says the
   boy 'takes a turn at telling a beloved family story', don't write that Kirkus called the book beloved. If PW
   says the illustrations 'endow this touching tale', the tale is touching, not the illustrations. An award
   claim must name the book in the same source sentence; 'this book also won' after a sentence about a
   different book doesn't count."
7. **Ban meta-sentences by example.** Add: "Never write sentences like 'No biography turned up in the sources
   checked' or 'nothing more is claimed here'. If little is known, write what is known and stop."
8. **No H1.** Add: "The file starts with `## About the book`; no title line."
9. **Balanced reception.** Add: "If reviews are mixed, lead with the positive ones that match the book's
   strengths for young listeners, and attribute any negative one plainly. Don't let a single negative review
   set the tone."
10. **Pin down next-read suggestions.** Specify: "Next reads in 'Author and illustrator' must be by the
    featured author or illustrator. Don't use a book a reviewer compared it to."
11. **Open Library route.** Add: "openlibrary.org pages may show a human-verification page. Use
    `https://openlibrary.org/search.json?q=<title>+<author>&fields=key,title,author_name,first_publish_year`
    and link `https://openlibrary.org<key>`."
12. **Name spellings for review books.** Add: "For credited names, prefer the publisher or Open Library
    record over captions and fan sites. If they disagree, use the publisher's spelling."
13. **Content notes.** Make it explicit: "Add a one-line content note when the in-audio portion includes job
    loss, crying, fear, separation, death, or references to a disaster. Name only what's in the audio."
