# TwelvePtMovingWindowAverage

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

This clock algorithm uses a 12-point moving window average to filter the time stamps returned from `GetCurrentZeroTimestamp()`.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
TwelvePtMovingWindowAverage
```

## See Also

### Clock algorithms
- [Raw](./raw.md)
  When this value for the clock algorithm is specified, the Host will not apply any filtering to the time stamps returned from `GetCurrentZeroTimeStamp()`, and the values will be used as-is.
- [SimpleIIR](./simpleiir.md)
  When this value for the clock algorithm is specified, the Host applies a simple IIR filter to the time stamp stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclockalgorithm/twelveptmovingwindowaverage)*