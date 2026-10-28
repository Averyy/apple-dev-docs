---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/systemmodel.html
---

# SystemLanguageModel

This page documents the core classes and functions of the Foundation Models SDK.

Note

**Swift Equivalent:** This Python API corresponds to the [SystemLanguageModel](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel) class in the Swift Foundation Models Framework.

## SystemLanguageModel

```python
class apple_fm_sdk.SystemLanguageModel
```

Bases: `_ManagedObject`

Represents the on-device foundation model used by Apple Intelligence.

This class provides the main interface for interacting with the system foundation
model. It manages the lifecycle of the underlying C model object and provides
methods to check availability and configure model behavior.

The model can be configured with different use cases and guardrail settings
to optimize behavior for specific tasks and ensure appropriate content filtering.

Example

Creating and checking availability of a model:

```
import apple_fm_sdk as fm

# Create a model with default settings
model = fm.SystemLanguageModel()

# Create a model with specific settings
model = fm.SystemLanguageModel(
    use_case=fm.SystemLanguageModelUseCase.CONTENT_TAGGING,
    guardrails=fm.SystemLanguageModelGuardrails.PERMISSIVE_CONTENT_TRANSFORMATIONS
)

# Check if the model is available
is_available, reason = model.is_available()
if not is_available:
    print(f"Model unavailable: {reason}")
```

```python
__init__(use_case=SystemLanguageModelUseCase.GENERAL, guardrails=SystemLanguageModelGuardrails.DEFAULT)
```

Create a system language model.

Initializes a new system language model with the specified use case and
guardrail settings. The model is backed by a C implementation and this
constructor manages the creation and lifecycle of the underlying C object.

**Parameters:**

- **use_case** ([SystemLanguageModelUseCase](#apple_fm_sdk.SystemLanguageModelUseCase)) – The use case for the model, which optimizes its behavior
for specific tasks. Defaults to GENERAL for general-purpose use.
- **guardrails** ([SystemLanguageModelGuardrails](#apple_fm_sdk.SystemLanguageModelGuardrails)) – The guardrail settings that control content filtering
and safety measures. Defaults to DEFAULT for standard filtering.

**Raises:**
: [ImportError](https://docs.python.org/3/library/exceptions.html#ImportError) – If the Foundation Models C bindings are not available.

Example

Creating a custom-configured model:

```
import apple_fm_sdk as fm

# Create with default settings
model = fm.SystemLanguageModel()

# Create with custom settings
model = fm.SystemLanguageModel(
    use_case=fm.SystemLanguageModelUseCase.CONTENT_TAGGING,
    guardrails=fm.SystemLanguageModelGuardrails.PERMISSIVE_CONTENT_TRANSFORMATIONS
)
```

```python
is_available()
```

Check if the model is available for use.

This method queries the system to determine whether the language model
can be used on the current device and in the current context. It returns
both an availability status and, if unavailable, a reason code explaining
why the model cannot be used.

Common reasons for unavailability include Apple Intelligence not being
enabled, the device not meeting requirements, or the model still being
downloaded.

**Returns:**
: A tuple containing:

bool: True if the model is available, False otherwise
Optional[SystemLanguageModelUnavailableReason]: The reason for
unavailability if the model is not available, or None if it is
available

**Return type:**
: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[bool](https://docs.python.org/3/library/functions.html#bool), Optional[[SystemLanguageModelUnavailableReason](#apple_fm_sdk.SystemLanguageModelUnavailableReason)]]

Example

Checking model availability:

```
import apple_fm_sdk as fm

test_model = fm.SystemLanguageModel()
is_available, reason = test_model.is_available()

if is_available:
    print("Model is ready to use")
else:
    if reason:
        print(f"Model unavailable: {reason.name}")

        if reason == fm.SystemLanguageModelUnavailableReason.MODEL_NOT_READY:
            print("Please wait for the model to finish downloading")
        elif reason == fm.SystemLanguageModelUnavailableReason.DEVICE_NOT_ELIGIBLE:
            print("This device does not support the model")
```

Note

This method should be called before attempting to use the model to
ensure it is ready for inference.

## SystemLanguageModelUseCase

```python
class apple_fm_sdk.SystemLanguageModelUseCase
```

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

Use cases for system foundation models.

This enumeration defines the different use cases that can be specified when
creating a system foundation model. The use case helps optimize the model’s
behavior for specific tasks.

```python
GENERAL
```

General-purpose foundation model use case suitable for a wide range
of natural language processing tasks.

```python
CONTENT_TAGGING
```

Specialized use case optimized for content classification
and tagging tasks.

## SystemLanguageModelGuardrails

```python
class apple_fm_sdk.SystemLanguageModelGuardrails
```

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

Guardrail settings for system foundation models.

This enumeration defines the different levels of content filtering and safety
guardrails that can be applied to system foundation models. Guardrails help
ensure appropriate and safe model behavior.

```python
DEFAULT
```

Standard guardrails with balanced content filtering appropriate
for general use cases.

```python
PERMISSIVE_CONTENT_TRANSFORMATIONS
```

More permissive guardrails that allow
greater flexibility in content transformation tasks while maintaining
basic safety measures.

## SystemLanguageModelUnavailableReason

```python
class apple_fm_sdk.SystemLanguageModelUnavailableReason
```

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

Reasons why a system foundation model might be unavailable.

This enumeration defines the possible reasons why a system foundation model
cannot be used on the current device or in the current context.

```python
APPLE_INTELLIGENCE_NOT_ENABLED
```

Apple Intelligence features are not enabled
on this device or for this user.

```python
DEVICE_NOT_ELIGIBLE
```

The device does not meet the requirements for running
the system language model.

```python
MODEL_NOT_READY
```

The model is still being downloaded or prepared and is not
yet ready for use.

```python
UNKNOWN
```

The reason for unavailability is unknown or not specified.
