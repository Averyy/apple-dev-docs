# Direction definition

**Framework**: QuickTime File Format

Define a direction in metadata keys.

#### Overview

For the metadata keys which define a direction, com.apple.quicktime.direction.facing and com.apple.quicktime.direction.motion, directions are specified as a string consisting of one or two angles, separated by a slash if two occur. The first is a compass direction, expressed in degrees and decimal degrees, optionally preceded by the characters “+” or “-”, and optionally followed by the character “M”.  The direction is determined as accurately as possible; the nominal due north (zero degrees) is defined as facing along a line of longitude of the location system, unless the angle is followed by the “M” character indicating a magnetic heading. The second is an elevation direction, expressed in degrees and decimal degrees between `+90.0` and `-90.0`, with `0` being horizontal (level), `+90.0` being straight up, and `-90.0` being straight down (and for these two cases, the compass direction is irrelevant).

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
- [Well-known types](well-known_types.md)
  Basic data types.
- [Location metadata](location_metadata.md)
  Storing the location coordinates, as well as several auxiliary pieces of information about a location, as metadata.
- [QuickTime metadata keys](quicktime_metadata_keys.md)
  Use QuickTime keys to hold data in a Metadata atom.
- [Metadata handling](appendix_d_metadata_handling.md)
  Handling metadata in other file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/direction_definition)*