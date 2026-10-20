# FormatFlagIsAlignedHigh

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

Set if the sample bits are placed into the high bits of the channel, clear for low bit placement.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
FormatFlagIsAlignedHigh
```

#### Discussion

This flag is only valid if `FormatFlagIsPacked` is clear.

## See Also

### Bitwise layout flags
- [LinearPCMFormatFlagIsAlignedHigh](./linearpcmformatflagisalignedhigh.md)
  Synonym for `FormatFlagIsAlignedHigh`.
- [FormatFlagIsPacked](./formatflagispacked.md)
  Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel.
- [LinearPCMFormatFlagIsPacked](./linearpcmformatflagispacked.md)
  Synonym for `FormatFlagIsPacked`.
- [FormatFlagsNativeFloatPacked](./formatflagsnativefloatpacked.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/formatflagisalignedhigh)*