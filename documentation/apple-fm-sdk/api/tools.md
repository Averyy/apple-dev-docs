---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/tools.html
---

# Tools

This page documents the Tool API for function calling capabilities.

Note

**Swift Equivalent:** This Python API corresponds to the [Tool](https://developer.apple.com/documentation/foundationmodels/tool) protocol in the Swift Foundation Models Framework.

## Tool Class

**class apple_fm_sdk.Tool**
: Bases: `_ManagedObject`, [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)
Base class for creating tools that foundation models can invoke during generation.
A `Tool` bridges Python async functions to the Foundation Models API, enabling
foundation models to perform actions like calculations, API calls, database queries,
or any other programmatic operations during generation.
**Tool Lifecycle:**

**Definition**: Subclass Tool and implement required methods/properties
**Registration**: Pass tool instances to LanguageModelSession
**Invocation**: Model automatically calls tools when appropriate
**Execution**: Your async `call()` method executes with parsed arguments
**Response**: Tool result is returned to the model to continue generation

**Callback Mechanism:**
Tools use an async callback system that:

Automatically handles argument parsing from GeneratedContent
Executes your `call()` method in the appropriate async context
Manages threading and event loops transparently
Returns results or errors back to the model

**Async Requirements:**
The `call()` method MUST be an async function (coroutine). This allows tools to:

Make async API calls without blocking
Perform I/O operations efficiently
Run concurrent operations when needed
Integrate with async frameworks

**Error Handling:**

Exceptions in `call()` are caught and reported to the model
The model receives error messages and can adapt its response
Tools should raise descriptive exceptions for better model understanding

Examples
Simple calculator tool:

  ```
  import apple_fm_sdk as fm

  @fm.generable("Calculator parameters")
  class CalculatorParams:
      operation: str = fm.guide("The operation to perform")
      a: float = fm.guide("First number")
      b: float = fm.guide("Second number")

  class CalculatorTool(fm.Tool):
      name = "calculator"
      description = "Performs basic arithmetic operations"

      @property
      def arguments_schema(self) -> fm.GenerationSchema:
          return CalculatorParams.generation_schema()

      async def call(self, args: fm.GeneratedContent) -> str:
          op = args.value(str, for_property="operation")
          a = args.value(float, for_property="a")
          b = args.value(float, for_property="b")

          if op == "add":
              result = a + b
          elif op == "multiply":
              result = a * b
          else:
              raise ValueError(f"Unknown operation: {op}")

          return str(result)
  ```

Tool with async API call:

  ```
  import aiohttp
  import apple_fm_sdk as fm

  @fm.generable("Weather parameters")
  class WeatherParams:
      city: str = fm.guide("The city to get weather for")
      units: str = fm.guide("Temperature units (metric or imperial)")

  class WeatherTool(fm.Tool):
      name = "get_weather"
      description = "Gets current weather for a city"

      @property
      def arguments_schema(self) -> fm.GenerationSchema:
          return WeatherParams.generation_schema()

      async def call(self, args: fm.GeneratedContent) -> str:
          city = args.value(str, for_property="city")
          try:
              units = args.value(str, for_property="units")
          except Exception:
              units = "metric"

          # Implement async API call to fetch weather here
          return "Sunny, 25°C"  # Placeholder response
  ```

Tool with error handling:

  ```
  import apple_fm_sdk as fm

  @fm.generable("Database query parameters")
  class DatabaseParams:
      user_id: int = fm.guide("The user ID to query")

  class DatabaseTool(fm.Tool):
      name = "query_database"
      description = "Queries the user database"

      @property
      def arguments_schema(self) -> fm.GenerationSchema:
          return DatabaseParams.generation_schema()

      async def call(self, args: fm.GeneratedContent) -> str:
          user_id = args.value(int, for_property="user_id")
          # Implement database query with error handling here
          return f"User data for ID {user_id}"  # Placeholder response
  ```

Using tools in a session:

  ```
  from apple_fm_sdk import LanguageModelSession

  session = LanguageModelSession(
      instructions="You are a helpful assistant with access to tools.",
      tools=[CalculatorTool(), WeatherTool(), DatabaseTool()]
  )

  # Model will automatically use tools when appropriate
  response = await session.respond("What's 15% of 240?")
  # Model invokes CalculatorTool internally
  ```

name
The tool’s name (must be set by subclass)

Type:
[str](https://docs.python.org/3/library/stdtypes.html#str)

description
Human-readable description of what the tool does (must be set by subclass)

Type:
[str](https://docs.python.org/3/library/stdtypes.html#str)

Note

Tool names should be descriptive and follow snake_case convention
Descriptions should explain the tool’s purpose and when to use it
The `call()` method must be async even if it doesn’t perform async operations
Tools are automatically managed by the session’s lifecycle
Multiple tools can be registered with a single session

See also

[LanguageModelSession](session.md#apple_fm_sdk.LanguageModelSession): For using tools in sessions
[GenerationSchema](generable.md#apple_fm_sdk.GenerationSchema): For defining argument schemas
[GeneratedContent](generable.md#apple_fm_sdk.GeneratedContent): For accessing parsed arguments

abstract property arguments_schema: [GenerationSchema](generable.md#apple_fm_sdk.GenerationSchema)
Define the schema for tool arguments.
This property must return a GenerationSchema that describes the structure
and types of arguments the tool expects. The model uses this schema to
generate properly formatted arguments when invoking the tool.

Returns:
Schema defining the tool’s expected arguments

Return type:
[GenerationSchema](generable.md#apple_fm_sdk.GenerationSchema)

Example

  ```
  import apple_fm_sdk as fm

  @fm.generable("Search parameters")
  class SearchParams:
      query: str = fm.guide("The search query")
      limit: int = fm.guide("Maximum number of results")

  @property
  def arguments_schema(self) -> fm.GenerationSchema:
      return SearchParams.generation_schema()
  ```

abstractmethod async call(*args*)
Execute the tool’s functionality with the provided arguments.
This async method is invoked when the model decides to use the tool.
The arguments are automatically parsed according to the `arguments_schema`
and provided as a GeneratedContent object.

Parameters:
**args** ([GeneratedContent](generable.md#apple_fm_sdk.GeneratedContent)) – Parsed arguments as GeneratedContent. Access values via `args.value`
which contains a dictionary matching your schema structure.

Returns:
The tool’s result as a string. This result is provided back to the
model to inform its continued generation.

Return type:
[str](https://docs.python.org/3/library/stdtypes.html#str)

Raises:
[Exception](https://docs.python.org/3/library/exceptions.html#Exception) – Any exception raised will be caught and reported to the model
as an error message. Use descriptive exceptions to help the model
understand what went wrong.

Example

  ```
  async def call(self, args: fm.GeneratedContent) -> str:
      query = args.value(str, for_property="query")
      try:
          limit = args.value(int, for_property="limit")
      except Exception:
          limit = 10

      # Perform async operation, for example, database search or another session call here

      return f"Results for '{query}' with limit {limit}"  # Placeholder response
  ```

Note

Must be an async function even if no async operations are performed
Return value must be a string (convert other types as needed)
Exceptions are automatically handled and reported to the model
