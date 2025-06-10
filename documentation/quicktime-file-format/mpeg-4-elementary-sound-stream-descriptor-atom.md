# MPEG-4 elementary stream descriptor atom  ('esds')

**Framework**: QuickTime File Format  
**Kind**: class

A required extension to the audio sample description for MPEG-4 audio.

## Mentions

- [QuickTime File Format change log](revision_history.md)
- [Sound sample data](sound_sample_data.md)

#### Overview

This atom contains an elementary stream descriptor, which is defined in ISO/IEC FDIS 14496.

## Topics

### Data fields
- [Size](mpeg-4_elementary_sound_stream_descriptor_atom/size.md)
  An unsigned 32-bit integer holding the size of the elementary stream descriptor atom.
- [Type](mpeg-4_elementary_sound_stream_descriptor_atom/type.md)
  An unsigned 32-bit field.
- [Version](mpeg-4_elementary_sound_stream_descriptor_atom/version.md)
  An unsigned 32-bit integer set to zero.
- [Elementary stream descriptor](mpeg-4_elementary_sound_stream_descriptor_atom/elementary_stream_descriptor.md)
  An elementary stream descriptor for MPEG-4 audio.

## See Also

- [siSlopeAndIntercept atom](sislopeandintercept_atom.md)
  An atom that contains parameters relevant to a decompressor component.
- [siDecompressionParam atom ('wave')](sidecompressionparam_atom.md)
  An atom that stores data specific to a given audio decompressor.
- [Format atom ('frma')](format_atom.md)
  An atom that shows the data format of the stored sound media.
- [Terminator atom ('0x00000000')](terminator_atom.md)
  An atom that indicates the end of the sound description.
- [Audio channel layout atom ('chan')](audio_channel_layout_atom.md)
  An optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies.
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-4_elementary_sound_stream_descriptor_atom)*