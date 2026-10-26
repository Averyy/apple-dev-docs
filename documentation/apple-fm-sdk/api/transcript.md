---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/transcript.html
---

# Transcript

This page documents the Transcript API for accessing session history.

Note

**Swift Equivalent:** This Python API corresponds to the [Transcript](https://developer.apple.com/documentation/foundationmodels/transcript) class in the Swift Foundation Models Framework.

## Transcript Class

**class apple_fm_sdk.transcript.Transcript**
: Bases: [object](https://docs.python.org/3/library/functions.html#object)
Represents a foundation model session’s transcript.
A `Transcript` provides access to the complete session history of a
LanguageModelSession, including all user prompts, model responses, and tool
invocations. The transcript is automatically updated after each interaction
with the model.
**Transcript Format:**
The transcript follows the Foundation Models Swift framework structure and is
organized as a dictionary containing:

**version**: Integer version number (currently 1)
**type**: String identifier “FoundationModels.Transcript”

**transcript**: Object containing:

**entries**: List of session entries, each with:
`id`: Unique UUID for the entry
`role`: One of “instructions”, “user”, “response”, or “tool”
`contents`: Array of content objects with `type`, `id`, and type-specific fields

**Entry Types by Role:**

**instructions**: System instructions and tool definitions
`tools`: Array of available tool definitions
`contents`: Array with text instructions

**user**: User messages and requests
`contents`: Array of content objects (text and more)
`options`: Optional configuration for the request
`responseFormat`: Optional structured output schema

**response**: Model-generated responses
`toolCalls`: Array of tool invocations (if tools were called)
`contents`: Array of response content (text or structured data)
`assets`: Array of model asset identifiers used

**tool**: Tool execution results
`toolName`: Name of the executed tool
`toolCallID`: UUID linking to the tool call
`contents`: Array with tool execution results

**When Transcripts Are Updated:**

After each `respond()` call completes successfully
After each `stream_response()` completes
After tool invocations are processed
NOT during streaming (only after completion)
NOT if a request fails or is cancelled

Examples
Accessing transcript after session:

  ```
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession()

  await session.respond("Hello!")
  await session.respond("What is Python?")

  # Get the full session history
  transcript = await session.transcript.to_dict()

  # Access the entries
  entries = transcript["transcript"]["entries"]
  for entry in entries:
      role = entry["role"]
      print(f"Entry role: {role}")
      if "contents" in entry:
          for content in entry["contents"]:
              if content["type"] == "text":
                  print(f"  Text: {content['text']}")
  ```

Monitoring session length::import apple_fm_sdk as fm
session = fm.LanguageModelSession()

for i in range(5):await session.respond(f”Question {i}”)
transcript = await session.transcript.to_dict()
entry_count = len(transcript[“transcript”][“entries”])
print(f”Session has {entry_count} entries”)

Examining tool calls in transcript:

  ```
  import apple_fm_sdk as fm
  from my_tools import CalculatorTool

  session = fm.LanguageModelSession(
      tools=[CalculatorTool()]
  )

  await session.respond("What is 15 * 24?")

  transcript = await session.transcript.to_dict()

  # Find entries with tool calls
  for entry in transcript["transcript"]["entries"]:
      if entry["role"] == "response" and "toolCalls" in entry:
          print(f"Tool calls: {entry['toolCalls']}")
      elif entry["role"] == "tool":
          print(f"Tool result for {entry['toolName']}")
  ```

Saving session history:

  ```
  import apple_fm_sdk as fm
  import json

  session = fm.LanguageModelSession()

  # Have a session
  await session.respond("Hello")
  await session.respond("Tell me about Python")

  # Save transcript to file
  transcript = await session.transcript.to_dict()
  with open("session.json", "w") as f:
      json.dump(transcript, f, indent=2)
  ```

Note

The transcript object shares the session’s internal pointer
Transcripts are read-only; you cannot modify session history
Large sessions may result in large transcript dictionaries
The transcript format follows the Foundation Models Swift framework structure
Accessing the transcript does not affect the session state

See also

[LanguageModelSession](session.md#apple_fm_sdk.LanguageModelSession): For creating sessions
`respond()`: For making requests

__init__(*_ptr*)
Initialize a Transcript instance.

Note
Transcript instances are automatically created by LanguageModelSession.
Do not create Transcript instances directly.

async to_dict()
Get the current transcript of the session as a dictionary.
This function retrieves the complete session history, including all
user messages, model responses, and tool interactions. The transcript
is returned as a structured dictionary following the Foundation Models
Swift framework format.

Returns:
The transcript data as a dictionary with the following structure:

`version` (int): Version number (currently 1)
`type` (str): Type identifier “FoundationModels.Transcript”

`transcript` (dict): Object containing:

`entries` (list): List of session entries, each with:
`id` (str): Unique UUID for the entry
`role` (str): One of “instructions”, “user”, “response”, or “tool”
`contents` (list): Array of content objects
Additional role-specific fields (tools, toolCalls, options, and more)

Return type:
[dict](https://docs.python.org/3/library/stdtypes.html#dict)

Raises:
[GenerationError](errors.md#apple_fm_sdk.GenerationError) – If fetching the transcript fails due to an internal error

Example

  ```
  import apple_fm_sdk as fm

  session = fm.LanguageModelSession()
  await session.respond("Hello!")

  transcript = await session.transcript.to_dict()

  # Access entries
  entries = transcript["transcript"]["entries"]
  for entry in entries:
      print(f"{entry['role']}: {entry.get('id')}")
  ```

Note

This is an async function and must be awaited
The returned dictionary is a snapshot; it won’t update automatically
Call this function again to get an updated transcript after new interactions

async classmethod from_dict(*dict*)
Create a Transcript from a dictionary representation.
This method deserializes a transcript dictionary (typically loaded from JSON)
and creates a Transcript instance. This is useful for loading saved session
transcripts and resuming sessions with the full history intact.

Parameters:
**dict** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – Dictionary representation of a transcript, typically loaded from
a JSON file. Must match the Foundation Models transcript format.

Returns:
A new Transcript instance initialized with the provided data

Return type:
[Transcript](#apple_fm_sdk.transcript.Transcript)

Raises:
[GenerationError](errors.md#apple_fm_sdk.GenerationError) – If the dictionary format is invalid or cannot be parsed

Warning
**Tools in a transcript:**
The transcript preserves the *history* of tool calls (what was called and
what the results were), but not the *capability* to make new tool calls.
Tool definitions stored in a transcript JSON will appear in the transcript’s
content history, but they will **not** be automatically available for the model
to call. That’s because the transcript doesn’t actually contain the tool
implementations. To allow the model to invoke tools mentioned in the transcript,
implement each tool in Python and then create a session with both the transcript
and tools using `from_transcript()`

Examples
Load a transcript from a JSON file:

  ```
  import apple_fm_sdk as fm
  import json

  # Load transcript from file
  with open("transcript.json", "r") as f:
      transcript_dict = json.load(f)

  # Create Transcript instance
  transcript = await fm.Transcript.from_dict(transcript_dict)

  # Now you can create a session starting from this transcript
  session = fm.LanguageModelSession.from_transcript(transcript)
  ```

Load and resume with tools:

  ```
  import apple_fm_sdk as fm
  import json
  from my_tools import CalculatorTool, WeatherTool

  # Load transcript that had tool calls
  with open("transcript_with_tools.json", "r") as f:
      transcript_dict = json.load(f)

  transcript = await fm.Transcript.from_dict(transcript_dict)

  # IMPORTANT: Tools in the transcript are historical mentions only.
  # To allow the model to call a tool, you must explicitly instantiate each
  # tool in Python and then pass them to the session initializer.
  session = fm.LanguageModelSession.from_transcript(
      transcript,
      tools=[CalculatorTool(), WeatherTool()]
  )
  ```

Note

The dictionary must follow the Foundation Models transcript format
Tool definitions in the transcript are for historical reference only
To use tools with the transcript, pass them to
`from_transcript()`

See also

[to_dict()](#apple_fm_sdk.transcript.Transcript.to_dict): For converting a Transcript to a dictionary
`from_transcript()`: For creating sessions from transcripts
[Tool](tools.md#apple_fm_sdk.Tool): For creating custom tools

## See Also

- [LanguageModelSession](session.md) - Session API
- [Basic Usage](../basic_usage.md) - Basic usage guide
