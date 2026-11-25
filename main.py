"""One-Sentence Absurd Invention Pitch: the discreet smoke alarm.

The tiny everyday annoyance here is one almost everyone has lived
through: you burn a piece of toast, and the smoke alarm answers with
a scream fit for a house fire. The machine cannot tell the difference
between breakfast going wrong and the building going up in flames, so
it treats both the same way, at full volume, at seven in the morning,
while you stand there waving a tea towel at the ceiling like that has
ever helped anyone.

The joke is built by giving the alarm the opposite personality to the
one it has now. Instead of a panicking town crier, this alarm is a
discreet accomplice. It still notices the smoke -- that is its job,
and the pitch keeps the job -- but it deals with it the quiet way:
it opens a window, lets the smoke out, and then, rather than sounding
the alarm, it whispers that the two of you will never speak of this
again. The laugh lands in that collision. A smoke alarm is the one
machine in the house whose entire purpose is to make a scene, and
here it is behaving like an embarrassed friend helping you hide a
minor disgrace from the neighbours.

That is also why the fix is clever rather than just silly. Opening a
window is a genuinely sensible response to burnt toast: it clears the
smoke, which is the actual problem, without the siren, which was never
the solution, only the announcement. The absurdity is not in the
mechanism -- windows do open, smoke does leave through them -- but in
the manners wrapped around it. The alarm treats a kitchen mishap as a
secret the two of you share, which is exactly the wrong job for a
safety device and exactly the right joke for a pitch about one.

The wording is kept tight on purpose, because the judge rewards a
single clean sentence that names the annoyance, the invention and its
silly mechanism without clutter. The opening names the machine and
its famous failure in one breath ("instead of screaming at burnt
toast"), the middle supplies the fix ("quietly opens a window"), and
the ending is the punchline in the alarm's own voice, a whispered
pact of silence. "Whispers" does the deadpan work: it is the sound of
a machine that is embarrassed on your behalf, and the quoted line
("we will never speak of this again") is the kind of thing people say
after a minor humiliation, which makes the alarm feel less like an
appliance and more like a co-conspirator. There is no second joke
bolted on at the end, no wink at the judge, and no extra clause
explaining the gag -- the sentence stands on its own as a pitch for
an invention that is ridiculous precisely because it is so polite.

The program itself is deliberately small: it holds the pitch, checks
that it satisfies the gate (one sentence, between 1 and 220
characters, not only white space), and writes it to /output/entry.txt.
"""

import os

# The pitch, in one sentence. The alarm's job is unchanged -- it still
# detects the smoke -- but its manners are the invention: instead of
# screaming about burnt toast, it quietly opens a window to clear the
# smoke and then treats the whole incident as a secret, whispering a
# pact of silence. The humour is the gap between what a smoke alarm
# is for (making a scene) and how this one behaves (covering one up),
# and the fix is silly yet weirdly plausible, because opening a window
# genuinely is what clears burnt-toast smoke.
PITCH = (
    "A smoke alarm that, instead of screaming at burnt toast, quietly "
    "opens a window and whispers 'we will never speak of this again.'"
)

# The gate the sealed scorer enforces: entry.txt must be UTF-8 text of
# 1 to 220 characters, not only white space. Keep the bounds here so a
# future edit that pushes the pitch over the cap fails loudly at home
# instead of silently on the server.
MIN_CHARS = 1
MAX_CHARS = 220


def validate(line):
    """Check one candidate pitch against the competition's gate.

    Returns the pitch unchanged when it passes, so the caller writes
    exactly what was checked. Raises ValueError with a plain reason
    when the pitch is empty, whitespace-only, split across lines, or
    longer than the 220-character cap.
    """
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(line))
        )
    return line


def main():
    line = validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    # Plain UTF-8, no trailing newline: the file holds exactly the
    # pitch the judge reads, byte for byte, nothing extra to trip
    # the gate.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
