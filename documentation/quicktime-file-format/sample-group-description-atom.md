# Sample group description atom ('sgpd')

**Framework**: Quicktime File Format  
**Kind**: class

An atom that gives information about the characteristics of sample groups.

## Mentions

- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)

#### Overview

Sample group description atoms give information about the characteristics of sample groups. The sample group description atom has an atom type of `‘sgpd’`.

In a general case, each instance of a sample group description atom has a type code that distinguishes different sample groupings. There can be multiple instances of this atom if there is more than one sample grouping for the samples in a track. At most one instance of a sample group description with a particular grouping type exists in a track. An associated sample-to-group atom has the same value associated with that grouping type. The information or “payload data” is stored in the sample group description atom, after the entry count, as an array of entries for which the meanings vary according to the characteristics of grouping type.

For use in AAC encoder delay representation, there is one instance of a sample group description atom in a given QuickTime sound track with grouping type `‘roll’`. The specifics for audio data (`AudioRollRecovery()`) are used and articulate the rolling decode dependency. Because the sample group description atom for this purpose is describing the entirety of the AAC audio stream, the payload data field resolves to a single signed 16-bit integer representing the roll distance, which is set to `-1`. In other words, one AAC packet (1024 encoded PCM audio samples) preceding the media sample is indicated as being of the same type as the encoded source data, allowing the decode transform to operate over the required two AAC packets for the first media sample specified in the edit list.

> **Note**: The payload data value (roll distance in this use) of `-1` is a typical value for existing AAC codecs, but the payload data can have other values. Codecs could use alternative values depending upon their implementation details.

The layout of the sample group atom is as follows:

| Sample group description atom | Bytes |
| --- | --- |
| [`Size`](sample_group_description_atom/size.md) | 4 |
| [`Type`](sample_group_description_atom/type.md) = `'sgpd'` | 4 |
| [`Version`](sample_group_description_atom/version.md) | 1 |
| [`Flags`](sample_group_description_atom/flags.md) | 3 |
| [`Grouping type`](sample_group_description_atom/grouping_type.md) | 4 |
| [`Default length`](sample_group_description_atom/default_length.md) | 4 |
| [`Entry count`](sample_group_description_atom/entry_count.md) | 4 |
| [`Payload data`](sample_group_description_atom/payload_data.md) | variable |

## Topics

### Data fields
- [Size](sample_group_description_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sample group description atom.
- [Type](sample_group_description_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sample_group_description_atom/version.md)
  A 1-byte specification of the version of this sample group description.
- [Flags](sample_group_description_atom/flags.md)
  A 3-byte reserved space.
- [Grouping type](sample_group_description_atom/grouping_type.md)
  A 32-bit integer that identifies the grouping type of this sample group description.
- [Default length](sample_group_description_atom/default_length.md)
  A 32-bit integer indicating the length of the group entry in the payload data.
- [Entry count](sample_group_description_atom/entry_count.md)
  A 32-bit integer giving the number of entries in the payload data field.
- [Payload data](sample_group_description_atom/payload_data.md)
  A 16-bit signed integer giving the roll distance.

## See Also

- [Sample-to-group atom ('sbpd')](sample-to-group_atom.md)
  An atom that associates a sample with a sample group description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_group_description_atom)*