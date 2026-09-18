# FormatFlagIsAlignedHigh

**Framework**: VideoDriverKit  
**Kind**: case

Set if the sample bits are placed into the high bits of the channel, clear for low bit placement.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
FormatFlagIsAlignedHigh
```

#### Discussion

This flag is only valid if `FormatFlagIsPacked` is clear.

## See Also

- [LinearPCMFormatFlagIsAlignedHigh](videodriverkit/iouservideoformatflags/linearpcmformatflagisalignedhigh.md)
  Synonym for `FormatFlagIsAlignedHigh`.
- [FormatFlagIsPacked](videodriverkit/iouservideoformatflags/formatflagispacked.md)
  Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel.
- [LinearPCMFormatFlagIsPacked](videodriverkit/iouservideoformatflags/linearpcmformatflagispacked.md)
  Synonym for `FormatFlagIsPacked`.
- [FormatFlagsNativeFloatPacked](videodriverkit/iouservideoformatflags/formatflagsnativefloatpacked.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/formatflagisalignedhigh)*