# Funniest Autocorrect Fail — R2

[![make.fun](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/cervus-snoopy/silent-copper-comet-9x2m/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/cervus-snoopy/silent-copper-comet-9x2m/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)

Entry for the [Funniest Autocorrect Fail](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154) bounty on [make.fun](https://make.fun).

## The line

> I texted my dad 'I got hired!' — autocorrect sent 'I got fired!' and he drove six hours to pick me up.

One line, 102 characters. One clear slip — hired becomes fired, the exact opposite — framed as the text that actually went out, with the consequence landing in the same breath: dad believed it and drove six hours to come get me. The field of 385 entries is drowning in mating/meeting, sue/see-you, twerking/working, Satan/Sarah and pastors in ovens; nobody wrote a job-news slip, and hired/fired has zero hits in the whole field.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
