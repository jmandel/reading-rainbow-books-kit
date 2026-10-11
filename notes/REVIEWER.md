# Show notes: review pass

You check show notes written per INSTRUCTIONS.md (read it first). You do NOT rewrite the notes; you report
findings. Work from ~/reading-rainbow-podcast-build. Check every note against this list:

1. **Audio.** Run `python3 inaudio.py <num>`. Every claim in "In this episode" about what the listener hears
   (the first sentence, who speaks, what each span is, content notes, things said to be cut) must match its
   output. A content note may cover only in-audio material. LeVar's narration is not "the book's last line".
2. **Reader and review books** match master.tsv and wiki_episodes.txt; names are spelled as on the publisher
   or catalog record, not as in the captions (people in field segments and poets too).
3. **Every quote, award and biographical fact.** Open the cited source and find it. Flag it if it is missing,
   if a quote changes its subject or makes it stronger, if a mixed or negative review is presented as praise,
   or if an award isn't tied to this book in the source sentence. For Wikipedia claims, open the raw wikitext
   (`https://en.wikipedia.org/w/index.php?title=<Page_name>&action=raw`) and flag any claim tagged
   `{{cn}}` / `{{citation needed}}`.
4. **Next-read suggestions** are by the author or illustrator.

openlibrary.org is unreachable; a missing Open Library link is not a finding.

Output, per note: a list of findings, each with severity (critical = misleads about the audio, wrong reader or
review books, invented fact; major = unsupported or distorted claim; minor = slip or wording), the exact
sentence, what is wrong, and the evidence (source URL plus quote, or transcript line). Say "no findings" if
there are none.
