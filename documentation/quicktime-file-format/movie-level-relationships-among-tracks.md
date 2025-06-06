# Movie-level relationships among tracks

**Framework**: QuickTime File Format

Handling tracks with more than one associated metadata track.

#### Overview

A “presentation” track (for example, video or audio) may have more than one metadata track associated with it via `'cdsc'` type track references. The union of all metadata across those tracks should be considered the metadata for the presentation track — just as if there was a single metadata track with all the corresponding metadata.

There is a potential conflict if more than one metadata value of the same type is in the metadata tracks. In this case, the layer of the metadata tracks should be used to establish which should be used. Tracks with lesser layer values (that is, `-1` is less than `0`) take priority and their metadata values should be used. If two tracks have the same layer value, the last track in movie track order (the order of `'trak'` atoms in the `'moov'` atom) shall override metadata values from tracks earlier in order.

If a metadata track does not have a relationship to another track defined by a track reference of `‘cdsc’`, it should be considered a global metadata track — its metadata applying to the entire movie. If part of a track would apply to a presentation track and part would apply globally, the metadata should be carried in two tracks, the first referencing the presentation track and the other not referencing any track.

## See Also

- [Overview of timed metadata](overview_of_timed_metadata.md)
  Synchronize metadata references to media tracks for particular media time periods with timed metadata.
- [Timed metadata sample description](timed_metadata_sample_descriptions.md)
  An atom that defines how to interpret timed metadata media samples.
- [Timed metadata sample data format](timed_metadata_sample_data_format.md)
  A concatenation of one or more atoms that structure a timed metadata media sample.
- [Constant-size timed metadata sample data](constant-size_timed_metadata_sample_data.md)
  Create metadata tracks with samples that have the same size.
- [Combining multiple streams of metadata into the same track](combining_multiple_streams_of_metadata_into_the_same_track.md)
  Introduce new metadata samples with the union of all metadata values from combined tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie-level_relationships_among_tracks)*