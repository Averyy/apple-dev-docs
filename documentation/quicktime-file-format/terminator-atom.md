# Terminator atom ('0x00000000')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that indicates the end of the sound description.

## Mentions

- [Sound sample data](sound_sample_data.md)

#### Overview

This atom is present to indicate the end of the sound description. It contains no data, and has a type field of zero (`0x00000000`) instead of a four-character code.

## Topics

### Data fields
- [Size](terminator_atom/size.md)
  An unsigned 32-bit integer holding the size of the decompression parameters atom.
- [Type](terminator_atom/type.md)
  An unsigned 32-bit integer.

## See Also

- [siSlopeAndIntercept atom](sislopeandintercept_atom.md)
  An atom that contains parameters relevant to a decompressor component.
- [siDecompressionParam atom ('wave')](sidecompressionparam_atom.md)
  An atom that stores data specific to a given audio decompressor.
- [Format atom ('frma')](format_atom.md)
  An atom that shows the data format of the stored sound media.
- [MPEG-4 elementary sound stream descriptor atom ('esds')](mpeg-4_elementary_sound_stream_descriptor_atom.md)
  A required extension to the audio sample description for MPEG-4 audio.
- [Audio channel layout atom ('chan')](audio_channel_layout_atom.md)
  An optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies.
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/terminator_atom)*