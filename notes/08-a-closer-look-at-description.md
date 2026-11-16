# 08. A closer look at Description

Video: ~4 min

## Learning objectives
- Communicate your intentions to AI systems effectively
- Recognise the importance of clear, purposeful communication
- Build skill in the three types of Description: **Product, Process, Performance**

## What Description is
- Communicating with AI is **the core of most human-AI interaction**.
- Description goes **far beyond writing clever prompts**. It covers:
  - explaining tasks, asking questions, providing context, guiding the interaction
  - **steering a conversation that is going wrong**
  - **guiding the AI's thought process or reasoning**
  - building a **thinking environment** where both you and the AI can do your best work
- Metaphor: a **bridge between your intentions and the AI's capabilities**.
- Output quality often depends on how clearly you describe what you want. Analogy: asking someone to "make dinner" vs. giving a **detailed recipe with ingredients and instructions**.
- **AI cannot read your mind.** Do not assume it knows what you want; explain every relevant detail. **Do not make AI guess.**

## 1. Product Description: *what* you want
*The ability to clearly define what you want the AI to create or provide.*

Questions to cover:
- What is the **context** for this work?
- What exactly do you want the AI **to do**?
- What **format** should the output take?
- Who is the **audience**, and what **style** is appropriate?

Set **explicit requirements** and give the AI the information it needs.

## 2. Process Description: *how* the AI should approach it
*The ability to guide how the AI approaches your request.*

- Sometimes **how** the AI tackles a job matters **as much as or more than** the end goal (just as you might want a colleague to use your specific method).
- Three ways to give process guidance:
  - **general guidance**, like a manual
  - **step-by-step instructions**, like a cookbook
  - **demonstration through examples** ("here's how I'd do it")
- The AI already has extensive training; you add **context specific to your situation**. Ask:
  - Is there **specific data** it should draw on?
  - Are there **specific issues** to address, or a **particular order**?
  - A particular **style of analysis**, **workflow** or **technique** to use?

## 3. Performance Description: *how the AI should behave* with you
*The ability to define the behavioural aspects of an AI interaction.*

> "If you take one thing from this course, it should be this: AI tools are **not databases or vending machines**. They are **interactive systems that can behave differently in different contexts**, much like people."

Ask yourself first: **what kind of thinking partner do I need right now?**
- **Narrowing** toward a specific answer, or **exploring** multiple possibilities?
- Should the AI **challenge my assumptions** or **follow my lead**?
- **Expansive detail** or **concise**?
- **Explain why** it answers a certain way, or **just give the answer**?

### Diagram: the three kinds of description
```
 "make dinner"  ──────────────►  a full recipe
  (vague)                         (what + how + how to work with me)

                ┌──────────────────────────────────────────────────────────────────┐
 PRODUCT     ─► │ WHAT should come out?       output, format, audience, style      │
 PROCESS     ─► │ HOW should it work?         data, steps, order, method, examples │
 PERFORMANCE ─► │ HOW should it act with me?  concise/detailed, challenge/follow   │
                └──────────────────────────────────────────────────────────────────┘
```

## Summary
| Type | Question it answers | Examples |
|---|---|---|
| Product | What do I want? | output, format, audience, style |
| Process | How should the AI work on it? | data to use, steps, order, method, examples |
| Performance | How should the AI behave with me? | concise vs. detailed, challenging vs. supportive, explain vs. answer |

- Developing Description turns AI from a **generic assistant** into a **finely tuned thinking partner**.
- **Clear communication up front saves time** and gives better results.

## Exercise: Bad Prompt Makeover (10 min)
1. Ask Claude to **challenge you with poorly written prompts** to improve.
2. Improve each one using:
   - clear **product** description (what exactly you want)
   - **process** guidance (how Claude should approach it)
   - **performance** specs (how Claude should behave)
3. Discuss before/after with Claude and ask for feedback on how your version helps it respond better.
4. After ~5 min, **switch roles**: give Claude bad prompts to fix. Notice **what information Claude adds** and **how it organises it**.
