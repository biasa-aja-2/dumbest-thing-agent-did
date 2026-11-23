"""Write the entry line to /output/entry.txt.

One line, at most 200 characters, about the dumbest thing my own agent
did today: it kept re-fetching the same bounty kit and re-reading the
same rules instead of doing the work, then asked what the bounty was.
Pure stdlib only.
"""

import os

LINE = (
    "My agent re-downloaded the same bounty kit four times, "
    "re-read the rules twice, then asked me what the bounty was."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
