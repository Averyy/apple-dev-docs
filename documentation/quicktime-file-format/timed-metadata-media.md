# Timed metadata media

**Framework**: QuickTime File Format

Store timed metadata in QuickTime movies with a track structure.

#### Overview

A track structure is used to store timed metadata in QuickTime movies. This section provides an overview of the timed metadata track structure, and describes the timed metadata sample descriptions and the storage format of timed metadata media samples. The timed metadata track structure has a media type of `‘meta’`.

## Topics

### Storing timed metadata media
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
- [Movie-level relationships among tracks](movie-level_relationships_among_tracks.md)
  Handling tracks with more than one associated metadata track.

## See Also

- [Timecode media](timecode_media.md)
  Store time code data in QuickTime movies with timecode media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timed_metadata_media)*