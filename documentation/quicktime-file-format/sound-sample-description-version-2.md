# Sound sample description version 2 ('stsd')

**Framework**: QuickTime File Format  
**Kind**: class

An updated sound sample description that adds high resolution audio.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

QuickTime 7 introduced a new version of the sound sample description, version 2, which extends QuickTime capabilities to include high resolution audio with another expansion of the sound sample description structure. In QuickTime 7, the sound and audio facilities are based on the Core Audio framework facilities and the Sound Manager has been deprecated. In this version of the sound sample description, the format field is set to `‘lpcm’` for uncompressed data. For compressed data formats, the format field is set to the compression type code (normally `‘mp4a’`) and the compression specifics and other features of QuickTime 7 are supplied by extensions.

The version field is set to `2` for this version of the sound sample description structure.

The sound sample description v2 structure adds the following new fields, appending to the v1 structure and renaming the four fields added in v1 to help ensure backwards compatibility with older applications.

> ❗ **Important**: The values contained in these fields have different meanings for compressed and uncompressed audio. The meaning may not be easily deducible from the field name and require reference to the appropriate sound sample description extensions to understand fully.

The values contained in these fields have different meanings for compressed and uncompressed audio. The meaning may not be easily deducible from the field name and require reference to the appropriate sound sample description extensions to understand fully.

Some definitions for sound sample description version 2:

- LPCM Frame: one uncompressed sample in each of the channels (for instance, 44100Hz audio has 44100 LPCM frames per second, whether it is mono, stereo, 5.1, or other possible values). In other words, LPCM Frames divided by the `audioSampleRate` value is duration in seconds.
- Audio Packet: For compressed audio, an audio packet is the natural compressed access unit of that format. For uncompressed audio, an audio packet is simply one LPCM frame.
- Fields prefixed by `const`: Note the three sound sample description v2 fields whose names start with `const`. These fields are only nonzero if the value is a constant. A zero in each field implies that the value is variable. For example: AAC audio would have a zero in `constBytesPerAudioPacket` because AAC has variable sized audio packets. Codecs with variable duration audio packets set a zero in `constLPCMFramesPerAudioPacket`.

#### Lpcm Flag Values

The formatSpecificFlags field carries flags significant to the layout and formatting of audio streams defined in the Core Audio underpinnings for sound sample description v2. These are enumerated in the Apple QuickTime/CoreAudioFormat.h interface file and are subject to a fuller interpretation in the context of the AudioStreamBasicDescription data type. See the CoreAudio, “Core Audio Framework Reference” in the OS X Developer Library.

```None
enum
{
    kAudioFormatFlagIsFloat                  = (1 << 0),  // 0x1
    kAudioFormatFlagIsBigEndian              = (1 << 1),  // 0x2
    kAudioFormatFlagIsSignedInteger          = (1 << 2),  // 0x4
    kAudioFormatFlagIsPacked                 = (1 << 3),  // 0x8
    kAudioFormatFlagIsAlignedHigh            = (1 << 4),  // 0x10
    kAudioFormatFlagIsNonInterleaved         = (1 << 5),  // 0x20
    kAudioFormatFlagIsNonMixable             = (1 << 6),  // 0x40
    kAudioFormatFlagsAreAllClear             = (1 << 31),
    
    kLinearPCMFormatFlagIsFloat              = kAudioFormatFlagIsFloat,
    kLinearPCMFormatFlagIsBigEndian          = kAudioFormatFlagIsBigEndian,
    kLinearPCMFormatFlagIsSignedInteger      = kAudioFormatFlagIsSignedInteger,
    kLinearPCMFormatFlagIsPacked             = kAudioFormatFlagIsPacked,
    kLinearPCMFormatFlagIsAlignedHigh        = kAudioFormatFlagIsAlignedHigh,
    kLinearPCMFormatFlagIsNonInterleaved     = kAudioFormatFlagIsNonInterleaved,
    kLinearPCMFormatFlagIsNonMixable         = kAudioFormatFlagIsNonMixable,
    kLinearPCMFormatFlagsSampleFractionShift = 7,
    kLinearPCMFormatFlagsSampleFractionMask  = (0x3F << kLinearPCMFormatFlagsSampleFractionShift),
    kLinearPCMFormatFlagsAreAllClear         = kAudioFormatFlagsAreAllClear,
    
    kAppleLosslessFormatFlag_16BitSourceData = 1,
    kAppleLosslessFormatFlag_20BitSourceData = 2,
    kAppleLosslessFormatFlag_24BitSourceData = 3,
    kAppleLosslessFormatFlag_32BitSourceData = 4
};
```

## Topics

### Data fields
- [Sample description size](sound_sample_description_version_2/sample_description_size.md)
  A 32-bit integer indicating the number of bytes in the sample description.
- [Data format](sound_sample_description_version_2/data_format.md)
  A 32-bit integer indicating the format of the stored data.
- [Reserved](sound_sample_description_version_2/reserved.md)
  Six bytes.
- [Data reference index](sound_sample_description_version_2/data_reference_index.md)
  A 16-bit integer that contains the index of the data reference to use to retrieve data associated with samples that use this sample description.
- [Version](sound_sample_description_version_2/version.md)
  A 16-bit integer that holds the sample description version.
- [Revision level](sound_sample_description_version_2/revision_level.md)
  A 16-bit integer.
- [Vendor](sound_sample_description_version_2/vendor.md)
  A 32-bit integer.
- [always3](sound_sample_description_version_2/always3.md)
  A 16-bit integer field.
- [always16](sound_sample_description_version_2/always16.md)
  A 16-bit integer field.
- [alwaysMinus2](sound_sample_description_version_2/alwaysminus2.md)
  A 16-bit integer field.
- [always0](sound_sample_description_version_2/always0.md)
  A 16-bit integer field.
- [always65536](sound_sample_description_version_2/always65536.md)
  A 32-bit integer field.
- [sizeOfStructOnly](sound_sample_description_version_2/sizeofstructonly.md)
  A 32-bit integer field providing the offset to sound sample description structure’s extensions.
- [numAudioChannels](sound_sample_description_version_2/numaudiochannels.md)
  A 32-bit integer field set to the number of audio channels.
- [always7F000000](sound_sample_description_version_2/always7f000000.md)
  A 32-bit integer field.
- [constBitsPerChannel](sound_sample_description_version_2/constbitsperchannel.md)
  A 32-bit integer field which is set only if constant and only for uncompressed audio.
- [formatSpecificFlags](sound_sample_description_version_2/formatspecificflags.md)
  A 32-bit integer field which carries LPCM flag values.
- [constBytesPerAudioPacket](sound_sample_description_version_2/constbytesperaudiopacket.md)
  A 32-bit unsigned integer set to the number of bytes per packet only if this value is constant.
- [constLPCMFramesPerAudioPacket](sound_sample_description_version_2/constlpcmframesperaudiopacket.md)
  A 32-bit unsigned integer set to the number of PCM frames per packet only if this value is constant.

## See Also

- [Sound sample description version 0 ('stsd')](sound_sample_description_version_0.md)
  A sound sample description that supports only uncompressed audio in raw or twos-complement format.
- [Sound sample description version 1 ('stsd')](sound_sample_description_version_1.md)
  An extended sound sample description that supports compressed audio, and includes the ability to add atoms to the sound description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_sample_description_version_2)*