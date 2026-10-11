# Pilot show notes review (episodes 1, 89, 142)

Severity: **High** = a false statement a parent would notice or that misdescribes what they hear; **Medium** = an unsupported or misattributed fact; **Low** = filler, vague wording, structure.

## Episode 1, Tight Times

Errors found:
- **High: wrong reader.** The note says LeVar Burton reads the book. LeVar only gives the lead-in. The narrator is Patrick McCaffrey, according to the Wikipedia episode list and `master.tsv`, which the writer had. The transcript also shows a change of speaker (`- "Tight Times" by...`).
- **High: "Also recommended" said "the podcast reading names no other books"** and filled the section with the writer's own picks. The episode reviewed *When I Was Young in the Mountains* (Rylant/Goode), *Pet Show!* (Keats) and *The Terrible Thing That Happened at Our House* (Blaine/Wallner). The local `s1/` file is the official "STORY" clip (reading only). The full episode's captions (YouTube `c6ZJuNfZnNA`, listed in `fan.tsv`) and `wiki_episodes.txt` both have the review books.
- **High: "In this episode" invented content.** It said "the closing words about times that feel tight" come at the end of the reading. Those words are LeVar's wrap-up, which is cut. It also said there was "a field segment" without saying what it was. In fact the episode had a pet show (pet rocks, an imaginary hamster), LeVar and Hillary's free-fun song, and a library song.
- **Medium: unsupported claim.** "Many librarians have since praised it for handling a hard subject gently" is not in any cited source. I replaced it with the sourced Booklist and Bulletin quotes (from the encyclopedia.com entry, which the writer had cited but not used).
- **Medium: Hyman details.** "Cricket art director 1972 to 1979" is wrong; Wikipedia says 1973–1979, and the cited encyclopedia.com page only says "the 1970s". "More than 150 books" came from Wikipedia, which was not cited; the cited source says "well over one hundred".
- **Low:** "pencil art" (Kirkus says pencil, encyclopedia.com says pen and ink, so I dropped it). "this show does not spoil it" (meta filler). A duplicate source URL. A dead/403 library record cited. Next reads (*City Cats, Country Cats*, 1969) chosen with no source saying they are suitable.

What I changed: corrected the reader. Rewrote "In this episode" from the full-episode captions. Replaced "Also recommended" with the three real review books. Replaced the unsourced praise with sourced quotes. Fixed the Cricket years and cited Wikipedia. Removed the filler and the bad sources. Word count is 503.

## Episode 89, Through Moon and Stars and Night Skies

Errors found:
- **High: wrong order and wrong content in "In this episode".** It said the adoption families (Harris, Peek, Abney) appear before Andrew reads the book, which suggests they are in the podcast. They come *after* the reading and are cut. The podcast lead-in is the Prospect Park skate day with families talking about what bugs them and what they love. It also said "LeVar presents three books the kids reviewed"; in fact kids present them, and LeVar only reads the credits.
- **Medium: reader name taken from auto-captions.** "Andrew Lee" should be **Andrew Lei** (Wikipedia, `master.tsv`). The instructions warn about exactly this.
- **Medium: unsupported or misread bio facts.** "She began as a poet" is wrong; Wikipedia says she began teaching high school English. "In 1991 the NCSS gave her first prize for this book" is marked *citation needed* on Wikipedia, so I cut it. PW called Hale a "newcomer", not his "debut".
- **Low:** the note said "I could not find further biographical details" (first person, but fine to keep as a one-line "we could not find"). "The Keller and Hoberman books listed below also deal with family life" was filler in the wrong section. There was no Open Library link, although one exists (OL16055879W). The Hoberman illustrator (Marylin Hafner) is credited on air but was missing. A CCBC listserv post was cited for nothing that appears in the note.

What I changed: rewrote "In this episode" to separate the podcast audio from the cut TV material. Fixed the reader's name. Removed the unsourced award and the "poet" claim, and added the sourced detail about her mother illustrating *Vultures*. Added the Open Library link and the illustrator credit. Word count is 468.

## Episode 142, The Tin Forest

Errors found:
- **High: "Also recommended" said there were no review books.** There are three: *On That Day* (Andrea Patel), *Mole Music* (David McPhail) and *The Wonderful Happens* (Cynthia Rylant). Again the local file is the 9-minute "STORY" clip. Both `wiki_episodes.txt` and the full-episode captions (`lwzYmUCUcIw` in `kidzuko.tsv`, plus two others) have them.
- **High: wrong content warning about the podcast audio.** The note said the lead-in spends about 90 seconds on September 11 and told parents to listen first. In `episodes.tsv` the cut starts at "Here's a book that's all about the message of hope". The Ground Zero opening is not in the podcast; only a passing "right after the tragedy" remains. This would have scared parents away from a gentle episode for no reason.
- **Medium: episode numbering.** "Season 19, episode 142" should be season 19, episode 1 (142 overall).
- **Medium: padding and overreach on Anderson.** "He and Ward have worked together on several picture books": the source names two. The *Dream* anthology tidbit was trivia (he painted its cover). The National Art Library award was mentioned twice, for both people.
- **Low:** "lists Dutton as the publisher" and "LeVar Burton, the host of the original *Reading Rainbow*" were filler. The plot summary gave away the ending (birds bring seeds, a living forest grows), which goes against "don't spoil the ending". Wikipedia's main *Reading Rainbow* page was cited but not used.

What I changed: put the real review books in. Rewrote "In this episode" so it describes the actual lead-in and labels the PS 234 segment (gifts, the "Back Where We Belong" music video) as cut. Fixed the numbering. Cut the spoiler and the padding. Added Anderson's sourced Society of Illustrators medal for *Ratsmagic*. Word count is 485.

## Overall grade: C−

The prose is mostly plain and warm, the structure is followed, and most book and author facts were really in the cited pages. Wikipedia and publisher pages were used well for the basics. But every note had at least one **High** error in the sections a parent relies on most: who is reading, what they will hear, and which books were reviewed. All three failures have the same root cause: the writer treated the local VTT, which is sometimes only the reading clip, as the whole episode. It never checked `master.tsv`, `wiki_episodes.txt` or the segment phrases in `episodes.tsv`, all of which were in the folder. When it found nothing, it wrote confident statements ("names no other books", "LeVar reads") instead of saying it did not know. Each note also had one or two unsourced "color" claims (librarians' praise, the NCSS award, "began as a poet", "several books"). At about 150 episodes this pattern means roughly a third of all reader and review-book fields would be wrong.

## Proposed edits to INSTRUCTIONS.md

1. **Add a "Data you already have" section above "Rules":**
   > Before writing, look up the episode in all of these:
   > - `master.tsv`: the last column is the **reader/narrator**. Use this name, not the captions' spelling.
   > - `wiki_episodes.txt`: search the title. `Aux2` = narrator, `EpisodeNumber` = overall number, `EpisodeNumber2` = number within the season, `Review Books:` = the books the kids reviewed.
   > - `episodes.tsv`: the `segments` column gives the start and end phrases of what is **in the podcast audio**. Only text between those phrases is "in the podcast".
   > - `sources_all.tsv`, `fan.tsv`, `kidzuko.tsv`, `channel22.tsv`, `official.tsv`: other uploads of the same episode.

2. **Replace the "In this episode" guidance:**
   > The local VTT may be a reading-only "STORY" clip (check its length; under ~10 min means reading-only). If so, find a full-episode upload in the tsv files above and fetch only its captions into your scratch directory:
   > `uvx --from 'yt-dlp[default]@latest' yt-dlp --skip-download --write-auto-subs --sub-langs en -o 'subtitle:<scratch>/%(id)s.%(ext)s' -- <id>`
   > Describe (a) LeVar's lead-in as it appears between the start phrase and the title, (b) who reads it, and (c) the field segment(s) by their concrete content, labelled "not in the podcast audio". Never write "a field segment" without saying what it was. Never say who reads the book from the captions alone; use `master.tsv`.

3. **Replace the "Also recommended" guidance:**
   > List the books from `wiki_episodes.txt` "Review Books", confirmed against the full-episode captions (kids say "my book is..." / "it's called..." near the end; LeVar often reads the credits with authors). Look up each author on Open Library or the publisher. Never put your own recommendations in this section. If you truly cannot find the review books, write "Review books: not found" and mention it in your reply; do not say the episode had none.

4. **Add to "Rules":**
   > - A Wikipedia sentence marked *citation needed* does not count as a source.
   > - Quote a reviewer's actual word ("newcomer") rather than paraphrasing it into a stronger claim ("debut"). Don't turn "two books" into "several".
   > - Don't write claims about how a book was received ("librarians have praised...") unless a named source says so. Prefer short attributed quotes (Kirkus, Booklist, PW).
   > - Every source in the list must have supplied at least one fact in the note. Remove sources that 403'd or weren't used.
   > - No first person ("I could not find") and no comments about the note itself ("this show does not spoil it").
   > - Content warnings must describe what is **in the podcast audio** (between the segment phrases), not the full TV episode.

5. **Episode details:** state the format exactly: "Reading Rainbow season S, episode E (episode N overall)", with E from `EpisodeNumber2`.

6. **Spoilers:** make it concrete: "Describe the setup and the first turn only. Don't reveal how the problem is solved or what the last pages show."

7. **Add a final self-check list the writer must run before finishing:** the reader matches `master.tsv`; the review books match `wiki_episodes.txt`; every sentence in "In this episode" is labelled as podcast audio or as cut; every fact in the first two sections can be pointed to in a listed source; the word count (excluding Sources) is between 450 and 550.
