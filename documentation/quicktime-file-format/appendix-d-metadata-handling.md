# Metadata handling

**Framework**: QuickTime File Format

Handling metadata in other file formats.

#### Overview

This section describes how metadata is handled when QuickTime imports other file formats. For more information about metadata, refer to [`Metadata atoms and types`](metadata_atoms_and_types.md) and [`Compressed movie resources`](compressed_movie_resources.md).

Each section includes a table with specific details on the following, where applicable:

- The format supported by QuickTime — for example, the movie import component or the graphics import component.
- The Macintosh file type — for example, `'Mp3 '`.
- File name extensions — for example, `.mp3`.
- Specific details for metadata handling — for example, all Microsoft-defined “tombstone” data is transferred to the imported movie’s user data. Metadata fields that have QuickTime equivalents are mapped as follows.
- Software required — for example, QuickTime 3 or later.

## Topics

### Handling metadata
- [Digital video file formats](digital_video_file_formats.md)
- [Digital audio file formats](digital_audio_file_formats.md)
- [Still image file formats](still_image_file_formats.md)
- [Animation and 3D file formats](animation_and_3d_file_formats.md)

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
- [Direction definition](direction_definition.md)
  Define a direction in metadata keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/appendix_d_metadata_handling)*