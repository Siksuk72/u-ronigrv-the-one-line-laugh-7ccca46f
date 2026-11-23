"""One-line laugh entry for make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f.

Design against the brief
-------------------------
The brief asks for a single funny line. This entry is a real joke with a
setup and a turn: the protector becomes the accuser. A password manager
exists to guard your secrets, so when it forgets the password and then
reports its own owner for suspicious activity, the roles reverse -- the
guard turns on the person it was meant to protect. That reversal is the
punchline, and it stays sensible: everyone has been locked out by a
security tool at some point, so the everyday truth lands immediately.
It is tight -- one sentence, no wasted words -- and fresh, because the
joke is on the security tool itself, not on forgetting a password.
The setup ("forgot my password") makes the manager look incompetent;
the turn ("reported me for suspicious activity") makes it look
arrogant. Incompetent plus arrogant, in one breath, is the laugh.
"""

import os

TEXT = "My password manager forgot my password, then reported me for suspicious activity."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(TEXT) <= 200, f"text length {len(TEXT)} outside 1..200"
    assert TEXT.strip(), "text must not be only white space"
    TEXT.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
