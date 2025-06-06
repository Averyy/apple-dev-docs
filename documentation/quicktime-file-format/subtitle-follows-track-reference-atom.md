# Subtitle follows track reference atom ('folw')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that indicates a default subtitle track for a selected sound track.

#### Overview

Sound tracks can have a track reference of type `'folw'` (for “follows”) to a single subtitle track from among the subtitle tracks in the same alternate group; this subtitle track should be considered the default to select if the sound track is selected. Use this only if compatibility between language tags is not possible for some reason making it impossible to otherwise select a default track. See [`Preparing sound and subtitle alternate groups for use with Apple devices`](preparing_sound_and_subtitle_alternate_groups_for_use_with_apple_devices.md) for related information.

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
- [Audio channel layout atom ('chan')](audio_channel_layout_atom.md)
  An optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_follows_track_reference_atom)*