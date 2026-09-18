# LinearPCMFormatFlagsSampleFractionShift

**Framework**: VideoDriverKit  
**Kind**: case

The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
LinearPCMFormatFlagsSampleFractionShift
```

#### Discussion

The value indicates the number of bits are used to represent the fractional portion of each sample value. This constant indicates the bit position (counting from the right) of the bitfield in `mFormatFlags`.

## See Also

- [LinearPCMFormatFlagsSampleFractionMask](videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionmask.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionshift)*