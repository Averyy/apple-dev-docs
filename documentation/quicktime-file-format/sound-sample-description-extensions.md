# Sound sample description extensions

**Framework**: QuickTime File Format

Extend sound sample descriptions by appending other atoms.

#### Overview

All extensions to the SoundDescription record are made using atoms. That means one or more atoms can be appended to the end of the SoundDescription record using the standard [size, type] mechanism used throughout the QuickTime movie architecture. Extensions were first added with sound sample description v1.

To illustrate this, for sound sample description v1, the extensions are added by following the last field of the struct with QuickTime atoms. The struct implementation looks like this:

```None
struct SoundDescriptionV1 {
    // original fields
    SoundDescription    desc;
    // fixed compression ratio information
    unsigned long   samplesPerPacket;
    unsigned long   bytesPerPacket;
    unsigned long   bytesPerFrame;
    unsigned long   bytesPerSample;
    // optional, additional atom-based fields --
    // ([long size, long type, some data], repeat)
};
```

Version 2 of the sound sample description maintains the same mechanism for the addition of extensions. In the sound sample description v2 structure, the `sizeOfStructOnly` field value provides the offset to the extensions.

## Topics

### Extending sound sample descriptions
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
- [Subtitle follows track reference atom ('folw')](subtitle_follows_track_reference_atom.md)
  An atom that indicates a default subtitle track for a selected sound track.

## See Also

- [Sound sample descriptions](sound_sample_descriptions.md)
  A sound sample description contains information that defines how to interpret sound media data.
- [Sound sample data](sound_sample_data.md)
  Sound sample formats that QuickTime supports.
- [Audio priming-handling encoder delay in AAC](appendix_g_audio_priming_handling_encoder_delay_in_aac.md)
  Position a source audio signal in a sound track to handle encoder delay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_sample_description_extensions)*