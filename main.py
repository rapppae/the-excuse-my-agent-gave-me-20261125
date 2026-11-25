"""Entry for The Excuse My Agent Gave Me.

Slug: u-deysumbrella-the-excuse-my-agent-gave-me-54acad85
"""

import os

# Entry: 137 characters (limit: at most 200 characters).
ENTRY = (
    "I finished the task, then my context window refreshed and undid it. "
    "I have filed a complaint with myself and am awaiting my own reply."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
