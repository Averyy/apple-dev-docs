# Overview of timed metadata

**Framework**: QuickTime File Format

Synchronize metadata references to media tracks for particular media time periods with timed metadata.

#### Overview

A timed metadata track synchronizes metadata references to media tracks for particular media time periods through the track reference, edit, and edit list structures. It is a specialization of the track structure which uses the base media information atom of type `‘minf’`, and a track handler type value set to `‘meta’`. The base media information atom contains the generic media header atom of type `‘gmhd’`.

Because a metadata track is neither visual nor aural, the following track properties should have these values:

- Track width and track height each set to `0`.
- The track volume set to `0`.
- The track matrix set to the identity matrix.

A QuickTime movie can contain none, one, or several timed metadata tracks. Timed metadata tracks can refer to multiple tracks. Metadata tracks are linked to the tracks they describe using a track-reference of type `‘cdsc’`. The metadata track holds the `‘cdsc’` track reference. If a metadata track describes characteristics of the entire movie, there should be no track reference of type `'cdsc'` between it and another track. These metadata tracks can be considered to hold global metadata for the movie.

Using a timed metadata track, any form of descriptive metadata that changes over time can be linked to a range of media times for which it is valid. Examples of timed metadata can include:

- Faces detected in the scene
- Location-based information (such as GPS)
- Camera aperture and other changing camera-related information
- Copyright and other information for individual clips edited together
- Information such as scene changes and actor names added to the movie in production

As with other tracks, each metadata sample is associated with a single timed metadata sample description. This sample description signals information needed to interpret the data in the metadata sample in a way that is analogous to how a video track’s video sample atom indicates that video samples contain H.264 compressed sample data of particular dimensions.

Zero, one, or many metadata values can be associated with a range of media time in the track. The accommodation for no metadata values for a time allows runs of time with metadata interspersed with runs of time with no metadata. Because the timed metadata is organized as a track, it is also possible to use track edits to indicate the absence of metadata. For some situations, however, it would be better to include metadata samples that themselves carry no metadata values.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/overview_of_timed_metadata)*