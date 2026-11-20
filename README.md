# Parsha Who Am I?

A weekly Shabbos-table guessing game for children and families.

## Print

US Letter, actual size, double-sided, flip on the long edge. Each week is one sheet: 15 three-clue riddles on the front; silly mistakes, acting prompts and the parent answer key on the back.

| Shabbos | Parsha | Printable |
| --- | --- | --- |
| November 14, 2026 | Toldos | [PDF](weeks/2026-11-14-toldos/Toldos_Who_Am_I.pdf) |
| November 21, 2026 | Vayeitzei | [PDF](weeks/2026-11-21-vayeitzei/Vayeitzei_Who_Am_I.pdf) |

## Editorial approach

- Familiar answers, subtler clues: the challenge is connecting clues, not knowing obscure trivia.
- Clue 1 is indirect, clue 2 narrows the field, clue 3 makes a familiar answer attainable.
- Never state the answer in the final clue. Avoid first-letter hints by default.
- Easy uses short, concrete language for younger children. Medium and hard give older children more inference and detail.
- Read one clue at a time, pause, and let the child whose turn it is guess first.
- Keep Torah facts accurate. Identify Midrash/Rashi explicitly if adding material beyond the text.
- Keep prior printed editions unchanged; record feedback for subsequent weeks.

## Build

Requires Python 3, ReportLab, pypdf and DejaVu Sans fonts (Debian package fonts-dejavu-core).

```sh
python -m pip install -r requirements.txt
python scripts/build_vayeitzei.py
python scripts/build_toldos.py
```

Vayeitzei's editable questions and answers are in `weeks/2026-11-21-vayeitzei/content.json`.
Toldos retains the original builder and extracted JSON content for reference.
The PDFs in this public repository omit children's names and ages; the personalized print copies remain separate.

For a new week: verify the Shabbos date/parsha, create a dated folder, write the content, adapt the builder, render both pages, inspect for overflow and legibility, update this index and record family feedback.
