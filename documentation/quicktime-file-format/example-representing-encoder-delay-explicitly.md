# Representing encoder delay explicitly

**Framework**: Quicktime File Format

Review an example that represents the temporal position of 5 seconds of 48kHz PCM audio encoded in a 48kHz AAC sound track.

#### Overview

Consider the following example of a typical case of PCM source sound data to be encoded as AAC:

The goal is to represent the temporal position of 5 seconds of 48kHz PCM audio encoded in a 48kHz AAC sound track. Assume a media timescale of 48000 and an encoder delay of 2112. For convenience, assume a movie timescale of 48000 as well.

#### Audio Data

Source PCM audio data prior to encoding:

- Sample rate: 48000 per second
- Sample count: 240000 PCM samples (5 seconds)
- Duration in timescale ticks: 240000 (with media timescale the same as sample rate)

AAC in the encoded sound track:

- Encoder delay: 2112 audio samples
- Samples per AAC packet: 1024
- Decoder delay: 1024 samples (or 1 AAC packet)
- Number of AAC packets: 237 (=((2112+240000) / 1024) rounded up to an integer value)
- Sample count: 242688 (= 237 * 1024)
- Remainder samples: 576 (= 242688 - (2112 + 240000))

The transformation from source PCM to encoded AAC results in a sound track with 237 AAC media samples corresponding to 242688 PCM audio samples if decoded and presented in its entirety. Of that total, only 240000 audio samples of source starting at sample offset 2112 (skipping the first 2111 samples) are to be presented. From this, the edit list atom and sample group atom described in the Track structures section below are used to represent the encoder delay.

#### Track Structures

Based on the Audio data section above, the following [`Edit list atom ('elst')`](edit_list_atom.md) and [`Sample group description atom ('sgpd')`](sample_group_description_atom.md) are used to represent the encoder delay.

The edit list atom contains this data:

- [`Size`](edit_list_atom/size.md): `28`
- [`Type`](edit_list_atom/type.md): `‘elst’`
- [`Version`](edit_list_atom/version.md): `0`
- [`Flags`](edit_list_atom/flags.md): `0`
- [`Number of entries`](edit_list_atom/number_of_entries.md): `1`

The edit list atom contains this [`Edit list table`](edit_list_atom/edit_list_table.md) data:

- Track duration: `240000` (source duration)
- Media time: `2112` (accounts for the encoder delay)
- Media rate: `1.0`

> **Note**: For this example, the conventional encoder delay value of 2112 audio samples has been used. Alternative encoder delay values can also be explicitly represented with this mechanism, depending upon codec implementation.

The [`Sample group description atom ('sgpd')`](sample_group_description_atom.md) contains this data:

- [`Size`](sample_group_description_atom/size.md): `26`
- [`Type`](sample_group_description_atom/type.md): `‘sgpd’`
- [`Version`](sample_group_description_atom/version.md): `1`
- [`Flags`](sample_group_description_atom/flags.md): `0`
- [`Grouping type`](sample_group_description_atom/grouping_type.md): `‘roll’`
- [`Default length`](sample_group_description_atom/default_length.md): `2`
- [`Entry count`](sample_group_description_atom/entry_count.md): `1`

The sample group description atom contains this [`Payload data`](sample_group_description_atom/payload_data.md):

- payload data: `-1`

> **Note**: Recall that the payload data value could be an alternative value, depending upon the particular codec in use. `-1` is typical for current AAC codecs.

And the [`Sample-to-group atom ('sbpd')`](sample-to-group_atom.md) contains this data:

- [`Size`](sample-to-group_atom/size.md): `22`
- [`Type`](sample-to-group_atom/type.md): `‘sbgp’`
- [`Version`](sample-to-group_atom/version.md): `0`
- [`Flags`](sample-to-group_atom/flags.md): `0`
- [`Grouping type`](sample-to-group_atom/grouping_type.md): `‘roll’`
- [`Entry count`](sample-to-group_atom/entry_count.md): `1`

The sample-to-group atom contains this [`Table data`](sample-to-group_atom/table_data.md):

- Sample count: `237` (number of AAC packets representing the encoder delay, original audio samples, and remainder audio samples)
- Group description index: `1` (corresponds to first and only entry in the sample group description atom’s payload data table for these sample units)

Other things to note from this example:

- You cannot use the edit list by itself to determine the encoder delay or remainder sample count. The sample group atoms provide the encoder delay. The placement of the end of the edit in a compressed audio packet allows calculation of the remainder samples.
- If the encoder delay was the theoretical minimum for AAC of 1024, then the media time field value in the edit list table data shown in this example would be 1024, not 2112.

## See Also

- [AAC encoding background](background_aac_encoding.md)
  AAC requires data beyond the source PCM audio samples in order to correctly encode and decode audio samples due to the nature of the encoding algorithm.
- [The timing and synchronization problem](the_timing_and_synchronization_problem.md)
  Trim the silent priming samples to preserve correct synchronization.
- [Historical solution for implicit encoder delay](historical_solution_implicit_encoder_delay.md)
  Implicit encoder delay uses the most common delay of 2112 audio samples.
- [Using track structures to represent encoder delay explicitly](using_track_structures_to_represent_encode_delay_explictly.md)
  Represent encoder delay explicitly with an edit list atom and sample group structures.
- [Representing encoder delay with track structures](summary_using_track_structures_to_represent_encoder_delay.md)
  Use sample group structures to represent encoder delay for AAC sound tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/example_representing_encoder_delay_explicitly)*