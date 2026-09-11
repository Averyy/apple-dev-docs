# FormatFlagIsPacked

**Framework**: VideoDriverKit  
**Kind**: case

Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
FormatFlagIsPacked
```

#### Discussion

Even if this flag is clear, it is implied that this flag is set if the `VideoStreamBasicDescription` is filled out such that the fields have the following relationship:

```None
((mBitsPerSample / 8) * mChannelsPerFrame) == mBytesPerFrame
```

## See Also

- [FormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/formatflagisalignedhigh.md)
  Set if the sample bits are placed into the high bits of the channel, clear for low bit placement.
- [LinearPCMFormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/linearpcmformatflagisalignedhigh.md)
  Synonym for `FormatFlagIsAlignedHigh`.
- [LinearPCMFormatFlagIsPacked](videodriverkit/iouservideoformatflags/linearpcmformatflagispacked.md)
  Synonym for `FormatFlagIsPacked`.
- [FormatFlagsNativeFloatPacked](videodriverkit/iouservideoformatflags/formatflagsnativefloatpacked.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/formatflagispacked)*