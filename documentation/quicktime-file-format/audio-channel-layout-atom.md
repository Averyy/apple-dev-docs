# Audio channel layout atom ('chan')

**Framework**: Quicktime File Format  
**Kind**: class

An optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies.

#### Overview

This atom is an optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies. It is a full atom followed by a big-endian audio channel layout structure as defined by Apple’s Core Audio framework. Audio channel layouts can be applied to both compressed and uncompressed sound formats.

> **Note**: Audio channel layouts with more than two channels per track require implementation with a version 2 sound sample description.

## Topics

### Data fields
- [Size](audio_channel_layout_atom/size.md)
  An unsigned 32-bit integer holding the size of the audio channel layout atom.
- [Type](audio_channel_layout_atom/type.md)
  An unsigned 32-bit field.
- [Version](audio_channel_layout_atom/version.md)
  A 1-byte specification of the version of the audio channel layout atom.
- [Flags](audio_channel_layout_atom/flags.md)
  A 3-byte space for audio channel layout flags.
- [Audio channel layout](audio_channel_layout_atom/audio_channel_layout.md)
  An audio channel layout structure.

## See Also

- [siSlopeAndIntercept atom](sislopeandintercept_atom.md)
  An atom that contains parameters relevant to a decompressor component.
- [siDecompressionParam atom ('wave')](sidecompressionparam_atom.md)
  An atom that stores data specific to a given audio decompressor.
- [Format atom ('frma')](format_atom.md)
  An atom that shows the data format of the stored sound media.
- [Terminator atom ('0x00000000')](terminator_atom.md)
  An atom that indicates the end of the sound description.
- [MPEG-4 elementary sound stream descriptor atom ('esds')](mpeg-4_elementary_sound_stream_descriptor_atom.md)
  A required extension to the audio sample description for MPEG-4 audio.
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/audio_channel_layout_atom)*