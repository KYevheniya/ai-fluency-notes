# 09. Effective prompting techniques (Deep Dive 2)

Video: ~11 min · Examples use Claude, but apply to most AI systems

## Learning objectives
- Understand what prompt engineering is and why it matters
- Apply **six foundational prompting techniques**
- Identify patterns that lead to successful interactions
- Troubleshoot and refine prompts when responses miss

## What prompting is
- Not as technical as some guides make it seem. **Prompting is how we apply the Description competency in practice**: what we want, how we want it done, how we want to interact throughout.
- Analogy: explaining a task to a **helpful new colleague** who is eager but needs clear directions and expectations.
- **Prompt engineering** = the practice of designing effective instructions for AI systems: crafting questions and context so the AI understands exactly what you want.

### Same as human communication
- be clear · give relevant context · give concrete examples

### Different from human communication
- be **more explicit** about things a human would naturally infer
- accommodate the AI's **limited context window**
- sometimes (depending on the AI) use **specific formatting** that machines process easily

Best practices **change as models evolve**; what works today may differ tomorrow. **Experimentation is key.**

## The six foundational techniques

### 1. Give context
Be specific about **what** you want, **why** you want it, and (surprisingly important) **who you are**.

- Vague: *"Tell me about climate change."* Leaves Claude guessing about your interests, knowledge level, depth, geography, time span.
- Better: *"Explain three major impacts of climate change on agriculture in tropical regions, with examples from the past decade."*
- Best (adds why and how you will use it): *...plus: "I'm preparing for a job interview at an agricultural research lab in Indonesia. I have a degree in ecology but no specific knowledge of climate change. Write a summary of key concepts that would help me speak intelligently in the interview."*
- This is background we naturally give people but forget to give AI.

### Diagram: anatomy of the improved climate prompt
```
 ┌ WHAT ─── Explain three major impacts of climate change on agriculture
 │          in tropical regions, with examples from the past decade.
 ├ WHY ──── I'm preparing for a job interview at an agricultural research
 │          lab in Indonesia.
 ├ WHO ──── I have a degree in ecology but no specific knowledge of
 │          climate change.
 └ OUTPUT ─ Write a summary of key concepts that would help me speak
            intelligently in the interview.
```

### 2. Show examples (few-shot / n-shot prompting)
- "n" = number of examples. Really just **showing the AI examples to emulate**.
- Prompt: *"Please convert this technical statement to plain language: The platform implements end-to-end encryption protocols to safeguard data integrity."*
- **Try without examples first**; Claude may already do it well.
- If you need a specific style that is easier to show than explain:
  - *Original:* "The quantum algorithm exhibits quadratic speedup." → *Plain:* "The new method solves problems roughly twice as fast as previous methods."
  - *Original:* "The interface leverages intuitive design paradigms." → *Plain:* "The design is easy to understand and use."
  - "Now please convert this complex technical manual to plain language."
- **Cover the full diversity** of cases and styles in your examples so the AI understands the breadth of the pattern.

### 3. Specify output constraints
- Format, length, programming language, even the colour of buttons on a page.
- Example: *"Create a clean, modern, single-page art portfolio website. Include these main sections: hero, about me, skills, portfolio, projects, experience, and contact. Make the navigation menu sticky and responsive with a hamburger menu on mobile. Use a sunset colour palette and add a dark/light mode toggle in the navigation."*
- Helps the AI **structure its response** to match expectations.

### 4. Break complex tasks into steps (chain-of-thought prompting)
- Like asking a friend to do something without saying how: they may not do it your way.
- Instead of *"Analyse this quarterly sales data"*: *"I'd like to analyse this quarterly sales data. Please approach this by (1) looking through our sales records to identify the top-performing products, (2) comparing current quarter results to the previous quarter, (3) highlighting any unusual trends or patterns, and then (4) suggesting possible reasons for these trends."*
- Often **unnecessary for simple tasks**, and reasoning / extended-thinking models increasingly do step-by-step reasoning themselves, but you can still guide it.
- Rule of thumb: **the more variance in ways to do the task well, or the more it relies on your domain experience, the more you should translate that knowledge into the prompt.**

### 5. Ask the AI to think first
- Give the AI **space to work through its process before executing**, for more thorough, considered responses.
- Example addition: *"Before answering, please think through this problem carefully. Consider the different factors involved, potential constraints, and various approaches before recommending the best solution."*
- Reasoning / extended-thinking models do this by default; for others you can prompt it.
- **Thinking must come *before* the answer, not after.** Explaining after the fact does not improve quality, just like acting first and justifying later is different from thinking before acting.
- Side benefit: you can **see where the AI goes astray**, which shows where to add more guidance.

### Diagram: why thinking must come first
```
 ✔  think ──► answer       the thinking shapes and improves the answer
 ✘  answer ──► explain     explaining afterwards does not improve it
```

### 6. Define the AI's role, style or tone
- Specifying **expertise level, perspective, communication style** changes both the interaction and the final result. In short: **who do you want the AI to act as?**
- *"Please explain how rainbows form from the perspective of an experienced science teacher speaking to a bright 10-year-old who's interested in science."*
- Good for brainstorming and feedback. Can be a general role or a **specific figure's persona** (e.g. Richard Feynman for physics explanations).
- *"As a UX design expert, review this website wireframe and suggest three improvements focusing on user navigation and accessibility."*

## The "secret weapon": ask the AI to improve your prompt
- Perhaps the most powerful technique. Describe your situation and ask Claude to improve or write the prompt:
  - *"I'm trying to get you, Claude, to help me with [goal]. I'm not sure how to phrase my request to get the best results. Can you help me craft an effective prompt for this?"*
- This is where AI assistants **vary most** in performance, so experiment with models (part of **Platform Awareness** in Delegation).

## Iterating and troubleshooting
Prompting is **iterative and experimental**; the first attempt will not always be perfect, and that is expected. When a response misses:
- add **more specificity or context**
- provide **examples** of desired output
- **break the task** into smaller steps
- try a **different technique or combination**
- ask for **variations**: *"Can you give me three different versions of this?"*
- request **different formats**: *"Instead of a paragraph, could you present this in an interactive artifact?"* (Artifacts are Claude outputs that can be easier to understand or more engaging.)
- **check confidence** on factual questions: *"How confident are you about this answer?"*
- **reset the conversation**: a fresh start sometimes beats correcting a conversation that has gone off track

Use each interaction as feedback for the next prompt; over time you build intuition.

### Diagram: the iteration loop
```
 prompt ──► response ──► good enough? ── yes ──► done
   ▲                          │ no
   │                          ▼
   └──── adjust: more context · examples · smaller steps · other technique
                · "give me 3 versions" · different format · "how confident are you?"
                · or start a fresh conversation
```

## Patterns that work
- a clear **task overview** statement up front
- **format specifications** and **examples**
- **explicit constraints** or requirements
- **rich, relevant background** information

## Common mistakes
- assuming Claude **can read your mind**
- **overloading** one prompt or conversation with multiple **unrelated tasks**
- being **too vague about what success looks like**
- **not giving feedback** on previous responses

## Recap
- Effective prompting = **timeless human communication principles + AI-specific techniques**.
- Six techniques + the secret weapon = a toolkit for applying **Description**.
- **Iteration and practice** are the key to fast improvement.
- Prompt engineering evolves: as models improve **some specific techniques become less necessary**, but the **principles of good communication stay relevant**.
