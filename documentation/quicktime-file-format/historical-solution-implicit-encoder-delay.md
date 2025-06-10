# Historical solution for implicit encoder delay

**Framework**: QuickTime File Format

Implicit encoder delay uses the most common delay of 2112 audio samples.

#### Overview

In the original AAC implementations, as stated above the common practice was to propagate the encoder delay in the provided AAC bitstream. With these original implementations, the most common delay used was 2112 audio samples. An AAC bitstream would therefore generally be 3 AAC packets larger than what was theoretically required by the original signal.

A playback implementation would then need to discard these first 2112 silent samples from the decoded output since they contain none of the original source audio data; these samples are an artifact of the encoding/decoding process.

Because there was no explicit way to represent the extent of the priming or remainder samples with the first implementations of an AAC bitstream, QuickTime assumed that the AAC bitstream always contained an encoding delay with a fixed number of samples. A fixed encoder delay of 2112 samples was chosen because at that time this was the common encoding delay used, for various reasons, by most of the shipping implementations of AAC encoders (commercial and otherwise).

> **Note**: The lack of explicit representation for encoder delay and remainder samples is not a problem unique to AAC encoding. With MPEG-4 and ADTS/MPEG-2 bitstreams and file containers, there is still no satisfactory, explicit representation for either the encoder delay or remainder samples. MP3 also has these data dependencies and delays in its bitstream, as do proprietary codecs such as AC-3 and others. In all of these cases the conventional solution is as described above: an implicit assumption is made about the size of the encoder delay and the playback engine is required to trim this designated number of samples from its output at the start of playback. Adjustments must also be made for the remainder samples as required.

In summary, the historical technique to handle the timing and synchronization problem is to assume an implicit 2112 sample standard encoder delay in AAC data streams and indicate start time—the first media sample or AAC packet—in the sound track edit list (see [`Edit list atom ('elst')`](edit_list_atom.md)) at the start of encoder delay.

## See Also

- [AAC encoding background](background_aac_encoding.md)
  AAC requires data beyond the source PCM audio samples in order to correctly encode and decode audio samples due to the nature of the encoding algorithm.
- [The timing and synchronization problem](the_timing_and_synchronization_problem.md)
  Trim the silent priming samples to preserve correct synchronization.
- [Using track structures to represent encoder delay explicitly](using_track_structures_to_represent_encode_delay_explictly.md)
  Represent encoder delay explicitly with an edit list atom and sample group structures.
- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)
  Review an example that represents the temporal position of 5 seconds of 48kHz PCM audio encoded in a 48kHz AAC sound track.
- [Representing encoder delay with track structures](summary_using_track_structures_to_represent_encoder_delay.md)
  Use sample group structures to represent encoder delay for AAC sound tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/historical_solution_implicit_encoder_delay)*