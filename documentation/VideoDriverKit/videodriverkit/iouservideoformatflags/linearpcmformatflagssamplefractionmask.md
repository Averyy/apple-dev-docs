# LinearPCMFormatFlagsSampleFractionMask

**Framework**: VideoDriverKit  
**Kind**: case

The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
LinearPCMFormatFlagsSampleFractionMask
```

#### Discussion

This constant is the mask used to extract that bitfield from `mFormatFlags`:

```None
number_fractional_bits = (mFormatFlags & LinearPCMFormatFlagsSampleFractionMask) >> LinearPCMFormatFlagsSampleFractionShift
```

## See Also

- [LinearPCMFormatFlagsSampleFractionShift](videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionshift.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionmask)*