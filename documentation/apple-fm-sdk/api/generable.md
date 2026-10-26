---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/generable.html
---

# Generable

This page documents the guided generation API for structured outputs.

Note

**Swift Equivalent:** This Python API corresponds to the [Generable](https://developer.apple.com/documentation/foundationmodels/generable) protocol and [GenerationSchema](https://developer.apple.com/documentation/foundationmodels/generationschema) in the Swift Foundation Models Framework.

## @generable Decorator

**apple_fm_sdk.generable(*arg: Type[object]*, */*) → [Type](https://docs.python.org/3/library/typing.html#typing.Type)[[Generable](#apple_fm_sdk.Generable)]**
: Decorator that makes a class generable for use with Foundation Models.
This decorator transforms a regular Python class (typically a dataclass) into
a generable type that can be used with Foundation Models’ guided generation
features. It adds all necessary methods and attributes to support schema
generation, content conversion, and partial generation during streaming.
The decorator performs the following transformations:

Converts the class to a dataclass if it isn’t already
Adds a `generation_schema()` class method for schema introspection
Adds `ConvertibleFromGeneratedContent` support for deserialization
Adds `ConvertibleToGeneratedContent` support for serialization
Creates a `PartiallyGenerated` inner class for streaming support
Adds required methods for structured generation

This decorator can be used with or without parentheses:
- `@fm.generable` - without parentheses
- `@fm.generable()` - with empty parentheses
- `@fm.generable("description")` - with a description

Parameters:
**arg** (*Optional**[**Union**[*[type](https://docs.python.org/3/library/functions.html#type)*, *[str](https://docs.python.org/3/library/stdtypes.html#str)*]**]*) – Either a class (when used without parentheses) or an optional
human-readable description of what this type represents. This description
is included in the generation schema and can help guide the model’s
generation behavior.

Returns:
Either the decorated class (when used without parentheses) or a
decorator function (when used with parentheses)

Return type:
Union[Type[[Generable](#apple_fm_sdk.Generable)], Callable[[Type], Type[[Generable](#apple_fm_sdk.Generable)]]]

Example
Basic usage with a dataclass:

  ```
  import apple_fm_sdk as fm

  @fm.generable("A cat's profile")
  class Cat:
      name: str = fm.guide("Cat's name")
      age: int = fm.guide("Age in years", range=(0, 20))
      profile: str = fm.guide("What makes this cat unique")
  ```

Usage without parentheses:

  ```
  @fm.generable
  class Dog:
      name: str
      breed: str
  ```

Using with Session for guided generation:

  ```
  session = fm.LanguageModelSession()
  cat = await session.respond(
      Cat,
      prompt="Generate a cat named Maomao who is 2 years old and has a fluffy tail"
  )
  print(f"{cat.name} is {cat.age} years old: {cat.profile}")
  ```

Nested generable types:

  ```
  import apple_fm_sdk as fm

  @fm.generable("Pet club")
  class PetClub:
      name: str = fm.guide("Club name")
      cats: [Cat] = fm.guide("List of cats in the club")
  ```

Note
@fm.generable automatically applies the `@dataclass` decorator if the
class is not already a dataclass.

See also
[guide()](#apple_fm_sdk.guide) for adding constraints to individual fields.
[GenerationSchema](#apple_fm_sdk.GenerationSchema) for the schema representation.
`Session` for using generable types in generation.

**apple_fm_sdk.generable(*arg: None = None*, */*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[Type](https://docs.python.org/3/library/typing.html#typing.Type)[[object](https://docs.python.org/3/library/functions.html#object)]], [Type](https://docs.python.org/3/library/typing.html#typing.Type)[[Generable](#apple_fm_sdk.Generable)]]**
: Decorator that makes a class generable for use with Foundation Models.
This decorator transforms a regular Python class (typically a dataclass) into
a generable type that can be used with Foundation Models’ guided generation
features. It adds all necessary methods and attributes to support schema
generation, content conversion, and partial generation during streaming.
The decorator performs the following transformations:

Converts the class to a dataclass if it isn’t already
Adds a `generation_schema()` class method for schema introspection
Adds `ConvertibleFromGeneratedContent` support for deserialization
Adds `ConvertibleToGeneratedContent` support for serialization
Creates a `PartiallyGenerated` inner class for streaming support
Adds required methods for structured generation

This decorator can be used with or without parentheses:
- `@fm.generable` - without parentheses
- `@fm.generable()` - with empty parentheses
- `@fm.generable("description")` - with a description

Parameters:
**arg** (*Optional**[**Union**[*[type](https://docs.python.org/3/library/functions.html#type)*, *[str](https://docs.python.org/3/library/stdtypes.html#str)*]**]*) – Either a class (when used without parentheses) or an optional
human-readable description of what this type represents. This description
is included in the generation schema and can help guide the model’s
generation behavior.

Returns:
Either the decorated class (when used without parentheses) or a
decorator function (when used with parentheses)

Return type:
Union[Type[[Generable](#apple_fm_sdk.Generable)], Callable[[Type], Type[[Generable](#apple_fm_sdk.Generable)]]]

Example
Basic usage with a dataclass:

  ```
  import apple_fm_sdk as fm

  @fm.generable("A cat's profile")
  class Cat:
      name: str = fm.guide("Cat's name")
      age: int = fm.guide("Age in years", range=(0, 20))
      profile: str = fm.guide("What makes this cat unique")
  ```

Usage without parentheses:

  ```
  @fm.generable
  class Dog:
      name: str
      breed: str
  ```

Using with Session for guided generation:

  ```
  session = fm.LanguageModelSession()
  cat = await session.respond(
      Cat,
      prompt="Generate a cat named Maomao who is 2 years old and has a fluffy tail"
  )
  print(f"{cat.name} is {cat.age} years old: {cat.profile}")
  ```

Nested generable types:

  ```
  import apple_fm_sdk as fm

  @fm.generable("Pet club")
  class PetClub:
      name: str = fm.guide("Club name")
      cats: [Cat] = fm.guide("List of cats in the club")
  ```

Note
@fm.generable automatically applies the `@dataclass` decorator if the
class is not already a dataclass.

See also
[guide()](#apple_fm_sdk.guide) for adding constraints to individual fields.
[GenerationSchema](#apple_fm_sdk.GenerationSchema) for the schema representation.
`Session` for using generable types in generation.

**apple_fm_sdk.generable(*arg: str*, */*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[Type](https://docs.python.org/3/library/typing.html#typing.Type)[[object](https://docs.python.org/3/library/functions.html#object)]], [Type](https://docs.python.org/3/library/typing.html#typing.Type)[[Generable](#apple_fm_sdk.Generable)]]**
: Decorator that makes a class generable for use with Foundation Models.
This decorator transforms a regular Python class (typically a dataclass) into
a generable type that can be used with Foundation Models’ guided generation
features. It adds all necessary methods and attributes to support schema
generation, content conversion, and partial generation during streaming.
The decorator performs the following transformations:

Converts the class to a dataclass if it isn’t already
Adds a `generation_schema()` class method for schema introspection
Adds `ConvertibleFromGeneratedContent` support for deserialization
Adds `ConvertibleToGeneratedContent` support for serialization
Creates a `PartiallyGenerated` inner class for streaming support
Adds required methods for structured generation

This decorator can be used with or without parentheses:
- `@fm.generable` - without parentheses
- `@fm.generable()` - with empty parentheses
- `@fm.generable("description")` - with a description

Parameters:
**arg** (*Optional**[**Union**[*[type](https://docs.python.org/3/library/functions.html#type)*, *[str](https://docs.python.org/3/library/stdtypes.html#str)*]**]*) – Either a class (when used without parentheses) or an optional
human-readable description of what this type represents. This description
is included in the generation schema and can help guide the model’s
generation behavior.

Returns:
Either the decorated class (when used without parentheses) or a
decorator function (when used with parentheses)

Return type:
Union[Type[[Generable](#apple_fm_sdk.Generable)], Callable[[Type], Type[[Generable](#apple_fm_sdk.Generable)]]]

Example
Basic usage with a dataclass:

  ```
  import apple_fm_sdk as fm

  @fm.generable("A cat's profile")
  class Cat:
      name: str = fm.guide("Cat's name")
      age: int = fm.guide("Age in years", range=(0, 20))
      profile: str = fm.guide("What makes this cat unique")
  ```

Usage without parentheses:

  ```
  @fm.generable
  class Dog:
      name: str
      breed: str
  ```

Using with Session for guided generation:

  ```
  session = fm.LanguageModelSession()
  cat = await session.respond(
      Cat,
      prompt="Generate a cat named Maomao who is 2 years old and has a fluffy tail"
  )
  print(f"{cat.name} is {cat.age} years old: {cat.profile}")
  ```

Nested generable types:

  ```
  import apple_fm_sdk as fm

  @fm.generable("Pet club")
  class PetClub:
      name: str = fm.guide("Club name")
      cats: [Cat] = fm.guide("List of cats in the club")
  ```

Note
@fm.generable automatically applies the `@dataclass` decorator if the
class is not already a dataclass.

See also
[guide()](#apple_fm_sdk.guide) for adding constraints to individual fields.
[GenerationSchema](#apple_fm_sdk.GenerationSchema) for the schema representation.
`Session` for using generable types in generation.

## guide Function

**apple_fm_sdk.guide(*description=None*, ***, *anyOf=None*, *constant=None*, *count=None*, *element=None*, *max_items=None*, *maximum=None*, *min_items=None*, *minimum=None*, *range=None*, *regex=None*)**
: Create a field with a guide, similar to Swift’s @Guide annotation.
This convenience function creates a dataclass field with generation guide
metadata that can be used to constrain model output during generation.
Multiple constraints can be applied to a single field.

Parameters:

**description** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Description of the field for documentation purposes
**anyOf** (*List**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]**, **optional*) – List of valid string choices that constrain output to specific values
**constant** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Constrains output to a single constant value
**count** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Expected exact number of items for collections (must be positive)
**element** (*GenerationGuide**, **optional*) – Guide to apply to array elements
**max_items** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Maximum number of items for collections (must be non-negative)
**maximum** (*Union**[*[int](https://docs.python.org/3/library/functions.html#int)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**, **optional*) – Maximum value for numeric types
**min_items** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Minimum number of items for collections (must be non-negative)
**minimum** (*Union**[*[int](https://docs.python.org/3/library/functions.html#int)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**, **optional*) – Minimum value for numeric types
**range** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*, **optional*) – Tuple of (min, max) for numeric ranges
**regex** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Regular expression pattern that the output must match

Returns:
A dataclass field with guide metadata attached

Return type:
Any

Raises:
[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If any constraint values are invalid (for example, negative counts,
malformed ranges, non-string choices)

Example
Basic field with description only:

  ```
  name: str = guide("The person's full name")
  ```

Numeric field with range constraint:

  ```
  age: int = guide("Age in years", range=(0, 120))
  ```

Collection with exact count:

  ```
  hobbies: List[str] = guide("List of hobbies", count=3)
  ```

String field with choices:

  ```
  color: str = guide("Favorite color", anyOf=["red", "blue", "green"])
  ```

Numeric field with separate min/max:

  ```
  score: float = guide("Test score", minimum=0.0, maximum=100.0)
  ```

Collection with size constraints:

  ```
  tags: List[str] = guide("Tags list", min_items=1, max_items=5)
  ```

Constant value constraint:

  ```
  status: str = guide("Status", constant="active")
  ```

Regex pattern constraint:

  ```
  email: str = guide("Name", regex=r"#/[a-zA-Z]+/#")
  ```

Element constraint for arrays:

  ```
  scores: List[int] = guide("Test scores", element=GenerationGuide.range((0, 100)))
  ```

Note
The guide function validates constraint parameters at creation time
and stores them as metadata that can be processed by generation
systems to enforce the specified constraints.

## Generable Class

**class apple_fm_sdk.Generable**
: Bases: `ConvertibleFromGeneratedContent`, `ConvertibleToGeneratedContent`, [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)
Protocol for types that support structured generation.
Equivalent to Swift’s Generable protocol.

classmethod generation_schema()
Get the generation schema for this type.

PartiallyGenerated = None

## GeneratedContent Class

**class apple_fm_sdk.GeneratedContent**
: Bases: `_ManagedObject`
Represents generated content, similar to Swift’s GeneratedContent.
This is the actual content generated according to a schema.

__init__(*content_dict=None*, *id=None*)
Create GeneratedContent.

Parameters:

**content_dict** (*Optional**[**Dict**]*) – Dictionary representation of the content
**id** (*Optional**[**GenerationID**]*) – Optional GenerationID

classmethod from_json(*json_str*)
Create GeneratedContent from JSON string.

to_json()
Convert to JSON string.

value(*type_class=None*, *for_property=None*)
Extract a value from the generated content.

Parameters:

**type_class** (*Optional**[**Type**]*) – The type to convert to
**for_property** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – The property name to extract (if None, extract the whole content)

Returns:
The extracted value converted to the specified type

Return type:
Any

property is_complete: [bool](https://docs.python.org/3/library/functions.html#bool)
Check if the generated content is complete.

## GenerationSchema Class

**class apple_fm_sdk.GenerationSchema**
: Bases: `_ManagedObject`
Represents a generation schema that defines the structure for guided generation.
A GenerationSchema describes the expected structure of generated content, including
the type, properties, and nested schemas. This is used with guided generation to
ensure the model’s output conforms to a specific format, such as JSON objects with
defined fields and types.
The schema is similar to JSON Schema but optimized for use with Foundation Models.
It supports basic types (str, int, float, bool), optional types, lists, and nested
object structures.

Variables:

**type_class** (*Type*) – The Python class this schema represents.
**description** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – Optional human-readable description of the schema.
**properties** (*List**[**Property**]*) – List of Property objects defining the schema’s fields.
**nested_schemas** (*List**[*[GenerationSchema](#apple_fm_sdk.GenerationSchema)*]*) – List of nested GenerationSchema objects for complex types.
**extra_schema_fields** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*, **Any**]*) – Additional schema fields that pass through to the
underlying Foundation Models API.

Note: Do not instantiate GenerationSchema directly. Use the [generable()](#apple_fm_sdk.generable) decorator
which automatically produces a GenerationSchema, or load in a json schema from your Swift app
instead.

See also
`Property` for defining individual schema fields.
`GenerationGuide` for constraining property values.

nested_schemas: [List](https://docs.python.org/3/library/typing.html#typing.List)[[GenerationSchema](#apple_fm_sdk.GenerationSchema)] = []

__init__(*type_class*, *description=None*, *properties=None*, *dynamic_nested_types=[]*)
Initialize a GenerationSchema instance.

Parameters:

**type_class** (*Type*) – The Python class this schema represents. This is typically
a dataclass or similar structured type that defines the shape of the data.
**description** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – Optional human-readable description of what this schema
represents. This can help provide context for the model during generation.
**properties** (*Optional**[**List**[**Property**]**]*) – List of Property objects that define the fields/attributes
of this schema. Each property specifies a field name, type, and optional
constraints. If None, defaults to an empty list.
**dynamic_nested_types** (*List**[*[GenerationSchema](#apple_fm_sdk.GenerationSchema)*]*) – List of nested GenerationSchema objects for
complex types that reference other schemas. Used when a property’s type
is itself a structured object.

Example

  ```
  >>> import apple_fm_sdk as fm
  >>>
  >>> @fm.generable("A cat's profile")
  >>> class Cat:
  ...     name: str
  ...     age: int
  >>>
  >>> schema = GenerationSchema(
  ...     type_class=Cat,
  ...     description="A cat's profile",
  ...     properties=[
  ...         Property(name="name", type_class=str),
  ...         Property(name="age", type_class=int)
  ...     ]
  ... )
  ```

Note
The schema is automatically converted to its C representation for use
with the underlying Foundation Models runtime.

type_class: [Type](https://docs.python.org/3/library/typing.html#typing.Type)

description: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None

properties: [List](https://docs.python.org/3/library/typing.html#typing.List)[Property]

to_dict()
Convert the GenerationSchema to a dictionary representation.
This method serializes the schema into a dictionary format compatible with
the Foundation Models Swift API. The resulting dictionary contains the schema
definition in a JSON-compatible format that can be used for validation,
inspection, or transmission.

Returns:
A dictionary representation of the schema, including type information,
properties, and any nested schemas.

Return type:
[dict](https://docs.python.org/3/library/stdtypes.html#dict)

Raises:

[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If the schema cannot be serialized (for example, empty JSON
string returned from the C layer).
[FoundationModelsError](errors.md#apple_fm_sdk.FoundationModelsError) – If an error occurs during serialization in
the underlying C/Swift implementation.

Example

  ```
  >>> schema = GenerationSchema(
  ...     type_class=Cat,
  ...     description="A cat's profile",
  ...     properties=[Property(name="name", type_class=str)]
  ... )
  >>> schema_dict = schema.to_dict()
  >>> print(schema_dict)
  {'name': 'Cat', 'description': 'A cat's profile', 'properties': [...]}
  ```

Note
This method interacts with the C layer to generate the schema dictionary.
Memory management is handled automatically.

See also
The schema dictionary format follows the Foundation Models schema
specification used by the Swift API.
