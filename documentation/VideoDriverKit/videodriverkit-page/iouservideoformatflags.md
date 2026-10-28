# IOUserVideoFormatFlags

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

Standard format flags for a basic description.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoFormatFlags : uint32_t;
```

## Overview

These are the standard flags for use in the `mFormatFlags` field of the [`IOUserVideoStreamBasicDescription`](./iouservideostreambasicdescription.md) structure.

Typically, when a VSBD is being used, the fields describe the complete layout of the sample data in the buffers that are represented by this description - where typically those buffers are represented by a video buffer that is contained in a video buffer list.

However, when a VSBD has the [`FormatFlagIsNonInterleaved`](./iouservideoformatflags/formatflagisnoninterleaved.md) flag, the video buffer list has a different structure and semantic. In this case, the VSBD fields describe the format of one of the video buffers that are contained in the list, and each video buffer in the list is determined to have a single (mono) channel of audio data. Then, the VSBD’s `mChannelsPerFrame` indicates the total number of buffers that are contained within the video buffer list - where each buffer contains one channel. This is used primarily with the `VideoUnit` (and `VideoConverter`) representation of this list - and won’t be found in the `VideoHardware` usage of this structure.

## Topics

### Numeric representation flags
- [FormatFlagIsFloat](./iouservideoformatflags/formatflagisfloat.md)
  Set for floating point, clear for integer.
- [LinearPCMFormatFlagIsFloat](./iouservideoformatflags/linearpcmformatflagisfloat.md)
  Synonym for `FormatFlagIsFloat`.
- [FormatFlagIsSignedInteger](./iouservideoformatflags/formatflagissignedinteger.md)
  Set for signed integer, clear for unsigned integer.
- [LinearPCMFormatFlagIsSignedInteger](./iouservideoformatflags/linearpcmformatflagissignedinteger.md)
  Synonym for `FormatFlagIsSignedInteger`.
### Bitwise layout flags
- [FormatFlagIsAlignedHigh](./iouservideoformatflags/formatflagisalignedhigh.md)
  Set if the sample bits are placed into the high bits of the channel, clear for low bit placement.
- [LinearPCMFormatFlagIsAlignedHigh](./iouservideoformatflags/linearpcmformatflagisalignedhigh.md)
  Synonym for `FormatFlagIsAlignedHigh`.
- [FormatFlagIsPacked](./iouservideoformatflags/formatflagispacked.md)
  Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel.
- [LinearPCMFormatFlagIsPacked](./iouservideoformatflags/linearpcmformatflagispacked.md)
  Synonym for `FormatFlagIsPacked`.
- [FormatFlagsNativeFloatPacked](./iouservideoformatflags/formatflagsnativefloatpacked.md)
### Endianness flags
- [FormatFlagIsBigEndian](./iouservideoformatflags/formatflagisbigendian.md)
  Set for big endian, clear for little endian.
- [LinearPCMFormatFlagIsBigEndian](./iouservideoformatflags/linearpcmformatflagisbigendian.md)
  Synonym for `FormatFlagIsBigEndian`.
- [FormatFlagsNativeEndian](./iouservideoformatflags/formatflagsnativeendian.md)
### Apple Lossless flags
- [AppleLosslessFormatFlag_16BitSourceData](./iouservideoformatflags/applelosslessformatflag_16bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 16 bit native endian signed integer data.
- [AppleLosslessFormatFlag_20BitSourceData](./iouservideoformatflags/applelosslessformatflag_20bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 20 bit native endian signed integer data aligned high in 24 bits.
- [AppleLosslessFormatFlag_24BitSourceData](./iouservideoformatflags/applelosslessformatflag_24bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 24 bit native endian signed integer data.
- [AppleLosslessFormatFlag_32BitSourceData](./iouservideoformatflags/applelosslessformatflag_32bitsourcedata.md)
  This flag is set for Apple Lossless data that was sourced from 32 bit native endian signed integer data.
### Channel layout flags
- [FormatFlagIsNonInterleaved](./iouservideoformatflags/formatflagisnoninterleaved.md)
  Set if the samples for each channel are located contiguously and the channels are layed out end to end, clear if the samples for each frame are layed out contiguously and the frames layed out end to end.
- [LinearPCMFormatFlagIsNonInterleaved](./iouservideoformatflags/linearpcmformatflagisnoninterleaved.md)
  Synonym for `FormatFlagIsNonInterleaved`.
### Mixability flags
- [FormatFlagIsNonMixable](./iouservideoformatflags/formatflagisnonmixable.md)
  Set to indicate when a format is non-mixable.
- [LinearPCMFormatFlagIsNonMixable](./iouservideoformatflags/linearpcmformatflagisnonmixable.md)
  Synonym for `FormatFlagIsNonMixable`.
### Sample fraction flags
- [LinearPCMFormatFlagsSampleFractionMask](./iouservideoformatflags/linearpcmformatflagssamplefractionmask.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.
- [LinearPCMFormatFlagsSampleFractionShift](./iouservideoformatflags/linearpcmformatflagssamplefractionshift.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.
### Special purpose flags
- [FormatFlagsAreAllClear](./iouservideoformatflags/formatflagsareallclear.md)
  Set if all the flags would be clear.
- [LinearPCMFormatFlagsAreAllClear](./iouservideoformatflags/linearpcmformatflagsareallclear.md)
  Synonym for `FormatFlagsAreAllClear`.

## See Also

### Working with video streams
- [IOUserVideoStreamBasicDescription](./iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [IOUserVideoFormatID](./iouservideoformatid.md)
  Identifiers used for formats of audio data.
- [IOUserVideoStreamDirection](./iouservideostreamdirection.md)
  The direction of a video stream.
- [IOUserVideoStreamTerminalType](./iouservideostreamterminaltype.md)
  The terminal type of video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags)*