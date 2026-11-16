# AI Fluency: Framework & Foundations, study notes

Source: Anthropic Academy course on Skilljar (13 lessons, 11 videos, about 1.1 h of video).
Course content © 2025 Rick Dakan, Joseph Feller and Anthropic, CC BY-NC-SA 4.0. These notes are for personal study.

## Contents
| # | Lesson | Notes | Full transcript |
|---|---|---|---|
| 01 | Introduction to AI Fluency | [notes](notes/01-introduction-to-ai-fluency.md) | [transcript](transcripts/01-introduction-to-ai-fluency.md) |
| 02 | Why do we need AI Fluency? | [notes](notes/02-why-do-we-need-ai-fluency.md) | [transcript](transcripts/02-why-do-we-need-ai-fluency.md) |
| 03 | The 4D Framework | [notes](notes/03-the-4d-framework.md) | [transcript](transcripts/03-the-4d-framework.md) |
| 04 | Generative AI fundamentals | [notes](notes/04-generative-ai-fundamentals.md) | [transcript](transcripts/04-generative-ai-fundamentals.md) |
| 05 | Capabilities & limitations | [notes](notes/05-capabilities-limitations.md) | [transcript](transcripts/05-capabilities-limitations.md) |
| 06 | A closer look at Delegation | [notes](notes/06-a-closer-look-at-delegation.md) | [transcript](transcripts/06-a-closer-look-at-delegation.md) |
| 07 | Project planning and Delegation (exercise) | [notes](notes/07-project-planning-and-delegation.md) | [page text](transcripts/07-project-planning-and-delegation.md) |
| 08 | A closer look at Description | [notes](notes/08-a-closer-look-at-description.md) | [transcript](transcripts/08-a-closer-look-at-description.md) |
| 09 | Effective prompting techniques | [notes](notes/09-effective-prompting-techniques.md) | [transcript](transcripts/09-effective-prompting-techniques.md) |
| 10 | A closer look at Discernment | [notes](notes/10-a-closer-look-at-discernment.md) | [transcript](transcripts/10-a-closer-look-at-discernment.md) |
| 11 | The Description-Discernment loop (exercise) | [notes](notes/11-the-description-discernment-loop.md) | [page text](transcripts/11-the-description-discernment-loop.md) |
| 12 | A closer look at Diligence | [notes](notes/12-a-closer-look-at-diligence.md) | [transcript](transcripts/12-a-closer-look-at-diligence.md) |
| 13 | Conclusion | [notes](notes/13-conclusion.md) | [transcript](transcripts/13-conclusion.md) |

All notes in one file: [ALL-NOTES.md](ALL-NOTES.md)

## One-page cheat sheet
**AI Fluency** = engaging with AI in ways that are **effective, efficient, ethical and safe**.

**Three modes:** Automation (AI does a defined task) · Augmentation (AI as thinking partner) · Agency (you set AI's knowledge and behaviour, it acts on your behalf; "director, not scriptwriter").

| D | Question | Components | Serves |
|---|---|---|---|
| Delegation | What should I do, what should AI do? | Problem awareness · Platform awareness · Task delegation | effective, efficient |
| Description | How do I communicate clearly? | Product · Process · Performance | effective, efficient |
| Discernment | Is what I got any good? | Product · Process · Performance | effective, efficient |
| Diligence | Am I responsible, transparent, accountable? | Creation · Transparency · Deployment | ethical, safe |

**Six prompting techniques:** give context (what, why, who you are) · show examples (few-shot) · specify constraints · break into steps (chain of thought) · ask it to think first · define role/tone. **Secret weapon:** ask the AI to improve your prompt.

**LLM limits:** knowledge cutoff · hallucinations · context window (first in, first out) · non-deterministic (temperature) · complex reasoning · no access to your data/tools.

**Key lines:** "Experts in their fields first, AI delegators second." · "AI tools are not databases or vending machines." · Thinking must come before the answer, not after. · When discernment flags a problem, better description is often the fix, sometimes better delegation. · You, not the AI, are responsible for what you share.

## How to re-run the capture
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python fetch_transcripts.py
```
`lessons.json` holds each lesson's title, URL, YouTube video ID and the lesson page text (captured from Skilljar while signed in). The script pulls YouTube captions and rewrites `transcripts/`. For another course, rebuild `lessons.json` from that course's lesson pages first.
