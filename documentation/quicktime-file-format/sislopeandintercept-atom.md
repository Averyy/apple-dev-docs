# siSlopeAndIntercept atom

**Framework**: Quicktime File Format  
**Kind**: class

An atom that contains parameters relevant to a decompressor component.

#### Overview

> **Note**: The siSlopeAndIntercept atom is deprecated in the QuickTime file format. The information that follows documents existing content containing this atom and should not be used for new development.

The siSlopeAndIntercept atom contains `slope`, `intercept`, `minClip`, and `maxClip` parameters relevant to a decompressor component.

At runtime, the contents of the type `siSlopeAndIntercept` and `siDecompressorSettings` atoms are provided to the decompressor component through the standard `SetInfo` mechanism of the Sound Manager.

```None
struct SoundSlopeAndInterceptRecord {
    Float64                 slope;
    Float64                 intercept;
    Float64                 minClip;
    Float64                 maxClip;
};
typedef struct SoundSlopeAndInterceptRecord SoundSlopeAndInterceptRecord;
```

## Topics

### Data fields
- [Slope](sislopeandintercept_atom/slope.md)
- [Intercept](sislopeandintercept_atom/intercept.md)
- [minClip](sislopeandintercept_atom/minclip.md)
- [maxClip](sislopeandintercept_atom/maxclip.md)

## See Also

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
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sislopeandintercept_atom)*