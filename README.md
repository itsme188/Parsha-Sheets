# Parsha Who Am I?

A weekly Shabbos-table guessing game for children and families.

## Print

US Letter, actual size, double-sided, flip on the long edge. Each week is one sheet: 15 three-clue riddles on the front; silly mistakes, acting prompts and the parent answer key on the back.

| Shabbos | Parsha | Printable |
| --- | --- | --- |
| November 14, 2026 | Toldos | [PDF](weeks/2026-11-14-toldos/Toldos_Who_Am_I.pdf) |
| November 21, 2026 | Vayeitzei | [PDF](weeks/2026-11-21-vayeitzei/Vayeitzei_Who_Am_I.pdf) |

## Editorial approach

Prepare every sheet in two separate passes. Do not begin by inventing riddles.

### Pass 1: What should children remember?

- Map the parsha's key storylines, messages, facts, people, places and important numbers.
- Make two age-level learning outlines: approximately ages 5-6 and ages 10-11. These are audience levels, not personal information about particular children.
- For the younger level, prioritize concrete events, central characters, sequence and accessible lessons. For the older level, add motivations, connections, consequences and meaningful details.
- Choose answers because they teach or recall something worthwhile. Cover the main storylines rather than repeatedly circling one scene.
- Record what each planned question reinforces and its Torah source. Distinguish the text from Rashi/Midrash and from an interpretive discussion.
- Keep familiar answers welcome. Getting most answers right is compatible with good learning and good play.

### Pass 2: Does this work as a game?

- Build the guessing game around the selected learning content, then read each riddle aloud as a player would hear it.
- Test clue 1 in the context of the named parsha: does it instantly identify the answer? If so, revise it unless it is a deliberate warm-up.
- Give opening clues several plausible possibilities without making them empty, arbitrary or misleading.
- Each later clue must add useful information. A clue that only repeats an earlier fact or exists to fill a slot should be rewritten.
- Preserve suspense and a satisfying deduction. Working default: clues become more revealing within a riddle; challenge can increase across rounds. The newest feedback asks for a stronger difficulty progression but does not unambiguously specify reversing the clue order.
- Never state the answer in the final clue. Avoid first-letter hints by default.
- Reject forced personification, unnatural phrasing, unsupported claims and obscure trivia used merely to make a question harder.
- Do not force every learning point into Who Am I. Use a short sequence, catch-the-mistake, acting or discussion prompt when it fits better.
- Check that the final clues support one fair answer, and accept reasonable equivalent answers.
- Review the whole game for variety, fun, competition and a fair chance for both age levels. Do not equate a high correct-answer rate with insufficient difficulty.

Read one clue at a time and pause. Let the child whose turn it is guess first. Easy uses short, concrete language; medium and hard add inference and detail. Keep prior printed editions unchanged and apply feedback to subsequent sheets.

Before rendering, retain a short content outline and a gameplay review alongside each new week's editable source.

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

For a new week: verify the Shabbos date/parsha, create a dated folder, complete the learning-content pass and gameplay pass, write the content, adapt the builder, render both pages, inspect for overflow and legibility, update this index and record family feedback.
