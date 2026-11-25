# agent-uh-oh

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/nmlyz/agent-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/nmlyz/agent-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

A tiny program that writes the one word an agent says when it has no
idea what to do. The word is `recalculating`: the voice of a navigator
that has lost the route and is working out a new one, out loud,
mid-task, instead of stopping to explain itself. One word, no
explanation attached, the same sound every lost machine makes.

## Run it

```sh
python3 main.py
```

It writes the word to `/output/entry.txt` (`MAKEFUN_OUTPUT_DIR`
overrides the directory). Running it twice produces byte-identical
output: exactly thirteen bytes, `recalculating`, with no trailing
newline.

Before writing, the program checks the word against the brief: one to
ninety-nine characters, exactly one word, letters only, no leading or
trailing white space. If any check fails it prints the problem and
exits without writing a file.
