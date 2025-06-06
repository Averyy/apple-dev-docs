# siDecompressionParam atom ('wave')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that stores data specific to a given audio decompressor.

## Mentions

- [Sound sample data](sound_sample_data.md)

#### Overview

The `siDecompressionParam` atom provides the ability to store data specific to a given audio decompressor in the `SoundDescription` record. As example, some audio decompression algorithms, such as Microsoft’s ADPCM, require a set of out-of-band values to configure the decompressor. These are stored in an atom of this type.

This atom contains other atoms with audio decompressor settings and is a required extension to the sound sample description for MPEG-4 audio. A `'wave'` chunk for `'mp4a'` typically contains (in order) at least a `'frma'` atom, an `'mp4a'` atom, an `'esds'` atom, and a [`Terminator atom ('0x00000000')`](terminator_atom.md).

The contents of other `siDecompressionParam` atoms are dependent on the audio decompressor.

## Topics

### Data fields
- [Size](sidecompressionparam_atom/size.md)
  An unsigned 32-bit integer holding the size of the decompression parameters atom.
- [Type](sidecompressionparam_atom/type.md)
  An unsigned 32-bit field.
- [Extension atoms](sidecompressionparam_atom/extension_atoms.md)
  Atoms containing the necessary out-of-band decompression parameters for the sound decompressor.

## See Also

- [siSlopeAndIntercept atom](sislopeandintercept_atom.md)
  An atom that contains parameters relevant to a decompressor component.
- [Format atom ('frma')](format_atom.md)
  An atom that shows the data format of the stored sound media.
- [Terminator atom ('0x00000000')](terminator_atom.md)
  An atom that indicates the end of the sound description.
- [MPEG-4 elementary sound stream descriptor atom ('esds')](mpeg-4_elementary_sound_stream_descriptor_atom.md)
  A required extension to the audio sample description for MPEG-4 audio.
- [Audio channel layout atom ('chan')](audio_channel_layout_atom.md)
  An optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies.
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sidecompressionparam_atom)*