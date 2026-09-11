# IOUserVideoFormatFlags

**Framework**: VideoDriverKit  
**Kind**: enum

Standard format flags for a basic description.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
enum IOUserVideoFormatFlags : uint32_t;
```

#### Overview

These are the standard flags for use in the `mFormatFlags` field of the `VideoStreamBasicDescription` structure.

Typically, when an ASBD is being used, the fields describe the complete layout of the sample data in the buffers that are represented by this description - where typically those buffers are represented by an VideoBuffer that is contained in an VideoBufferList.

However, when an ASBD has the [`FormatFlagIsNonInterleaved`](videodriverkit/iouservideoformatflags/formatflagisnoninterleaved.md) flag, the video buffer list has a different structure and semantic. In this case, the ASBD fields describe the format of oneof the video buffersthat are contained in the list, and each video buffer in the list is determined to have a single (mono) channel of audio data. Then, the ASBD’s `mChannelsPerFrame` indicates the total number of buffers that are contained within the video buffer list - where each buffer contains one channel. This is used primarily with the `VideoUnit` (and `VideoConverter`) representation of this list - and won’t be found in the `VideoHardware` usage of this structure.

## Topics

### Numeric representation flags
- [FormatFlagIsFloat](videodriverkit/iouservideoformatflags/formatflagisfloat.md)
  Set for floating point, clear for integer.
- [LinearPCMFormatFlagIsFloat](videodriverkit/iouservideoformatflags/linearpcmformatflagisfloat.md)
  Synonym for `FormatFlagIsFloat`.
- [FormatFlagIsSignedInteger](videodriverkit/iouservideoformatflags/formatflagissignedinteger.md)
  Set for signed integer, clear for unsigned integer.
- [LinearPCMFormatFlagIsSignedInteger](videodriverkit/iouservideoformatflags/linearpcmformatflagissignedinteger.md)
  Synonym for `FormatFlagIsSignedInteger`.
### Bitwise layout flags
- [FormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/formatflagisalignedhigh.md)
  Set if the sample bits are placed into the high bits of the channel, clear for low bit placement.
- [LinearPCMFormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/linearpcmformatflagisalignedhigh.md)
  Synonym for `FormatFlagIsAlignedHigh`.
- [FormatFlagIsPacked](videodriverkit/iouservideoformatflags/formatflagispacked.md)
  Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel.
- [LinearPCMFormatFlagIsPacked](videodriverkit/iouservideoformatflags/linearpcmformatflagispacked.md)
  Synonym for `FormatFlagIsPacked`.
- [FormatFlagsNativeFloatPacked](videodriverkit/iouservideoformatflags/formatflagsnativefloatpacked.md)
### Endianness flags
- [FormatFlagIsBigEndian](videodriverkit/iouservideoformatflags/formatflagisbigendian.md)
  Set for big endian, clear for little endian.
- [LinearPCMFormatFlagIsBigEndian](videodriverkit/iouservideoformatflags/linearpcmformatflagisbigendian.md)
  Synonym for `FormatFlagIsBigEndian`.
- [FormatFlagsNativeEndian](videodriverkit/iouservideoformatflags/formatflagsnativeendian.md)
### Apple Lossless flags
- [AppleLosslessFormatFlag_16BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_16bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 16 bit native endian signed integer data.
- [AppleLosslessFormatFlag_20BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_20bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 20 bit native endian signed integer data aligned high in 24 bits.
- [AppleLosslessFormatFlag_24BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_24bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 24 bit native endian signed integer data.
- [AppleLosslessFormatFlag_32BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_32bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 32 bit native endian signed integer data.
### Channel layout flags
- [FormatFlagIsNonInterleaved](videodriverkit/iouservideoformatflags/formatflagisnoninterleaved.md)
  Set if the samples for each channel are located contiguously and the channels are layed out end to end, clear if the samples for each frame are layed out contiguously and the frames layed out end to end.
- [LinearPCMFormatFlagIsNonInterleaved](videodriverkit/iouservideoformatflags/linearpcmformatflagisnoninterleaved.md)
  Synonym for `FormatFlagIsNonInterleaved`.
### Mixability flags
- [FormatFlagIsNonMixable](videodriverkit/iouservideoformatflags/formatflagisnonmixable.md)
  Set to indicate when a format is non-mixable.
- [LinearPCMFormatFlagIsNonMixable](videodriverkit/iouservideoformatflags/linearpcmformatflagisnonmixable.md)
  Synonym for `FormatFlagIsNonMixable`.
### Sample fraction flags
- [LinearPCMFormatFlagsSampleFractionMask](videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionmask.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.
- [LinearPCMFormatFlagsSampleFractionShift](videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionshift.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.
### Special purpose flags
- [FormatFlagsAreAllClear](videodriverkit/iouservideoformatflags/formatflagsareallclear.md)
  Set if all the flags would be clear.
- [LinearPCMFormatFlagsAreAllClear](videodriverkit/iouservideoformatflags/linearpcmformatflagsareallclear.md)
  Synonym for `FormatFlagsAreAllClear`.

## See Also

- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [IOUserVideoFormatID](videodriverkit/iouservideoformatid.md)
  Identifiers used for formats of audio data.
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
  The direction of a video stream.
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)
  The terminal type of video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags)*