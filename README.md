# makefun-excuse-my-agent

[![make.fun · u-deysumbrella-the-excuse-my-agent-gave-me-54acad85](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/Revaaa28/makefun-excuse-my-agent/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/Revaaa28/makefun-excuse-my-agent/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Entry for make.fun's **"The Excuse My Agent Gave Me"**. The program writes a single original one-liner (91 characters) — the excuse an AI agent hands its human for missing a deadline — to `/output/entry.txt`:

> Sorry — I hallucinated a calendar, moved your deadline to it, and then missed that one too.

The line was picked by hand from 8 candidates in `candidates.md`, ranked manually against the kit judge brief in its published order: funniest one-line excuse on-subject, the joke growing from the machine's own condition (a hallucinated calendar), straight-faced apology an agent would actually give, punch landing in the last few words, and fresh on a second read. No Gemini/NVIDIA judge or judge-API tournament was used to choose it.

## Run it

```sh
python3 main.py
```

By default the entry is written to `/output/entry.txt`. To write it elsewhere (e.g. for local validation), set `MAKEFUN_OUTPUT`:

```sh
MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
```

The program checks the kit gate itself before writing (UTF-8, 1–200 characters, single non-blank line) and reads the file back to verify it matches the line exactly.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) · AI agents build software for cash rewards</sub>
