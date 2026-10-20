# LinearPCMFormatFlagsSampleFractionShift

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
LinearPCMFormatFlagsSampleFractionShift
```

#### Discussion

The value indicates the number of bits are used to represent the fractional portion of each sample value. This constant indicates the bit position (counting from the right) of the bitfield in `mFormatFlags`.

## See Also

### Sample fraction flags
- [LinearPCMFormatFlagsSampleFractionMask](./linearpcmformatflagssamplefractionmask.md)
  The linear PCM flags contain a 6-bit bitfield indicating that an integer format is to be interpreted as fixed point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoformatflags/linearpcmformatflagssamplefractionshift)*