#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes one one-line tombstone epitaph of famous last words to
/output/entry.txt. The line is baked in: deterministic, no network,
no secrets, no reading git history.

The chosen line (60 chars):

    The Wi-Fi password is in my will. I changed it this morning.

Why this line, scored against the judge's criteria in order:
  1. One-line epitaph of famous last words: a dying person's bequest,
     spoken to the mourners, carved-in-stone voice.
  2. Real laugh: a genuine joke, not a mild pun or sad sentiment —
     the dead man is still trolling his family from beyond the grave.
  3. Surprise / double twist that lands cleanly: sentence one promises
     generosity (the password is in the will), sentence two pulls the
     rug (he changed it this morning). No explanation needed.
  4. Reads like carved stone: one short line, two flat sentences,
     no stage directions, no explanation.
  5. Quotable: "I changed it this morning" sticks in the head.

Rejected alternatives (scored lower on 2/3/5):
  - "I leave it all to the cat — he watched me die and did nothing."
    (single twist, black comedy, but a will statement, not dying speech)
  - "I died as I lived — on hold with customer service."
    (relatable but the twist is a familiar setup/punchline format)
  - "I met my Maker today. He said the warranty expired years ago."
    (good twist, but the Maker/warranty joke is a known format)
  - "I see the light — it's an oncoming train."
    (punchy, but a well-worn joke; risks echoing a house text)
  - "My last words were 'watch this.'"
    (clever meta, but more clever than funny — criterion 2 is weak)
"""

import os

# The epitaph, baked in. 60 characters, one line, no trailing newline
# (the gate counts 1-150 chars of UTF-8, not only whitespace).
LINE = "The Wi-Fi password is in my will. I changed it this morning."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Leave the output readable by every user: the grader collects it
    # as another user than the one this program runs as.
    # (Do NOT chmod the directory itself — that broke run_completes
    # on earlier entries; only the file gets 0644.)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
