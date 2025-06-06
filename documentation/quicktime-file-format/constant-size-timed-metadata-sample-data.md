# Constant-size timed metadata sample data

**Framework**: Quicktime File Format

Create metadata tracks with samples that have the same size.

#### Overview

Some clients using timed metadata tracks may prefer to create metadata tracks with samples that have the same size. Two approaches are described here.

In one approach, the metadata written might contain a fixed number of fixed-sized metadata values (for example, integers or statically sized structures). If one or more values are not used, atoms corresponding to unused values can have their `local_key_id` value set to an unreferenced value (such as `0`).

In the second approach, the size of individual metadata values may vary. It is possible to create constant-sized metadata samples by determining a maximum timed metadata media sample size and using unreferenced atoms to add up to this size. The approach is:

1. Determine the constant metadata media atom size desired.
2. Fill in the atoms holding metadata values (see the Timed metadata media sample structure example in [`Timed metadata sample data format`](timed_metadata_sample_data_format.md)).
3. If necessary, add one or more unreferenced atoms to reach the constant metadata media atom size.

> **Note**: Because an atom has a minimum size of 8 bytes, the sum of the sizes of contained timed metadata media samples either must equal the target constant metadata media atom size, or must be 8 or more bytes smaller than the target constant atom size to allow for one or more padding atoms.

#### Unreferenced or Null Timed Metadata Sample Data

A timed metadata sample is identified by its derived atom type supplied by the `local_key_id` value in the metadata sample description’s key tables. An unreferenced metadata atom, meaning one which is not identified in the key tables and not having the reserved value `0xFFFFFFFF`, can be considered a “NULL” metadata media sample since its type is unknown in the local namespace and its data will not be interpreted. There is no prescribed atom type indicating a NULL metadata sample although a type of `0` is recommended, as mentioned in the [`Metadata key atom`](metadata_key_atom.md) description. Using unreferenced atoms presents a useful way to supply padding when structuring a track for constant-sized metadata sample data or when there are runs of no-metadata interspersed with runs of metadata in a given track, instead of using multiple track edits.

## See Also

- [Overview of timed metadata](overview_of_timed_metadata.md)
  Synchronize metadata references to media tracks for particular media time periods with timed metadata.
- [Timed metadata sample description](timed_metadata_sample_descriptions.md)
  An atom that defines how to interpret timed metadata media samples.
- [Timed metadata sample data format](timed_metadata_sample_data_format.md)
  A concatenation of one or more atoms that structure a timed metadata media sample.
- [Combining multiple streams of metadata into the same track](combining_multiple_streams_of_metadata_into_the_same_track.md)
  Introduce new metadata samples with the union of all metadata values from combined tracks.
- [Movie-level relationships among tracks](movie-level_relationships_among_tracks.md)
  Handling tracks with more than one associated metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/constant-size_timed_metadata_sample_data)*