---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/generation_options.html
---

# Generation Options

This page documents the classes for controlling how the model generates responses.

Note

**Swift Equivalent:** This Python API corresponds to the [GenerationOptions](https://developer.apple.com/documentation/foundationmodels/generationoptions) structure in the Swift Foundation Models Framework.

## GenerationOptions

```python
class apple_fm_sdk.GenerationOptions
```

Bases: [object](https://docs.python.org/3/library/functions.html#object)

Options that control how the model generates its response to a prompt.

Generation options determine the decoding strategy the framework uses to adjust
the way the model chooses output tokens. When you interact with the model, it
converts your input to a token sequence and uses it to generate the response.

**Important Considerations:**

- Only use `maximum_response_tokens` when you need to protect against
unexpectedly verbose responses. Enforcing a strict token response limit can
lead to the model producing malformed results or grammatically incorrect
responses.
- All input to the model contributes tokens to the context window, including
the Instructions, Prompt, Tool definitions, and Generable types, as well as
the model’s responses. If your session exceeds the available context size,
it throws an ExceededContextWindowSizeError.

**Variables:**

- **sampling** (*Optional*[[SamplingMode](#apple_fm_sdk.SamplingMode)]) – A sampling strategy for how the model picks tokens when
generating a response. Defaults to None (uses model default).
- **temperature** (*Optional*[[float](https://docs.python.org/3/library/functions.html#float)]) – Temperature influences the confidence of the model’s response.
Higher values (e.g., 1.0) make output more random and creative, while lower
values (e.g., 0.1) make it more focused and deterministic. Valid range is
typically 0.0 to 1.0. Defaults to None (uses model default).
- **maximum_response_tokens** (*Optional*[[int](https://docs.python.org/3/library/functions.html#int)]) – The maximum number of tokens the model is allowed
to produce in its response. Use this to prevent unexpectedly verbose responses,
but be aware that strict limits may result in incomplete or malformed output.
Defaults to None (no explicit limit).

Examples

Default options:

```
import apple_fm_sdk as fm

options = fm.GenerationOptions()
```

Custom temperature and token limit:

```
import apple_fm_sdk as fm

options = fm.GenerationOptions(
    temperature=0.7,
    maximum_response_tokens=500
)
```

Greedy sampling with temperature:

```
import apple_fm_sdk as fm

options = fm.GenerationOptions(
    sampling=fm.SamplingMode.greedy(),
    temperature=0.3
)
```

Random sampling with constraints:

```
import apple_fm_sdk as fm

options = fm.GenerationOptions(
    sampling=fm.SamplingMode.random(top=50, seed=42),
    temperature=0.8,
    maximum_response_tokens=1000
)
```

See also

- [SamplingMode](#apple_fm_sdk.SamplingMode): For configuring sampling strategies
- [LanguageModelSession](session.md#apple_fm_sdk.LanguageModelSession): For using options in sessions

```python
sampling: SamplingMode | None = None
```

```python
temperature: float | None = None
```

```python
maximum_response_tokens: int | None = None
```

```python
__post_init__()
```

Validate generation options after initialization.

**Raises:**
: [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If any option values are invalid

## SamplingMode

```python
class apple_fm_sdk.SamplingModeType
```

Bases: [str](https://docs.python.org/3/library/stdtypes.html#str), [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Enumeration of available sampling mode types.

**Variables:**

- **GREEDY** – Always select the most likely token
- **RANDOM** – Randomly select from high-probability tokens

```python
class apple_fm_sdk.SamplingMode
```

Bases: [object](https://docs.python.org/3/library/functions.html#object)

A type that defines how values are sampled from a probability distribution.

This class represents different sampling strategies that control how the model
picks tokens when generating a response. The model builds its response in a loop,
and at each iteration it produces a probability distribution for all tokens in
its vocabulary. The sampling mode determines how to select the next token from
this distribution.

**Variables:**

- **mode_type** ([SamplingModeType](#apple_fm_sdk.SamplingModeType)) – The type of sampling mode
- **top** (*Optional*[[int](https://docs.python.org/3/library/functions.html#int)]) – For random sampling with fixed top-k, the number of high-probability
tokens to consider
- **probability_threshold** (*Optional*[[float](https://docs.python.org/3/library/functions.html#float)]) – For random sampling with variable threshold, the
cumulative probability threshold
- **seed** (*Optional*[[int](https://docs.python.org/3/library/functions.html#int)]) – Random seed for reproducible random sampling

```python
mode_type: SamplingModeType
```

```python
top: int | None = None
```

```python
probability_threshold: float | None = None
```

```python
seed: int | None = None
```

```python
classmethod greedy()
```

Create a sampling mode that always chooses the most likely token.

Greedy sampling provides deterministic, focused responses by always
selecting the token with the highest probability at each step.

**Returns:**
: A SamplingMode configured for greedy sampling

**Return type:**
: [SamplingMode](#apple_fm_sdk.SamplingMode)

Example:

```
import apple_fm_sdk as fm

sampling = fm.SamplingMode.greedy()
options = fm.GenerationOptions(sampling=sampling)
```

```python
classmethod random(top=None, probability_threshold=None, seed=None)
```

Create a random sampling mode with optional constraints.

Random sampling introduces variability in responses by randomly selecting
from high-probability tokens. You can constrain the selection using either:

- **top**: Consider only the top-k most likely tokens (fixed number)
- **probability_threshold**: Consider tokens until cumulative probability
reaches the threshold (variable number)

**Parameters:**

- **top** (*Optional*[[int](https://docs.python.org/3/library/functions.html#int)]) – Number of high-probability tokens to consider. If specified,
only the top-k most likely tokens are candidates for selection.
- **probability_threshold** (*Optional*[[float](https://docs.python.org/3/library/functions.html#float)]) – Cumulative probability threshold (0.0 to 1.0).
If specified, tokens are considered until their cumulative probability
reaches this threshold.
- **seed** (*Optional*[[int](https://docs.python.org/3/library/functions.html#int)]) – Random seed for reproducible sampling. Using the same seed
with the same inputs will produce the same outputs.

**Returns:**
: A SamplingMode configured for random sampling

**Return type:**
: [SamplingMode](#apple_fm_sdk.SamplingMode)

**Raises:**
: [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If both top and probability_threshold are specified,
or if values are out of valid ranges

Examples

Random sampling with top-k:

```
import apple_fm_sdk as fm

# Consider only top 50 most likely tokens
sampling = fm.SamplingMode.random(top=50, seed=42)
options = fm.GenerationOptions(sampling=sampling)
```

Random sampling with probability threshold:

```
import apple_fm_sdk as fm

# Consider tokens until 90% cumulative probability
sampling = fm.SamplingMode.random(
    probability_threshold=0.9,
    seed=42
)
options = fm.GenerationOptions(sampling=sampling)
```

Random sampling with seed only:

```
import apple_fm_sdk as fm

# Reproducible random sampling without constraints
sampling = fm.SamplingMode.random(seed=42)
options = fm.GenerationOptions(sampling=sampling)
```

Note

- Only one of `top` or `probability_threshold` can be specified
- If neither is specified, all tokens are considered
- The `seed` parameter enables reproducible generation
