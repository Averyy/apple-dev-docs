---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/errors.html
---

# Errors

This page documents the exception classes for error handling.

Note

**Swift Equivalent:** `GenerationError` cooresponds to the the [LanguageModelSession.GenerationError](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/generationerror)
in the Swift Foundation Models Framework. `ToolCallError` corresponds to the
[LanguageModelSession.ToolCallError](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/toolcallerror) in
the Swift Foundation Models Framework. `InvalidGenerationSchemaError` is unique to the Python SDK
and does not have a direct Swift equivalent since it means a schema failed to compile in the underlying Swift.

## Base Exceptions

### FoundationModelsError

```python
class apple_fm_sdk.FoundationModelsError
```

Bases: [Exception](https://docs.python.org/3/library/exceptions.html#Exception)

Base exception for Foundation Models errors.

Base exception for all Foundation Models SDK errors.

## Generation Errors

### GenerationError

```python
class apple_fm_sdk.GenerationError
```

Bases: [FoundationModelsError](#apple_fm_sdk.FoundationModelsError)

Base class for generation-specific errors.

Base class for errors that occur during text generation.

### ExceededContextWindowSizeError

```python
class apple_fm_sdk.ExceededContextWindowSizeError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when the context window size is exceeded.

Raised when the input exceeds the model’s context window size.

### AssetsUnavailableError

```python
class apple_fm_sdk.AssetsUnavailableError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when required assets are unavailable.

Raised when required model assets are not available.

### GuardrailViolationError

```python
class apple_fm_sdk.GuardrailViolationError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when a guardrail violation occurs.

Raised when content violates safety guardrails. For more on the guardrails, see the Swift
reference article on `SystemLanguageModel` safety meansures: [Improving the safety of generative model output](https://developer.apple.com/documentation/foundationmodels/improving-the-safety-of-generative-model-output).

### UnsupportedGuideError

```python
class apple_fm_sdk.UnsupportedGuideError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when an unsupported guide is used.

Raised when an unsupported guide constraint is used.

### UnsupportedLanguageOrLocaleError

```python
class apple_fm_sdk.UnsupportedLanguageOrLocaleError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when an unsupported language or locale is used.

Raised when the requested language or locale is not supported.

### DecodingFailureError

```python
class apple_fm_sdk.DecodingFailureError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when decoding fails.

Raised when decoding the model’s output fails.

### RateLimitedError

```python
class apple_fm_sdk.RateLimitedError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when rate limited.

Raised when rate limits are exceeded. Rate limits do not apply to the
on-device `SystemLanguageModel` on macOS so you should not encounter this error.

### ConcurrentRequestsError

```python
class apple_fm_sdk.ConcurrentRequestsError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when there are too many concurrent requests.

Raised when too many concurrent requests are made. The python SDK does
not enforce concurrency limits so you should not encounter this error.

### RefusalError

```python
class apple_fm_sdk.RefusalError
```

Bases: [GenerationError](#apple_fm_sdk.GenerationError)

Error thrown when the model refuses to generate content.

Raised when the model refuses to generate a response _specifically_ for
safety reasons on a generable output. For more on refusals, see the Swift
reference article on `SystemLanguageModel` safety meansures: [Improving the safety of generative model output](https://developer.apple.com/documentation/foundationmodels/improving-the-safety-of-generative-model-output).

**Attributes:**

- `reason` (str): The reason for refusal

## Schema Errors

### InvalidGenerationSchemaError

```python
class apple_fm_sdk.InvalidGenerationSchemaError
```

Bases: [FoundationModelsError](#apple_fm_sdk.FoundationModelsError)

Error thrown when a generation schema is invalid.

Raised when a generation schema is invalid. This means the schema failed
to compile in the underlying Swift code and most commonly occurs if you
give an invalid json schema to the `json_schema` parameter of the `respond()` method.
This error may also occur if you use the `@generable` decorator on a class with
properties that cannot be serialized to a json schema.

To validate if your json schema is valid, run the following code snippet in **Swift**:

```
import FoundationModels

jsonSchemaString = "..."  // Your JSON schema as a string

let schema = try JSONDecoder().decode(
  GenerationSchema.self,
  from: Data(jsonSchemaString.utf8)
)
```

The code above is the same validation step used in the Python SDK, so if it runs
without throwing an error, your schema is valid.

For examples of what valid json schemas look like, see the tester schemas in the Github repo,
such as `tests/tester_schemas/hedgehog.json`.

## Tool Errors

### ToolCallError

```python
class apple_fm_sdk.ToolCallError
```

Bases: [FoundationModelsError](#apple_fm_sdk.FoundationModelsError)

Error thrown when a tool call fails.

Raised when a `Tool` call fails.

**Attributes:**

- `tool_name` (str): Name of the tool that failed
- `underlying_error` (Exception): The original exception
