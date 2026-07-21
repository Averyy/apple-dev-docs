# IOUserVideoFormatFlags

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoFormatFlags : uint32_t;
```

#### Overview

Standard IOUserVideoFormatFlags values for IOUserVideoStreamBasicDescription. These are the standard VideoFormatFlags for use in the mFormatFlags field of the VideoStreamBasicDescription structure.

Typically, when an ASBD is being used, the fields describe the complete layout of the sample data in the buffers that are represented by this description - where typically those buffers are represented by an VideoBuffer that is contained in an VideoBufferList.

However, when an ASBD has the FormatFlagIsNonInterleaved flag, the VideoBufferList has a different structure and semantic. In this case, the ASBD fields will describe the format of ONE of the VideoBuffers that are contained in the list, AND each VideoBuffer in the list is determined to have a single (mono) channel of audio data. Then, the ASBD’s mChannelsPerFrame will indicate the total number of VideoBuffers that are contained within the VideoBufferList - where each buffer contains one channel. This is used primarily with the VideoUnit (and VideoConverter) representation of this list - and won’t be found in the VideoHardware usage of this structure.

Set for floating point, clear for integer.

Set for big endian, clear for little endian.

Set for signed integer, clear for unsigned integer. This is only valid if FormatFlagIsFloat is clear.

Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel. Note that even if this flag is clear, it is implied that this flag is set if the VideoStreamBasicDescription is filled out such that the fields have the following relationship: ((mBitsPerSample / 8) * mChannelsPerFrame) == mBytesPerFrame

Set if the sample bits are placed into the high bits of the channel, clear for low bit placement. This is only valid if FormatFlagIsPacked is clear.

Set if the samples for each channel are located contiguously and the channels are layed out end to end, clear if the samples for each frame are layed out contiguously and the frames layed out end to end.

Set to indicate when a format is non-mixable. Note that this flag is only used when interacting with the HAL’s stream format information. It is not a valid flag for any other uses.

Set if all the flags would be clear in order to preserve 0 as the wild card value.

Synonym for FormatFlagIsFloat.

Synonym for FormatFlagIsBigEndian.

Synonym for FormatFlagIsSignedInteger.

Synonym for FormatFlagIsPacked.

Synonym for FormatFlagIsAlignedHigh.

Synonym for FormatFlagIsNonInterleaved.

Synonym for FormatFlagIsNonMixable.

Synonym for FormatFlagsAreAllClear.

The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point. The value indicates the number of bits are used to represent the fractional portion of each sample value. This constant indicates the bit position (counting from the right) of the bitfield in mFormatFlags.

number_fractional_bits = (mFormatFlags & LinearPCMFormatFlagsSampleFractionMask) >> LinearPCMFormatFlagsSampleFractionShift

This flag is set for Apple Lossless data that was sourced from 16 bit native endian signed integer data.

This flag is set for Apple Lossless data that was sourced from 20 bit native endian signed integer data aligned high in 24 bits.

This flag is set for Apple Lossless data that was sourced from 24 bit native endian signed integer data.

This flag is set for Apple Lossless data that was sourced from 32 bit native endian signed integer data.

## Topics

### Numeric representation flags
- [FormatFlagIsFloat](videodriverkit/iouservideoformatflags/formatflagisfloat.md)
- [LinearPCMFormatFlagIsFloat](videodriverkit/iouservideoformatflags/linearpcmformatflagisfloat.md)
- [FormatFlagIsSignedInteger](videodriverkit/iouservideoformatflags/formatflagissignedinteger.md)
- [LinearPCMFormatFlagIsSignedInteger](videodriverkit/iouservideoformatflags/linearpcmformatflagissignedinteger.md)
### Bitwise layout flags
- [FormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/formatflagisalignedhigh.md)
- [LinearPCMFormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/linearpcmformatflagisalignedhigh.md)
- [FormatFlagIsPacked](videodriverkit/iouservideoformatflags/formatflagispacked.md)
- [LinearPCMFormatFlagIsPacked](videodriverkit/iouservideoformatflags/linearpcmformatflagispacked.md)
- [FormatFlagsNativeFloatPacked](videodriverkit/iouservideoformatflags/formatflagsnativefloatpacked.md)
### Endianness flags
- [FormatFlagIsBigEndian](videodriverkit/iouservideoformatflags/formatflagisbigendian.md)
- [LinearPCMFormatFlagIsBigEndian](videodriverkit/iouservideoformatflags/linearpcmformatflagisbigendian.md)
- [FormatFlagsNativeEndian](videodriverkit/iouservideoformatflags/formatflagsnativeendian.md)
### Apple Lossless flags
- [AppleLosslessFormatFlag_16BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_16bitsourcedata.md)
- [AppleLosslessFormatFlag_20BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_20bitsourcedata.md)
- [AppleLosslessFormatFlag_24BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_24bitsourcedata.md)
- [AppleLosslessFormatFlag_32BitSourceData](videodriverkit/iouservideoformatflags/applelosslessformatflag_32bitsourcedata.md)
### Channel layout flags
- [FormatFlagIsNonInterleaved](videodriverkit/iouservideoformatflags/formatflagisnoninterleaved.md)
- [LinearPCMFormatFlagIsNonInterleaved](videodriverkit/iouservideoformatflags/linearpcmformatflagisnoninterleaved.md)
### Mixability flags
- [FormatFlagIsNonMixable](videodriverkit/iouservideoformatflags/formatflagisnonmixable.md)
- [LinearPCMFormatFlagIsNonMixable](videodriverkit/iouservideoformatflags/linearpcmformatflagisnonmixable.md)
### Sample fraction flags
- [LinearPCMFormatFlagsSampleFractionMask](videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionmask.md)
- [LinearPCMFormatFlagsSampleFractionShift](videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionshift.md)
### Special purpose flags
- [FormatFlagsAreAllClear](videodriverkit/iouservideoformatflags/formatflagsareallclear.md)
- [LinearPCMFormatFlagsAreAllClear](videodriverkit/iouservideoformatflags/linearpcmformatflagsareallclear.md)

## See Also

- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [IOUserVideoFormatID](videodriverkit/iouservideoformatid.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags)*