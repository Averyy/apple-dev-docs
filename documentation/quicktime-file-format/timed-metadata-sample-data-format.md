# Timed metadata sample data format

**Framework**: Quicktime File Format

A concatenation of one or more atoms that structure a timed metadata media sample.

#### Overview

A timed metadata media sample is structured as a concatenation of one or more atoms. Typically each atom will contain a metadata value corresponding to a key signaled in the timed metadata sample description.

If no value for a particular key is present in the timed metadata media sample at a given time, the interpretation should be that there is no metadata of that type at the specified time. Timed metadata values for that key for other times (such as from a previous timed metadata media sample) should not be interpreted as applying to the given time.

> **Note**: All metadata samples are marked as sync samples.

If no values for any key are present for a time range, one approach is to include a `“NULL”` or unreferenced metadata media sample (see Unreferenced or `NULL` timed metadata sample data in [`Constant-size timed metadata sample data`](constant-size_timed_metadata_sample_data.md)) for the time range. A zero-byte timed metadata media sample cannot be used because all sample sizes must be one or more bytes. Alternatively, “empty edit” track edit list entries could be used to indicate there is no metadata for a range of movie time.

In general, however, it is preferable to include a NULL metadata media sample data instead of using a track edit with an empty edit list to indicate the absence of metadata. Some readers may be unprepared for complex edits (more than one edit list entry and/or a non-contiguous presentation media time).

#### Timed Metadata Media Sample Structure

The timed metadata media sample data consists of some number of concatenated atoms. A `local_key_id` value defines the atom type for each of the atoms. The `local_key_id` value corresponds to a `local_key_id` defined for a metadata key atom in the metadata key table atom for the timed metadata sample. No special interpretation is made regarding the 32-bit value of `local_key_id`. Its interpretation is based solely on what is defined in the corresponding metadata key of the associated metadata sample description.

The `local_key_id` value `0` is reserved and can be used as a placeholder atom in the media sample. Such an atom has no prescribed contents. (See [`Metadata key atom`](metadata_key_atom.md).)

The `local_key_id` value `0xFFFFFFFF` is also reserved. In the future, this may be documented to hold a particular payload. This `local_key_id` should not be used or interpreted otherwise. If a reader finds an atom with `local_key_id` of `0xFFFFFFFF` and does not understand its format, the atom should be ignored.

A timed metadata media sample may contain atoms with types other than those defined in the metadata key table atom and other than the two reserved values `0` and `0xFFFFFFFF`. Although this practice is discouraged, any instances of such atoms may be interpreted according to their conventional meaning (such as `‘free’`) or in a private way so long as they are not advertised as keys.

Example:

Consider the metadata format for a geographic point location using coordinates as defined in ISO-6709. The timed metadata media sample created for this data might have a `local_key_id` value of `‘wher’` and the resulting metadata sample would contain the information (such as “+27.5916+086.5640+8850/”) in a corresponding `‘wher’` atom. There is no interpretation of this atom type or a requirement that it be `‘wher’`.

## See Also

- [Overview of timed metadata](overview_of_timed_metadata.md)
  Synchronize metadata references to media tracks for particular media time periods with timed metadata.
- [Timed metadata sample description](timed_metadata_sample_descriptions.md)
  An atom that defines how to interpret timed metadata media samples.
- [Constant-size timed metadata sample data](constant-size_timed_metadata_sample_data.md)
  Create metadata tracks with samples that have the same size.
- [Combining multiple streams of metadata into the same track](combining_multiple_streams_of_metadata_into_the_same_track.md)
  Introduce new metadata samples with the union of all metadata values from combined tracks.
- [Movie-level relationships among tracks](movie-level_relationships_among_tracks.md)
  Handling tracks with more than one associated metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timed_metadata_sample_data_format)*