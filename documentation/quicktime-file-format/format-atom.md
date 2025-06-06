# Format atom ('frma')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that shows the data format of the stored sound media.

## Mentions

- [Sound sample data](sound_sample_data.md)

## Topics

### Data fields
- [Size](format_atom/size.md)
  An unsigned 32-bit integer holding the size of the format atom.
- [Type](format_atom/type.md)
  An unsigned 32-bit field.
- [Data format](format_atom/data_format.md)
  A 32-bit integer indicating the format of the stored data.

## See Also

- [siSlopeAndIntercept atom](sislopeandintercept_atom.md)
  An atom that contains parameters relevant to a decompressor component.
- [siDecompressionParam atom ('wave')](sidecompressionparam_atom.md)
  An atom that stores data specific to a given audio decompressor.
- [Terminator atom ('0x00000000')](terminator_atom.md)
  An atom that indicates the end of the sound description.
- [MPEG-4 elementary sound stream descriptor atom ('esds')](mpeg-4_elementary_sound_stream_descriptor_atom.md)
  A required extension to the audio sample description for MPEG-4 audio.
- [Audio channel layout atom ('chan')](audio_channel_layout_atom.md)
  An optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies.
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/format_atom)*