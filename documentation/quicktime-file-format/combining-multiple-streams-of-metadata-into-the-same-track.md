# Combining multiple streams of metadata into the same track

**Framework**: Quicktime File Format

Introduce new metadata samples with the union of all metadata values from combined tracks.

#### Overview

Because two “streams” or tracks of metadata values might occur where the time ranges for one stream does not coincide with those of the other stream, a convention is recommended if both streams of metadata values are combined into a single new metadata track (typically because of some production process). At any point in the timeline where a metadata value comes into scope or goes out of scope, new metadata samples should be introduced with the union of all metadata values present for the time range, replacing the existing overlapped samples for that portion of the media time range.

For example, this figure shows the results of combining the metadata from two metadata tracks:

![A diagram with two axes, where the horiztonal axis shows time marked with t0, t1, t2, and t3, and the vertical axis has labels for tracks, which are Metadata 1, Metadata 2, and Metadata track (bundled). A track labeled A is at the top of the diagram, aligned with the label Metadata 1, and extends from t0 to t2. A track labeled B, aligned with the label Metadata 2, is below the track labeled B, extends from t1 to t3, and has an arrow pointing to the track labeled {A, B} below it. There are three tracks below the tracked labeled B, all aligned with the label Metadata track (bundled). The track labeled A extends from t0 to t1. The track labeled {A, B} extends from t1 to t2. The track labeled B extends from t2 to t3.](https://docs-assets.developer.apple.com/published/ffc09588348aaf5d109d93ef8dc2b9d6/combining-metadata-streams%402x.png)

> **Note**: The combined timed metadata media samples from time t1 to t2 contain both the A and B metadata values. This is done so that for any time t, it is possible to determine all applicable metadata values without needing to scan through all timed metadata media tracks in backward or forward directions.

In the new combined track, a single timed metadata sample description containing the keys A and B may be used. Creating sample descriptions for each combination (A, B, {A,B}) is possible but discouraged as this makes the determination of whether a key is in the tracks more complex.

## See Also

- [Overview of timed metadata](overview_of_timed_metadata.md)
  Synchronize metadata references to media tracks for particular media time periods with timed metadata.
- [Timed metadata sample description](timed_metadata_sample_descriptions.md)
  An atom that defines how to interpret timed metadata media samples.
- [Timed metadata sample data format](timed_metadata_sample_data_format.md)
  A concatenation of one or more atoms that structure a timed metadata media sample.
- [Constant-size timed metadata sample data](constant-size_timed_metadata_sample_data.md)
  Create metadata tracks with samples that have the same size.
- [Movie-level relationships among tracks](movie-level_relationships_among_tracks.md)
  Handling tracks with more than one associated metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/combining_multiple_streams_of_metadata_into_the_same_track)*