# Well-known types

**Framework**: QuickTime File Format

Basic data types.

#### Overview

| Code | Type | Comment |
| --- | --- | --- |
| 0 | reserved | Reserved for use where no type needs to be indicated |
| 1 | UTF-8 | Without any count or NULL terminator |
| 2 | UTF-16 | Also known as UTF-16BE |
| 3 | S/JIS | Deprecated unless it is needed for special Japanese characters |
| 4 | UTF-8 sort | Variant storage of a string for sorting only |
| 5 | UTF-16 sort | Variant storage of a string for sorting only |
| 13 | JPEG | In a JFIF wrapper |
| 14 | PNG | In a PNG wrapper |
| 21 | BE Signed Integer | A big-endian signed integer in 1,2,3 or 4 bytes. Note: This data type is not supported in [`Timed metadata media`](timed_metadata_media.md). Use one of the fixed-size signed integer data types (that is, type codes 65, 66, or 67) instead. |
| 22 | BE Unsigned Integer | A big-endian unsigned integer in 1,2,3 or 4 bytes; size of value determines integer size. Note: This data type is not supported in [`Timed metadata media`](timed_metadata_media.md). Use one of the fixed-size unsigned integer data types (that is, type codes 75, 76, or 77) instead. |
| 23 | BE Float32 | A big-endian 32-bit floating point value (IEEE754) |
| 24 | BE Float64 | A big-endian 64-bit floating point value (IEEE754) |
| 27 | BMP | Windows bitmap format graphics |
| 28 | QuickTime Metadata atom | A block of data having the structure of the Metadata atom defined in this specification |
| 65 | 8-bit Signed Integer | An 8-bit signed integer |
| 66 | BE 16-bit Signed Integer | A big-endian 16-bit signed integer |
| 67 | BE 32-bit Signed Integer | A big-endian 32-bit signed integer |
| 70 | BE PointF32 | A block of data representing a two dimensional (2D) point with 32-bit big-endian floating point x and y coordinates. It has the structure: `struct { BEFloat32 x; BEFloat32 y; }` |
| 71 | BE DimensionsF32 | A block of data representing 2D dimensions with 32-bit big-endian floating point width and height. It has the structure: `struct { BEFloat32 width; BEFloat32 height; }` |
| 72 | BE RectF32 | A block of data representing a 2D rectangle with 32-bit big-endian floating point x and y coordinates and a 32-bit big-endian floating point width and height size. It has the structure: `struct { BEFloat32 x; BEFloat32 y; BEFloat32 width; BEFloat32 height;}` or the equivalent structure: `struct { PointF32 origin; DimensionsF32 size; }` |
| 74 | BE 64-bit Signed Integer | A big-endian 64-bit signed integer |
| 75 | 8-bit Unsigned Integer | An 8-bit unsigned integer |
| 76 | BE 16-bit Unsigned Integer | A big-endian 16-bit unsigned integer |
| 77 | BE 32-bit Unsigned Integer | A big-endian 32-bit unsigned integer |
| 78 | BE 64-bit Unsigned Integer | A big-endian 64-bit unsigned integer |
| 79 | AffineTransformF64 | A block of data representing a 3x3 transformation matrix. It has the structure: `struct { BEFloat64 matrix[3][3]; }` |

The sorting variant of text is used for languages in which sorting is not evident from the written form (for example, some forms of Asian languages). In these cases, the sorting can only be performed by a human who can identify the actual words by understanding the context. For these languages, an alternative form of the same information can be stored using a different representation of the same text which can be machine sorted. This alternative representation is still sorted according to the sort rules of the language in question, as defined for the text system in use (for example, Unicode). In general, a simple lexical sorting which compares the values of the characters alone is not sufficient.

## See Also

- [Extensibility](extensibility.md)
  Avoid issues building extensibility into your file.
- [Localization list sets](localization_list_sets.md)
  Provide metadata for more than one country or language.
- [Type indicator](type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Locale indicator](locale_indicator.md)
  A four-byte value that indicates a locale.
- [Data ordering](data_ordering.md)
  Represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data.
- [Location metadata](location_metadata.md)
  Storing the location coordinates, as well as several auxiliary pieces of information about a location, as metadata.
- [QuickTime metadata keys](quicktime_metadata_keys.md)
  Use QuickTime keys to hold data in a Metadata atom.
- [Direction definition](direction_definition.md)
  Define a direction in metadata keys.
- [Metadata handling](appendix_d_metadata_handling.md)
  Handling metadata in other file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/well-known_types)*