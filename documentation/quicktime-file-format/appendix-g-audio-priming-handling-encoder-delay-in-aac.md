# Audio priming-handling encoder delay in AAC

**Framework**: QuickTime File Format

Position a source audio signal in a sound track to handle encoder delay.

#### Overview

This section describes temporal positioning of a source audio signal after AAC encoding into a sound track for QuickTime media files. The mechanisms described here are specified in ISO MPEG-4 standards (ISO/IEC 14496-12, 2008) and are used here with additional constraints.

> **Note**: AAC implementations typically represent 1024 PCM audio samples in one AAC packet (synonymous in this context with a QuickTime media sample, and also referred to in ISO documents as an “access unit”). The terms “sample” and “audio sample” in this appendix are used to refer to PCM samples. For the encoded audio data, the terms “AAC packet” and QuickTime “media sample” are used.

## Topics

### Handling encoder delay
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
- [Representing encoder delay with track structures](summary_using_track_structures_to_represent_encoder_delay.md)
  Use sample group structures to represent encoder delay for AAC sound tracks.

## See Also

- [Sound sample descriptions](sound_sample_descriptions.md)
  A sound sample description contains information that defines how to interpret sound media data.
- [Sound sample description extensions](sound_sample_description_extensions.md)
  Extend sound sample descriptions by appending other atoms.
- [Sound sample data](sound_sample_data.md)
  Sound sample formats that QuickTime supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/appendix_g_audio_priming_handling_encoder_delay_in_aac)*