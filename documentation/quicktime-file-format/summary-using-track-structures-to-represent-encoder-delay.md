# Representing encoder delay with track structures

**Framework**: QuickTime File Format

Use sample group structures to represent encoder delay for AAC sound tracks.

#### Overview

When using sample group structures in representing encoder delay for AAC sound tracks:

- Include a version 1 sample group description atom with grouping type set to `‘roll’`. Set default length to `2` (bytes) for audio entries. Follow that with the payload data: the typical value is `-1`, meaning one preceding AAC packet, which is the theoretical minimum decoder delay of 1024 samples.
- Include a version 0 sample-to-group atom with a `'roll'` grouping type. By including this, you associate the AAC packets with the corresponding sample group description atom. All AAC packets including the encoder delay must be associated with the sample group in the table data’s sample count field. Typically, the sample count for this sample-to-group atom’s table data corresponds with the number of media samples in the track.

These two sample group structure atoms in addition to the edit list atom, properly composed, form a complete implementation to explicitly represent the temporal position of the source audio samples in an AAC encoded track.

## See Also

- [AAC encoding background](background_aac_encoding.md)
  AAC requires data beyond the source PCM audio samples in order to correctly encode and decode audio samples due to the nature of the encoding algorithm.
- [The timing and synchronization problem](the_timing_and_synchronization_problem.md)
  Trim the silent priming samples to preserve correct synchronization.
- [Historical solution for implicit encoder delay](historical_solution_implicit_encoder_delay.md)
  Implicit encoder delay uses the most common delay of 2112 audio samples.
- [Using track structures to represent encoder delay explicitly](using_track_structures_to_represent_encode_delay_explictly.md)
  Represent encoder delay explicitly with an edit list atom and sample group structures.
- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)
  Review an example that represents the temporal position of 5 seconds of 48kHz PCM audio encoded in a 48kHz AAC sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/summary_using_track_structures_to_represent_encoder_delay)*