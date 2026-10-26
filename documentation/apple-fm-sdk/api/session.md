---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/session.html
---

# LanguageModelSession

This page documents the session management classes for handling sessions with the model.

Note

**Swift Equivalent:** This Python API corresponds to the [LanguageModelSession](https://developer.apple.com/documentation/foundationmodels/languagemodelsession) class in the Swift Foundation Models Framework.

## LanguageModelSession

**class apple_fm_sdk.LanguageModelSession**
: Bases: `_ManagedObject`
Represents a language model session for foundation model interactions.
A `LanguageModelSession` manages the lifecycle of a session with a foundation model,
maintaining session history (transcript), handling tool calls, and providing both
synchronous and streaming response capabilities.
The session is thread-safe for sequential requests but does not support concurrent
requests. If a request is in progress, attempting another request will wait for the
first to complete.
**Session Lifecycle:**

**Creation**: Initialize with optional instructions, model configuration, and tools
**Active Use**: Make requests via `respond()` or `stream_response()`
**Cleanup**: Automatically handled via context manager or explicit cleanup

**Concurrent Request Handling:**
Sessions use an internal lock to prevent concurrent requests. If you need to handle
multiple requests simultaneously, create multiple session instances.

Examples
Basic session creation and usage:

  ```
  import apple_fm_sdk as fm

  # Create a simple session
  session = fm.LanguageModelSession()
  response = await session.respond("Hello, how are you?")
  print(response)
  ```

Session with instructions:

  ```
  import apple_fm_sdk as fm

  # Guide the model's behavior with instructions
  session = fm.LanguageModelSession(
      instructions="You are a helpful bird expert. Provide concise, "
                  "accurate information about birds."
  )
  response = await session.respond("What is a Swift?")
  ```

Session with custom model and tools:

  ```
  import apple_fm_sdk as fm
  from my_tools import CalculatorTool, WeatherTool

  model = fm.SystemLanguageModel(
      temperature=0.7,
      top_p=0.9
  )

  session = fm.LanguageModelSession(
      instructions="You are a helpful assistant with access to tools.",
      model=model,
      tools=[CalculatorTool(), WeatherTool()]
  )

  response = await session.respond("What's the weather like in Cupertino?")
  ```

See also

[SystemLanguageModel](systemmodel.md#apple_fm_sdk.SystemLanguageModel): For model configuration
[Tool](tools.md#apple_fm_sdk.Tool): For creating custom tools
[Transcript](transcript.md#apple_fm_sdk.transcript.Transcript): For accessing session history

__init__(*instructions=None*, *model=None*, *tools=None*)
Create a language model session.

Parameters:

**instructions** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – Optional system instructions to guide the model’s behavior throughout
the session. These instructions persist across all requests in the session.
Example: “You are a helpful coding assistant.”
**model** (*Optional**[*[SystemLanguageModel](systemmodel.md#apple_fm_sdk.SystemLanguageModel)*]*) – Optional specialized system model configuration. If not provided, uses default
SystemLanguageModel() with standard settings. Use this to customize temperature,
top_p, and other generation parameters.
**tools** (*Optional**[*[list](https://docs.python.org/3/library/stdtypes.html#list)*[*[Tool](tools.md#apple_fm_sdk.Tool)*]**]*) – Optional list of Tool instances that the model can invoke during generation.
Tools enable the model to perform actions like calculations, API calls, or
database queries. The model will automatically decide when to use tools based
on the session context.

Raises:
[FoundationModelsError](errors.md#apple_fm_sdk.FoundationModelsError) – If session creation fails

Note
The session maintains a transcript of all interactions, which can be accessed
via the `transcript` property. This transcript is automatically updated after
each request.

classmethod from_transcript(*transcript*, *model=None*, *tools=None*)
Create a new session from an existing transcript.
This method creates a new LanguageModelSession initialized from an existing transcript.
The new session will contain all the conversation history from the transcript, including
user messages, model responses, and tool interactions.

Parameters:

**transcript** ([Transcript](transcript.md#apple_fm_sdk.transcript.Transcript)) – The Transcript instance to initialize the session from.
This transcript contains the complete conversation history.
**model** (*Optional**[*[SystemLanguageModel](systemmodel.md#apple_fm_sdk.SystemLanguageModel)*]*) – Optional SystemLanguageModel to use for the new session. If not
provided, uses the default model. This allows you to continue a conversation
with a different model configuration than the original.
**tools** (*Optional**[*[list](https://docs.python.org/3/library/stdtypes.html#list)*[*[Tool](tools.md#apple_fm_sdk.Tool)*]**]*) – **IMPORTANT**: Tool mentions loaded from a Transcript are historical only.
You must **also** pass tool instances here if you want to allow the model to make new
tool calls in this session.

Returns:
A new LanguageModelSession initialized with the transcript’s history

Return type:
[LanguageModelSession](#apple_fm_sdk.LanguageModelSession)

Raises:
[FoundationModelsError](errors.md#apple_fm_sdk.FoundationModelsError) – If session creation fails

Examples
Resume a conversation from a saved transcript:

  ```
  import apple_fm_sdk as fm
  import json

  # Load a saved transcript
  with open("transcript.json", "r") as f:
      transcript_dict = json.load(f)

  transcript = await fm.Transcript.from_dict(transcript_dict)

  # Create a new session from the transcript
  session = fm.LanguageModelSession.from_transcript(transcript)

  # Continue the session
  response = await session.respond("Summarize the session so far.")
  ```

Resume with tools:

  ```
  import apple_fm_sdk as fm
  from my_tools import CalculatorTool, WeatherTool

  # Load transcript that had tool calls
  transcript = await fm.Transcript.from_dict(transcript_dict)

  # IMPORTANT: You must pass the tool instances explicitly.
  # The transcript contains the history of tool calls, but not
  # the ability to make new tool calls unless you provide them.
  session = fm.LanguageModelSession.from_transcript(
      transcript,
      tools=[CalculatorTool(), WeatherTool()]
  )

  # Now the model can make new tool calls
  response = await session.respond("Calculate 15 * 24")
  ```

Note

The transcript contains the session instructions, so you don’t need to
pass instructions separately
The new session shares the transcript object with the original
Any new interactions will update the transcript
Tool mentions from the transcript are historical only. To allow the model to
make new tool calls, you must explicitly pass the tool instances in the `tools` parameter.

See also

[Transcript](transcript.md#apple_fm_sdk.transcript.Transcript): For working with transcripts
[from_dict()](transcript.md#apple_fm_sdk.transcript.Transcript.from_dict): For loading transcripts from JSON
[Tool](tools.md#apple_fm_sdk.Tool): For creating custom tools

property is_responding: [bool](https://docs.python.org/3/library/functions.html#bool)
Check if the session is currently responding to a request.

Returns:
True if the session is currently processing a request, False otherwise

Return type:
[bool](https://docs.python.org/3/library/functions.html#bool)

async respond(*prompt: str | Attachment | list[str | Attachment]*, ***, *options: GenerationOptions | None = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str)

async respond(*prompt: str | Attachment | list[str | Attachment]*, ***, *generating: type[Generable]*, *options: GenerationOptions | None = None*) → [Type](https://docs.python.org/3/library/typing.html#typing.Type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)]

async respond(*prompt: str | Attachment | list[str | Attachment]*, ***, *generating: Generable*, *options: GenerationOptions | None = None*) → [Type](https://docs.python.org/3/library/typing.html#typing.Type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)]

async respond(*prompt: str | Attachment | list[str | Attachment]*, ***, *schema: GenerationSchema*, *options: GenerationOptions | None = None*) → [GeneratedContent](generable.md#apple_fm_sdk.GeneratedContent)

async respond(*prompt: str | Attachment | list[str | Attachment]*, ***, *json_schema: dict*, *options: GenerationOptions | None = None*) → [GeneratedContent](generable.md#apple_fm_sdk.GeneratedContent)
Get a response to a prompt with optional guided generation.
This function supports multiple response modes:

**Basic text response**: Returns a plain string
**Guided generation with Generable**: Returns a typed Python object
**Guided generation with schema**: Returns structured GeneratedContent
**Guided generation with JSON schema**: Returns structured GeneratedContent

The session automatically updates its transcript after each response, maintaining
the full session history.

Parameters:

**prompt** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The input prompt string to send to the model
**generating** (*Optional**[**Union**[**Type**[*[Generable](generable.md#apple_fm_sdk.Generable)*]**, *[Generable](generable.md#apple_fm_sdk.Generable)*]**]*) – Optional Generable type or instance for type-safe guided generation.
When provided, the response will be constrained to match the structure of
the Generable type and automatically converted to an instance of that type.
**schema** (*Optional**[*[GenerationSchema](generable.md#apple_fm_sdk.GenerationSchema)*]*) – Optional GenerationSchema for explicit schema-based guided generation.
Use this for custom schemas that don’t map to a Generable type.
**json_schema** (*Optional**[*[dict](https://docs.python.org/3/library/stdtypes.html#dict)*]*) – Optional JSON schema dictionary for guided generation. The schema
should follow JSON Schema specification.
**options** (*Optional**[*[GenerationOptions](generation_options.md#apple_fm_sdk.GenerationOptions)*]*) – Optional GenerationOptions to control generation behavior such as
temperature, sampling mode, and maximum response tokens. These options apply
to this specific request and override any session-level defaults.

Returns:
Plain text response if no generation constraints are specified, or
instance of generating type if `generating` parameter is provided, or
structured content if `schema` or `json_schema` is provided

Return type:
Union[[str](https://docs.python.org/3/library/stdtypes.html#str), Any, [GeneratedContent](generable.md#apple_fm_sdk.GeneratedContent)]

Raises:

[FoundationModelsError](errors.md#apple_fm_sdk.FoundationModelsError) – If the response fails or times out
[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If both `generating` and `schema` are provided, or if the
generating type is not a valid Generable
[asyncio.CancelledError](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError) – If the request is cancelled

Examples

Basic text response::import apple_fm_sdk as fm
session = fm.LanguageModelSession()
response = await session.respond(“What is the capital of France?”)
print(response)  # Plain string response

Guided generation with Generable type:

  ```
  import apple_fm_sdk as fm

  @fm.generable()
  class Cat:
      name: str
      age: int
      profile: str

  session = fm.LanguageModelSession()
  cat = await session.respond(
      "Generate a cat named Maomao",
      generating=Cat
  )
  print(f"{cat.name} is {cat.age} years old")
  ```

Multi-turn session:

  ```
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession(
      instructions="You are a helpful expert on architecture."
  )

  # First turn
  response1 = await session.respond("What is the tallest building in the world?")
  print(response1)

  # Second turn - context is maintained
  response2 = await session.respond(
      "What's the architectural style of that building?"
  )
  print(response2)
  ```

Using generation options:

  ```
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession()

  # Control generation with custom options
  options = fm.GenerationOptions(
      temperature=0.7,
      sampling=fm.SamplingMode.random(top=50, seed=42),
      maximum_response_tokens=500
  )

  response = await session.respond(
      "Write a creative story",
      options=options
  )
  print(response)
  ```

Note

Only one of `generating`, `schema`, or `json_schema` can be specified
The session maintains session context across multiple `respond()` calls
Concurrent calls to `respond()` on the same session will be serialized
For streaming responses, use [stream_response()](#apple_fm_sdk.LanguageModelSession.stream_response) instead

See also

[stream_response()](#apple_fm_sdk.LanguageModelSession.stream_response): For streaming text responses
[Generable](generable.md#apple_fm_sdk.Generable): For creating typed response structures
[GenerationSchema](generable.md#apple_fm_sdk.GenerationSchema): For custom schemas

async stream_response(*prompt*, *options=None*)
Stream response chunks for a prompt (text only).
This function provides real-time streaming of the model’s response, yielding text
snapshots as they become available. Each yielded value represents the complete
response text generated so far, rather than the delta from the previous chunk.
**Streaming Behavior:**

Yields complete text snapshots (not deltas) as generation progresses
The final yield contains the complete response
Automatically updates the session transcript after completion
Does not support guided generation (text responses only)
Can be cancelled mid-stream using asyncio cancellation

Parameters:

**prompt** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The input prompt string to send to the model
**options** (*Optional**[*[GenerationOptions](generation_options.md#apple_fm_sdk.GenerationOptions)*]*) – Optional GenerationOptions to control generation behavior such as
temperature, sampling mode, and maximum response tokens. These options apply
to this specific request and override any session-level defaults.

Yields:
Progressive snapshots of the response text. Each snapshot contains
the full text generated so far, rather than only the new tokens.

Ytype:
str

Raises:

[FoundationModelsError](errors.md#apple_fm_sdk.FoundationModelsError) – If streaming fails or encounters an error
[asyncio.CancelledError](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError) – If the stream is cancelled

Examples
Basic streaming:

  ```
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession()

  async for chunk in session.stream_response("Tell me a story"):
      print(chunk, end="", flush=True)
  ```

Streaming with options:

  ```
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession()

  options = fm.GenerationOptions(
      temperature=0.8,
      sampling=fm.SamplingMode.random(top=50),
      maximum_response_tokens=1000
  )

  async for chunk in session.stream_response("Write a creative story", options=options):
      print(chunk, end="", flush=True)
  ```

Cancelling a stream:

  ```
  import asyncio
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession()

  async def stream_with_timeout():
      try:
          async for chunk in session.stream_response("Write a long essay"):
              print(chunk)
              # Simulate some processing
              await asyncio.sleep(0.1)
      except asyncio.CancelledError:
          print("Stream cancelled")
          raise

  # Cancel after 5 seconds
  task = asyncio.create_task(stream_with_timeout())
  await asyncio.sleep(5)
  task.cancel()
  ```

Streaming with error handling::import apple_fm_sdk as fm
session = fm.LanguageModelSession()

try:
async for chunk in session.stream_response(“Hello”):print(chunk)

except fm.FoundationModelsError as e:print(f”Streaming error: {e}”)

Note

Streaming currently only supports basic text responses
For guided generation, use [respond()](#apple_fm_sdk.LanguageModelSession.respond) instead
Each snapshot contains the full text, rather than only new tokens
The session transcript is updated only after streaming completes
Breaking out of the async for loop early will properly clean up resources

See also

[respond()](#apple_fm_sdk.LanguageModelSession.respond): For non-streaming responses with guided generation support
