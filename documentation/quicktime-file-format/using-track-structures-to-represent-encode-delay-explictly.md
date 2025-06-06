# Using track structures to represent encoder delay explicitly

**Framework**: QuickTime File Format

Represent encoder delay explicitly with an edit list atom and sample group structures.

#### Overview

In QuickTime movie files (.mov) and related MPEG-4 files, AAC encoded audio is carried in a sound track as a series of media samples—each media sample corresponding to an AAC encoded audio packet. A track uses an edit list (see [`Edit list atom ('elst')`](edit_list_atom.md)) to indicate the range of time from the media samples to present. The edit list atom along with additional atoms known as Sample Group Structures, introduced in the Sample group structures section below, can now be used to explicitly represent encoder delay.

> ❗ **Important**: A complete implementation using the sample group structures is required to explicitly represent the placement of the source signal in the encoded track. An incomplete implementation will result in unspecified interpretation by Apple software and tools. In the absence of the sample group structures, the classic solution of expecting an implicit encoding delay of 2112 samples and the edit list to start at the beginning of encoder delay will be assumed as described in the previous section.

A complete implementation using the sample group structures is required to explicitly represent the placement of the source signal in the encoded track. An incomplete implementation will result in unspecified interpretation by Apple software and tools. In the absence of the sample group structures, the classic solution of expecting an implicit encoding delay of 2112 samples and the edit list to start at the beginning of encoder delay will be assumed as described in the previous section.

#### Edit List Atom

See [`Edit atom ('edts')`](edit_atom.md) and [`Edit list atom ('elst')`](edit_list_atom.md) for details of edit lists in track atom structures.

A sound track of AAC encoded audio uses an edit list to indicate the placement of the source signal in the time represented by the encoded AAC packets. The media time field of the edit list must indicate the first sample to be presented and will correspond in time to the first audio sample following the encoder delay in that track. The edit list track duration field should be set to the duration of the source waveform in media samples. The edit list must not extend into the encoder delay or into any remainder samples of the encoded sound track. Note that for a single waveform encoded into a sound track, the sound track requires only a single edit list atom with one entry.

> **Note**: Track duration uses the movie timescale instead of the media timescale used by media time. If the media timescale and movie timescale differ, the track duration may not be sample accurate.

Track duration uses the movie timescale instead of the media timescale used by media time. If the media timescale and movie timescale differ, the track duration may not be sample accurate.

#### Sample Group Structures

> **Note**: This implementation of sample group structures in QuickTime is designed to be compatible with the ISO Sample Group Structures definition and allow for future generalization. A full description of ISO 14996-12 Sample Group Structures is not required in order to provide explicit encoder delay representation. A short description of the more general characteristics of these structures is included in the descriptions below, followed by the information required for use with QuickTime.

This implementation of sample group structures in QuickTime is designed to be compatible with the ISO Sample Group Structures definition and allow for future generalization. A full description of ISO 14996-12 Sample Group Structures is not required in order to provide explicit encoder delay representation. A short description of the more general characteristics of these structures is included in the descriptions below, followed by the information required for use with QuickTime.

Sample group structures of roll-group type with a constant roll distance are used to represent decoder dependencies for AAC encoded media. The sample group structures are intended to serve two purposes:

- To indicate the amount of decoder delay in AAC packets
- To signal to readers parsing QuickTime movies that the sound track includes explicit information for encoder delay and remainder samples for the AAC packets encoded in the file

> **Note**: The effect of using sample group structures in the track in this manner is that the edit list’s media time and track duration fields do not include encoder delay, as specified above in [`Edit list atom ('elst')`](edit_list_atom.md).

The effect of using sample group structures in the track in this manner is that the edit list’s media time and track duration fields do not include encoder delay, as specified above in [`Edit list atom ('elst')`](edit_list_atom.md).

Two sample group structure atoms are used to represent the amount of encoder delay and remainder samples which must be trimmed: [`Sample group description atom ('sgpd')`](sample_group_description_atom.md) and [`Sample-to-group atom ('sbpd')`](sample-to-group_atom.md).

## Topics

### Sample group structures
- [Sample group description atom ('sgpd')](sample_group_description_atom.md)
  An atom that gives information about the characteristics of sample groups.
- [Sample-to-group atom ('sbpd')](sample-to-group_atom.md)
  An atom that associates a sample with a sample group description.

## See Also

- [AAC encoding background](background_aac_encoding.md)
  AAC requires data beyond the source PCM audio samples in order to correctly encode and decode audio samples due to the nature of the encoding algorithm.
- [The timing and synchronization problem](the_timing_and_synchronization_problem.md)
  Trim the silent priming samples to preserve correct synchronization.
- [Historical solution for implicit encoder delay](historical_solution_implicit_encoder_delay.md)
  Implicit encoder delay uses the most common delay of 2112 audio samples.
- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)
  Review an example that represents the temporal position of 5 seconds of 48kHz PCM audio encoded in a 48kHz AAC sound track.
- [Representing encoder delay with track structures](summary_using_track_structures_to_represent_encoder_delay.md)
  Use sample group structures to represent encoder delay for AAC sound tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/using_track_structures_to_represent_encode_delay_explictly)*