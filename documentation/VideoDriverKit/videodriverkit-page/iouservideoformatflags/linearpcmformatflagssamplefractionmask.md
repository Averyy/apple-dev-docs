# LinearPCMFormatFlagsSampleFractionMask

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
LinearPCMFormatFlagsSampleFractionMask
```

#### Discussion

This constant is the mask used to extract that bitfield from `mFormatFlags`:

```
number_fractional_bits = (mFormatFlags & LinearPCMFormatFlagsSampleFractionMask) >> LinearPCMFormatFlagsSampleFractionShift
```

## See Also

### Sample fraction flags
- [LinearPCMFormatFlagsSampleFractionShift](./linearpcmformatflagssamplefractionshift.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionmask)*