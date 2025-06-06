# Extensibility

**Framework**: QuickTime File Format

Avoid issues building extensibility into your file.

#### Overview

In order to allow metadata to be rewritten easily and without the need to rewrite the entire QuickTime movie file, free space atoms may occur anywhere in the definition of the metadata atom between the positions of other atoms contained by the metadata atom. Free space atoms may not be inserted between items in the metadata item list atom or within atoms in the metadata item list atom. This restriction on free space atom definition avoids the risk of confusing a free space atom with a meaning of a `‘free’` identifier or a value atom of type `‘free’` defined in the context of the metadata atom structure.

Similarly, UUID atoms for specific extensions may be placed in any position where a succession of atoms is permitted. Note that UUID atoms should not be created for atoms already defined using four-character codes.

Unrecognized atoms (that is, those atoms whose types not defined in the context of the metadata atom structure and are contained within the metadata item list atom) are ignored.

## See Also

- [Localization list sets](localization_list_sets.md)
  Provide metadata for more than one country or language.
- [Type indicator](type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Locale indicator](locale_indicator.md)
  A four-byte value that indicates a locale.
- [Data ordering](data_ordering.md)
  Represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/extensibility)*