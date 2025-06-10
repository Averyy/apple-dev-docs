# Timed metadata sample description

**Framework**: QuickTime File Format

An atom that defines how to interpret timed metadata media samples.

#### Overview

The timed metadata sample description contains information that defines how to interpret timed metadata media samples. This sample description is based on the standard sample description header, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

The metadata sample description is a derived sample description format which describes metadata values represented in atoms. It may also include other atoms not holding metadata values.

Zero, one, or more values may be carried in a metadata sample description for a particular time.

The data format field contains the format of the timed metadata media, which is set to `'mebx'`.

> **Note**: Other forms of timed metadata media are not described here. They would be indicated by an alternative type code in the place of `‘mebx’`.

The metadata sample description must contain a metadata key table atom and optionally contains a bit rate atom following the standard sample description atom header, defined below. Other atoms may be introduced in the future.

## Topics

### Describing timed metadata
- [Metadata key table atom ('keys')](metadata_key_table_atom.md)
  An atom that contains a table of keys and mappings to payload data in the corresponding timed metadata media samples.
- [Bit rate atom ('btrt')](bit_rate_atom.md)
  An atom that signals the bit rate information of a stream.
- [Metadata key atom](metadata_key_atom.md)
  An atom that contains a key that corresponds to the timed metadata track containing it.
- [Metadata key declaration atom ('keyd')](metadata_key_declaration_atom.md)
  An atom that holds the key namespace and key value of that namespace for the given values.
- [Metadata datatype definition atom ('dtyp')](metadata_datatype_definition_atom.md)
  An atom you use to specify the data type of the metadata key atom’s value.
- [Metadata locale atom ('loca')](metadata_locale_atom.md)
  An atom that tags a metadata value with a locale.

## See Also

- [Overview of timed metadata](overview_of_timed_metadata.md)
  Synchronize metadata references to media tracks for particular media time periods with timed metadata.
- [Timed metadata sample data format](timed_metadata_sample_data_format.md)
  A concatenation of one or more atoms that structure a timed metadata media sample.
- [Constant-size timed metadata sample data](constant-size_timed_metadata_sample_data.md)
  Create metadata tracks with samples that have the same size.
- [Combining multiple streams of metadata into the same track](combining_multiple_streams_of_metadata_into_the_same_track.md)
  Introduce new metadata samples with the union of all metadata values from combined tracks.
- [Movie-level relationships among tracks](movie-level_relationships_among_tracks.md)
  Handling tracks with more than one associated metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timed_metadata_sample_descriptions)*