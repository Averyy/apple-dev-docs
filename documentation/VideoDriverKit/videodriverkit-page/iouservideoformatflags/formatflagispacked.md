# FormatFlagIsPacked

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

Set if the sample bits occupy the entire available bits for the channel, clear if they are high or low aligned within the channel.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
FormatFlagIsPacked
```

#### Discussion

Even if this flag is clear, it is implied that this flag is set if the [`IOUserVideoStreamBasicDescription`](../iouservideostreambasicdescription.md) is filled out such that the fields have the following relationship:

```
((mBitsPerSample / 8) * mChannelsPerFrame) == mBytesPerFrame
```

## See Also

### Bitwise layout flags
- [FormatFlagIsAlignedHigh](./formatflagisalignedhigh.md)
  Set if the sample bits are placed into the high bits of the channel, clear for low bit placement.
- [LinearPCMFormatFlagIsAlignedHigh](./linearpcmformatflagisalignedhigh.md)
  Synonym for `FormatFlagIsAlignedHigh`.
- [LinearPCMFormatFlagIsPacked](./linearpcmformatflagispacked.md)
  Synonym for `FormatFlagIsPacked`.
- [FormatFlagsNativeFloatPacked](./formatflagsnativefloatpacked.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/formatflagispacked)*