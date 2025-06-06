# Data ordering

**Framework**: QuickTime File Format

Represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data.

#### Overview

Multiple values for the same tag represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data. For example, an artist name may be supplied in three ways:

- as a large JPEG of their signature
- as a smaller ‘thumbnail’ JPEG of their signature
- as text

An application may then choose the variation of the the artist name to display based on the size it needs.

Data must be ordered in each item from the most-specific data to the most general. An application may, if it wishes, stop ‘searching’ for a value once it finds a value that it can display (it has an acceptable locale and type).

## See Also

- [Extensibility](extensibility.md)
  Avoid issues building extensibility into your file.
- [Localization list sets](localization_list_sets.md)
  Provide metadata for more than one country or language.
- [Type indicator](type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Locale indicator](locale_indicator.md)
  A four-byte value that indicates a locale.
- [Well-known types](well-known_types.md)
  Basic data types.
- [Location metadata](location_metadata.md)
  Storing the location coordinates, as well as several auxiliary pieces of information about a location, as metadata.
- [QuickTime metadata keys](quicktime_metadata_keys.md)
  Use QuickTime keys to hold data in a Metadata atom.
- [Direction definition](direction_definition.md)
  Define a direction in metadata keys.
- [Metadata handling](appendix_d_metadata_handling.md)
  Handling metadata in other file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/data_ordering)*