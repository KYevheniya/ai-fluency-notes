# 05. Capabilities & limitations (Deep Dive 1, part 2)

Video: ~7 min · Presenter: Drew Bent (Anthropic)

## Learning objective
- Identify the major capabilities and limitations of current generative AI (focus: LLMs such as Claude)

Framing: treat it like **getting to know a new colleague**. Knowing their strengths and limits helps you collaborate.

## Capabilities
1. **Versatility with language**
   - crafting emails that **capture your voice**
   - condensing long reports into clear summaries
   - translating between languages
   - explaining complex topics across fields (from microbiology to marketing strategy)
2. **Switching tasks without extra training**: the same system can write poetry, brainstorm a birthday party, explain quantum computing and analyse quarterly business trends, all through plain conversation.
3. **Maintaining the thread of a conversation**: it remembers what was said earlier and builds on it (e.g. you mention a project deadline in passing and refer back later; it understands, much like a human partner).
4. **Connecting to external tools and information**: many LLMs can search the web, process files, or use other applications, which greatly expands what they can help with.

## Limitations
1. **Knowledge cutoff date (bounded by training data)**
   - No innate knowledge of the world after the training cutoff. Example: a November 2024 cutoff means no training data after November 2024.
   - Analogy: someone who went on a retreat without internet on a given date does not know what happened after.
   - Needs tools such as **web search** for recent developments.
2. **Hallucinations**
   - Training does **not verify every fact** in the data, so models can learn and reproduce inaccuracies, and can make mistakes when piecing information together.
   - Hallucination = AI **confidently stating something plausible but incorrect**.
   - Unlike search engines, which **retrieve existing documents**, LLMs **generate** responses from statistical patterns.
   - Analogy: a friend telling a story with total confidence but the details completely wrong.
3. **Context window limits**
   - Every LLM has a maximum amount it can consider in one interaction.
   - When exceeded, information outside the window is lost, **usually first in, first out** (the oldest drops off).
   - Can limit processing of large documents or remembering a whole conversation.
4. **Non-determinism (unpredictability)**
   - Unlike traditional software (same input → same output), LLMs are **non-deterministic by default**: ask twice, get slightly different answers.
   - Cause: **probabilistic decisions** about what text comes next, plus settings developers can adjust.
   - Good for **brainstorming and diverse ideas**; needs awareness when **consistency or accuracy** is critical.
   - Some interfaces let you control randomness via a setting usually called **temperature**.
5. **Complex reasoning**
   - Historically weak on complex multi-step **mathematical or logical** problems.
   - Newer **reasoning / "extended thinking" models** that think step by step show strong progress.
6. **Lack of access to specific data or tools**
   - Even with tool use, a model may lack the data source or specialised tool a task needs.
   - Analogy: a brilliant colleague who **cannot access your company's internal database**; no matter how smart, their help is limited.
   - If the model does not have the data or tool, **do not be surprised it cannot answer**.

### Diagram: context window overflow and knowledge cutoff
```
 CONTEXT WINDOW FULL: oldest content falls out first (first in, first out)

   lost ◄── [ msg 1 ][ msg 2 ][ msg 3 ][ msg 4 ][ msg 5 ] ◄── new message
             └────────────── window size ─────────────┘

 KNOWLEDGE CUTOFF

   ──────── training data ────────┤ cutoff ├─────── the world keeps going ───►
          model knows this              model does not know this
                                        (needs web search or other tools)
```

## Where the field is heading
- Researchers are addressing limitations through:
  - **Retrieval-augmented generation (RAG)**: connecting models to external knowledge and data sources
  - expanding **tool use**
  - improving **reasoning**
- Some limitations will likely remain for the foreseeable future, though we do not know exactly which.

## Complementary strengths (the key message)
| Humans bring | AI brings |
|---|---|
| critical thinking | speed |
| judgment | scale |
| creativity | pattern recognition |
| ethical oversight | processing vast amounts of information |

- The most effective applications **combine these complementary strengths**.
- The balance **will shift as the technology evolves**, so continued learning and experimentation matter.
- Knowing what AI can and cannot do is essential to fluency and directly informs **Delegation**.

## Key takeaways (from the lesson page, covering lessons 4 and 5)
- Generative AI creates new content (text, images, code) rather than just analysing data
- Made possible by: architectural breakthroughs (transformer), vast training data, much more compute
- Two training stages: **pre-training** (patterns across billions of examples) and **fine-tuning** (following instructions, helpful responses)
- Capabilities: versatility, conversational awareness, connecting to external tools
- Limitations: knowledge cutoff, hallucinations, context window constraints, complex reasoning challenges
- Best results combine human and AI strengths, with humans providing critical thinking, judgment, creativity and ethical oversight
