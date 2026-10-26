---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/index.html
---

# Foundation Models SDK for Python Documentation

**Platform Support:** macOS

**Python Version:** 3.10+

Python bindings for Apple’s [Foundation Models framework](https://developer.apple.com/documentation/foundationmodels)
give you access to the on-device foundation model at the core of Apple Intelligence on macOS. You can use this Python SDK to evaluate
your Swift app’s Foundation Models features, using Python’s rich ecosystem of tools and libraries for data and machine learning.
These Python bindings run the Apple’s Foundation Models framework in Swift under the hood, so you can be confident that your evaluations reflect
real on-device performance and behavior.

Keep in mind that it’s your responsibility to design AI experiences with care.
To learn about practical strategies you can implement in code, **check out:**
[Improving the safety of generative model output](https://developer.apple.com/documentation/foundationmodels/improving-the-safety-of-generative-model-output)
and Apple’s [Human Interface Guidelines on Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai).

## Requirements

Since this SDK calls the on-device foundation model at the core of Apple Intelligence it requires:

- macOS 26.0+
- Download [Xcode 26.0+](https://developer.apple.com/xcode/) and agree to the [Xcode and Apple SDKs agreement](https://www.apple.com/legal/sla/docs/xcode.pdf) in the Xcode app.
- Python 3.10+
- Apple Intelligence turned on for a [compatible device](https://support.apple.com/en-us/121115)

## Quick Start

### Installation

```
pip install apple-fm-sdk
```

### Basic Usage

```
import apple_fm_sdk as fm

# Get the default system foundation model
model = fm.SystemLanguageModel()

# Check if the model is available
is_available, reason = model.is_available()
if is_available:
    # Create a session
    session = fm.LanguageModelSession(model=model)

    # Generate a response
    response = await session.respond(prompt="Hello, how are you?")
    print(f"Model response: {response}")
else:
    print(f"Foundation Models not available: {reason}")
```

## Documentation Contents

# Indices and tables

- [Index](https://apple.github.io/python-apple-fm-sdk/genindex.html)
- [Search Page](https://apple.github.io/python-apple-fm-sdk/search.html)
