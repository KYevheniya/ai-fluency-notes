# 04. Generative AI fundamentals (Deep Dive 1, part 1)

Video: ~6 min · Presenter: Drew Bent (Anthropic)

## Learning objectives
- Define generative AI and how it differs from other types of AI
- Recognise its key characteristics and technological foundations

## What generative AI is
- AI systems that **create new content** rather than just analysing existing data.
- Contrast:
  - **Traditional AI**: classifies an email as spam / not spam based on patterns. It **analyses and categorises**.
  - **Generative AI**: writes a completely new email for you. It **creates something that did not exist before**.
- This is described as a **fundamental shift in AI capabilities**.

## Large language models (LLMs)
- A prominent type of generative AI (e.g. Anthropic's Claude models).
- **"Language model"**: trained to predict and generate human language.
- **"Large"**: contains **billions of parameters**, the mathematical values that determine how the model processes information (loosely like synaptic connections in a brain).

## Three developments that made it possible
The path was not sudden; three things came together:
1. **Algorithmic and architectural breakthroughs.** Neural networks existed conceptually for decades, but the **transformer architecture (2017)** was a game changer. It excels at processing **sequences of text** while maintaining **relationships between words across long passages**, which is critical for understanding language in context.
2. **Explosion of digital data.** The raw material for training. Models like Claude learn from diverse sources such as **websites, code repositories and other text** representing human knowledge and communication, giving a broad and nuanced understanding of language and concepts.
3. **Massive increases in computing power.** Specialised hardware (**GPUs**, graphics processing units, and **TPUs**, tensor processing units) plus **distributed computing networks ("clusters")** enabled processing impossible a few years earlier.

## Scaling laws and emergent capabilities
- **Scaling laws**: empirical finding that as models get **larger**, train on **more data**, with **more compute**, performance **improves in predictable ways**.
- More surprising: **entirely new capabilities emerge** at larger scale that nobody explicitly programmed, e.g. reasoning through problems step by step, adapting to new tasks with minimal instruction.

### Diagram: from ingredients to answers
```
 INGREDIENTS   transformer (2017)  +  huge text data  +  GPU/TPU compute
                                   │
                                   ▼   bigger = predictably better (scaling laws)
 PRE-TRAINING  read billions of texts, keep predicting the next word
               result: a "map" of language and knowledge
                                   │
                                   ▼
 FINE-TUNING   learn to follow instructions; helpful, honest, harmless
               (human feedback + reinforcement learning)
                                   │
                                   ▼
 IN USE        your prompt ──► model continues the text ──► response
               (generates new text, does NOT look answers up in a database)
```

## How LLMs are trained
### Pre-training
- The model analyses patterns across **billions of text examples**. Analogy: reading every website and text you can find, not just to absorb information but to learn the **statistical relationships between words, phrases and concepts**.
- Result: something like a **complex map of language and knowledge**.
- Mechanism: show the model text and ask it to **predict what comes next**; over many iterations it refines its predictions and learns what makes language coherent and meaningful.

### Fine-tuning
- After pre-training, the model learns to **follow instructions**, give **helpful responses**, and **avoid harmful content**.
- Often involves **human feedback** plus **reinforcement learning** (rewards and penalties) to shape behaviour toward being **helpful, honest and harmless**.
- Then the model is **deployed** for people to use.

## What happens when you use it
- You provide a **prompt**: text the model reads and then **continues from**, based on patterns learned in training.
- The model is **not retrieving pre-written answers from a database**. It **generates new text** that statistically follows from what you wrote.

## The context window
- A practical limit on how much information the model can consider at once. Think of it as the AI's **working memory**.
- It includes **your prompts, the AI's responses, and anything else you have shared** in the conversation.
- Context windows keep growing (longer documents and conversations), but the limit means the model **does not have unlimited access to information** and **cannot use content outside its current context window** without specialised tools such as web search.

### Diagram: the context window
```
 CONTEXT WINDOW = the model's working memory for this conversation
 ┌──────────────────────────────────────────────────────────────┐
 │ prompt │ reply │ your file │ prompt │ reply │ prompt │ ...   │
 └──────────────────────────────────────────────────────────────┘
 outside the box = invisible to the model, unless a tool (e.g. web search) brings it in
```

## The three characteristics that make modern generative AI powerful
1. **Processing vast amounts of information during training**, so it learns complex, nuanced patterns in language and knowledge
2. **In-context learning**: adapts to new tasks from instructions or examples **in your prompt**, with no extra training
3. **Emergent capabilities from scale**: abilities not explicitly designed in, sometimes surprising even their creators

## Quick self-test
- Generative vs. traditional AI in one sentence each?
- What does "large" refer to in LLM?
- Name the three enabling developments. What year was the transformer introduced? (2017)
- Pre-training objective? (Predict the next text.) What does fine-tuning add?
- What sits inside the context window?
