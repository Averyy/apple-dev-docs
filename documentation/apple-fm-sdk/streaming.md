---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/streaming.html
---

# Streaming Responses

Note

**Swift Equivalent:** This guide covers concepts that correspond to streaming responses in the [LanguageModelSession](https://developer.apple.com/documentation/foundationmodels/languagemodelsession) class in the Swift Foundation Models Framework.

Streaming lets you receive model responses in real-time as the model generates them, rather than waiting for the complete response. This creates responsive interfaces.

## Why Use Streaming?

- **Better experience**: You see output immediately
- **Perceived performance**: Applications feel faster and more responsive
- **Progressive Display**: Show partial results as they’re generated

## Basic Streaming

In the code below, session.stream_response returns an async iterator that yields text chunks:

```
import apple_fm_sdk as fm

model = fm.SystemLanguageModel()
is_available, _ = model.is_available()

if is_available:
    session = fm.LanguageModelSession()

    async for chunk in session.stream_response("Tell me a short story"):
        print(chunk, end="", flush=True)
```

## Streaming with Context

Like regular responses, streaming maintains session context:

```
import apple_fm_sdk as fm

session = fm.LanguageModelSession()

# First streaming response
async for chunk in session.stream_response(
    "What are some differences between Swift and Python?"
):
    print(chunk, end="", flush=True)
print("\n")

# Follow-up with context maintained
async for chunk in session.stream_response("Show me an example"):
    print(chunk, end="", flush=True)
```
