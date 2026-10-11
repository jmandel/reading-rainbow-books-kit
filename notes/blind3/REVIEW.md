# Blind review: writers X and Y, episodes 1, 89, 142, 88, 28, 80

Method: each claim in "About the book" and "Author and illustrator" was checked against the URLs the note cites (raw Wikipedia wikitext for citation-needed tags). Each claim in "In this episode" was checked against `inaudio.py`, the local captions, and full-episode captions where the local file is only the story clip (ep 1: c6ZJuNfZnNA; ep 142: UL5XAkkMh4s). Reader and review books were checked against master.tsv and wiki_episodes.txt. Episode numbers, air dates and `lint_notes.py` were also checked. All 12 files pass lint, and every reader, review-book list, episode number and air date is correct.

## 1. Errors and usefulness

C = critical, M = major, m = minor. Usefulness is for a parent, 1 to 5.

| Ep | Writer | C | M | m | Use | Critical and major errors |
|---|---|---|---|---|---|---|
| 1 | X | 0 | 2 | 1 | 4 | M: "studied ... in Stockholm" rests on a Wikipedia sentence tagged `{{cn}}`. M: Kirkus distorted. Its "heavy overstatement" is about one drawing, not "the family's emotional moments", and the "one light note" is the naming alone, not the boy's happiness with the pet. |
| 1 | Y | 0 | 0 | 4 | 4 | (minor: says both parents answer "tight times", but only Daddy does; "Nancy Kincaid" should be Kincade; an editorial gloss after the Sutherland quote; cut segments slightly conflated) |
| 89 | X | 0 | 1 | 3 | 4 | M: NCSS 1991 first prize. The Wikipedia sentence is tagged `{{Cn}}`, and "According to Wikipedia" doesn't fix that. |
| 89 | Y | 0 | 2 | 3 | 3 | M: the same NCSS claim, stated as fact. M: lead-in speaker. The note quotes the opener and then says "several speakers, none of them LeVar" talk about families. LeVar is the host who opens and carries that montage ("Your family also makes you feel great"), and the note never credits him. |
| 142 | X | 0 | 1 | 3 | 5 | M: "Kirkus praised Wayne Anderson's detailed art" leaves out Kirkus's verdict that the book is "less developed both in art and storyline" than *Paper Bag Prince*. A mixed review is presented as praise. |
| 142 | Y | 0 | 1 | 3 | 3 | M: Kirkus misframed. Its "less developed both in art and storyline" is reported as a complaint about the story, and the note opens "Reviewers praise the art more than the text", which no source supports. PW praises the "touching tale" and its message. |
| 88 | X | 0 | 0 | 5 | 4 | (minor: "teaches" should be "taught" at Marist; the timeline of Petruccio's early commissions is compressed; the *Child's First Book* credit is loose; "learn the names of shells" is padding; "32 pages of color illustrations" isn't in its archive.org source) |
| 88 | Y | 0 | 1 | 4 | 3 | M: "It ends on the book's last line, 'The wind, the sun, and the sea.'" That is LeVar's own narration on the beach. The episode has no book reading, and it is the one episode where this matters. |
| 28 | X | 0 | 0 | 5 | 5 | (minor: says a child orders the ice cream, which the captions don't support; "speech balloons" goes beyond the sources; the "get it right" quote is generalized; an unsourced age fit; the YouTube upload isn't listed in Sources) |
| 28 | Y | 0 | 1 | 3 | 4 | M: says the in-audio "Whiskers died" passage is "one short group segment from Nurock's session". The book itself covers a pet's death (bookstores.com: "when a beloved pet dies"), and the kept span is the book's page. Also says flatly that the opening is "not with LeVar", which the captions don't show. |
| 80 | X | 0 | 1 | 4 | 4 | M: "the podcast contains three poems from it [the anthology]". The Frost poem is not in *Snowy Day* (archive.org table of contents). It is the third review book (the Susan Jeffers edition), introduced by a child reviewer, and the note also lists "three children's book reviews" as cut. |
| 80 | Y | 0 | 0 | 4 | 4 | (minor: Aileen Fisher and Eve Merriam aren't in the cited sources, though they are true per archive.org; *Handbook for Storytellers* is given as "ALA, 1995", which is the *New Handbook*; date conflicts; review-book credits are trimmed) |

Both writers spell the poet "Carla Kuskin" (a caption spelling; it should be Karla Kuskin). That counts as a minor error in both 80 notes.

Totals:

| Writer | Critical | Major | Minor | Mean usefulness |
|---|---|---|---|---|
| X | 0 | 5 | 21 | 4.3 |
| Y | 0 | 5 | 21 | 3.5 |

Instruction-specific checks:

| Check | X | Y |
|---|---|---|
| First in-audio sentence matches inaudio.py | 6/6 (28 paraphrases the opening scene and quotes LeVar's lead-in) | 6/6 |
| Lead-in speaker right | 6/6 | 4/6 (89 never credits LeVar and denies his part; 28 asserts "not LeVar" without evidence) |
| Content notes cover only in-audio material, and cover what's there | 6/6 | 6/6 (88's note is unnecessary but accurate) |
| Cut references explained | 142 "tragedy" explained in full; 28 explains "Blah"; 1 flags the pet-show context (harmless) | 142 explained |
| Quotes keep their subject | 1 (Kirkus) fails | 142 (Kirkus) fails |
| No citation-needed claims | fails 1 and 89 | fails 89 |
| Next reads by author or illustrator | 6/6 | 6/6 |

Why the usefulness scores differ: X's bios are fuller and better sourced (Y/142 has almost no biography of Ward or Anderson, only blurbs from a publisher page). X describes the cut segments concretely (the pet show, the PS 234 mural and song, the seine-net haul). X's content notes are more specific (job loss, a cat crying in a trash can, the dragon story). Y's audio sections contain the more parent-facing mistakes.

## 2. Failure patterns and fixes

1. **Claims that Wikipedia tags "citation needed" (X/1, X/89, Y/89).** Both writers missed the tag, because it is invisible in rendered or summarized page text. X tried to hedge it ("According to Wikipedia").
   - Fix: a **tool**. A script fetches `action=raw` for each cited Wikipedia page and lists the sentences tagged `{{cn}}`/`{{citation needed}}`, for the writer and the reviewer.
   - Also a **prompt change**: hedging doesn't make the claim usable.
2. **A reviewer's verdict narrowed or inverted (Kirkus in X/1, X/142, Y/142).** Writers quote the positive half of a mixed review, or move the negative onto a different subject.
   - Fix: a **review pass** that re-reads each review and compares the note's summary to the review's overall verdict.
   - Also a **prompt change**: when a review has a negative verdict, either state it plainly or don't characterize that review.
3. **Misreading what each part of the audio is (Y/88 "book's last line", X/80 Frost "from it", Y/28 Whiskers "from Nurock's session", Y/89 speaker).** This is the most parent-facing pattern. Multi-span and no-reading episodes are where it happens.
   - Fix: a **tool**. Extend `inaudio.py` to label each span (lead-in, reading of the featured book, another book read aloud, host narration) from episodes.tsv, and print the end-credits roll ("Today's Reading Rainbow books are ...").
   - Also a **prompt change** for multi-span and no-reading episodes.
   - A stronger model helps only partly. These are inference errors on garbled captions, and the evidence (the credits roll, the table of contents) is often outside what the writer looks at.
4. **Asserting a speaker the captions can't show (Y/28 "not with LeVar", X/28 "a child orders").**
   - Fix: a **prompt change**. Name a speaker only when the captions or the content make it clear, and never say who it is not.
5. **Caption spellings of names (Kuskin in both notes; Y/88's field guests "Lisa Satchel" and "Christy Seaman").**
   - Fix: a **prompt change**, extending the existing rule to poets, contributors and field-segment guests.
   - Also a **review pass**: list every proper name and check that it appears in a non-caption source.
6. **Small sourcing slips (dates, tense, compressions, facts true but not in the cited sources, audio used but not listed in Sources).**
   - Fix: a **review pass**. These are mechanical and low-stakes.

## 3. Ranking and recommendation

**Ranking: X first, Y second.** The error counts are the same, but X's majors are mostly about sourcing and reviews in the book sections. Y's include three misstatements about what the child actually hears (88, 28, 89), which is the core promise of the notes. X is also clearly more useful: richer bios, concrete cut-segment descriptions, sharper content notes.

**Writer:** use X's configuration for the roughly 150 episodes.

**A review pass is needed.** Neither writer reached zero major errors on six episodes. At 5 per 6 that is about 125 majors over 150 episodes. The review should check:
- **Wikipedia:** every Wikipedia-sourced sentence against the raw wikitext for `{{cn}}`, run as a script.
- **Quotes:** every quoted phrase is exact in its source and keeps its subject.
- **Reviews:** each reviewer's characterization matches that review's overall verdict.
- **In this episode:** every sentence matches inaudio.py, and in particular:
  - who speaks the lead-in;
  - what the last in-audio line is (the book, LeVar, or another book);
  - for multi-span episodes, which book each span comes from, checked against the credits roll.
- **Names:** every proper name taken from captions is verified or dropped.
- **Sourcing:** every fact in the first two sections appears in a listed source, and the YouTube upload is listed if the note used it.

**Could a cheaper reviewer catch these?**
- **Mostly mechanical errors:** probably yes, with tools. The citation-needed check should be a script, not a model. Exact-quote and "is this fact in the cited page" checks are lookups that a cheaper model handles well with a narrow checklist. They account for about half the majors and most minors here.
- **Review-verdict framing:** this needs judgment. A cheaper model would catch it only with an explicit instruction to compare the note to the review's final verdict. Test this on X/1 and X/142 before relying on it.
- **Audio structure (pattern 3):** a cheaper reviewer looking only at the note and inaudio.py would likely miss these, since each needed outside evidence (the credits roll, the anthology's contents, the book's own pet-death page). The fix is to give the facts to the reviewer through the `inaudio.py` labels and credits roll above, not to rely on model strength. With that tool, a cheaper reviewer becomes reasonable.
- **Suggested setup:** the X writer, then scripted checks (cn tags, lint, names), then a cheaper reviewer with the checklist. Have a stronger model spot-check the multi-span and no-reading episodes (an anthology, a nature guide, songs).

## 4. Remaining edits to INSTRUCTIONS.md

- **Rules:** "Read Wikipedia through the raw wikitext (`https://en.wikipedia.org/w/index.php?title=<page>&action=raw`). A sentence ending in `{{cn}}` or `{{citation needed}}` can't be used, even as 'According to Wikipedia'."
- **Rules:** "Don't call a review praise if it also judges the same thing negatively. Give the negative verdict plainly or leave that review out."
- **In this episode:**
  - "When inaudio.py prints more than one span, or the episode has no book reading, say what each span is: the featured book, another book read aloud (check the credits roll at the end of the captions, 'Today's Reading Rainbow books are ...'), or LeVar's own narration. Never call LeVar's narration the book's last line."
  - "Name a speaker only when the captions or what is said make it clear. Never write who a line is not spoken by."
- **Transcripts:** extend the name rule: "This includes poets, contributors and the people in field segments. Verify their spelling outside the captions or leave the name out."
- **Sources:** "If the note uses the episode transcript, list the YouTube upload."
- **Tool (not an instruction):** have `inaudio.py` label spans and print the credits roll, so writers and reviewers don't have to infer the episode's structure.
