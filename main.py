"""Fortune in a Pot.

Writes exactly one fortune for a houseplant, and prints the same
line, with the line written to entry.txt inside MAKEFUN_OUTPUT_DIR
(falling back to the current directory).

Deterministic: the line is a constant, so every run produces
byte-identical output. No network, no randomness, no secrets.
"""

import os
import sys

# The fortune, written for one particular plant on one particular
# windowsill rather than for plants in general:
#  - a prediction about the plant's own future ("Soon ... will ..."),
#    told through what it can see from the sill (the sunbeam, the
#    newest leaf) and the keeper passing by;
#  - the small joke is the keeper taking full credit for the plant's
#    moment in the sun in front of guests -- warm teasing a plant
#    lover recognises, never a pun and never mockery;
#  - 108 characters, well inside the 120-character gate, so it reads
#    cleanly aloud with nothing padded on to reach the limit.
FORTUNE = (
    "Soon a sunbeam will crown your newest leaf, and your keeper "
    "will take full credit for it in front of guests."
)

# The gate requires 1-120 characters of non-whitespace text.
assert 1 <= len(FORTUNE) <= 120, "fortune must fit the 120-char gate"


def main() -> int:
    # One encoded payload feeds both outputs, so stdout and the file
    # can never drift apart; newline="" keeps the line ending an LF
    # on every platform.
    payload = (FORTUNE + "\n").encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(payload)
    sys.stdout.buffer.write(payload)
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
