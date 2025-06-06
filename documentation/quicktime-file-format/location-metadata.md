# Location metadata

**Framework**: QuickTime File Format

Storing the location coordinates, as well as several auxiliary pieces of information about a location, as metadata.

#### Overview

Many systems have the ability to detect or establish their position in a coordinate reference system. The specification “ISO 6709:2008 Standard representation of geographic point location by coordinates” describes one way of storing such information. One of the common systems is the Global Positioning System (GPS) developed by the US Department of Defense. Other systems include the ability of some cellular telephone systems to triangulate the position of cell-phones, and the possibility that IEEE 802.11 Wireless Base Stations are tagged with their position (whereupon mobile units that can ‘see’ their signal can establish that they are probably ‘near’ that location).

This support is increasingly common in still and movie cameras, or composite devices (such as camera-phones) that can function as cameras.

Use the defined keys to store the location coordinates as metadata, as well as several auxiliary pieces of information about a location. For all the location metadata keys defined in this specification, the Metadata atom handler-type should be `‘mdta’`. See the com.apple.quicktime.location.ISO6709 entry in the [`QuickTime metadata keys`](quicktime_metadata_keys.md) table for a description of the main location metadata key, and the additional table describing auxiliary location metadata keys.

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
- [QuickTime metadata keys](quicktime_metadata_keys.md)
  Use QuickTime keys to hold data in a Metadata atom.
- [Direction definition](direction_definition.md)
  Define a direction in metadata keys.
- [Metadata handling](appendix_d_metadata_handling.md)
  Handling metadata in other file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/location_metadata)*