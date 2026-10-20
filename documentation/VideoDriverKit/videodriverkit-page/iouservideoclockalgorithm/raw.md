# Raw

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

When this value for the clock algorithm is specified, the Host will not apply any filtering to the time stamps returned from `GetCurrentZeroTimeStamp()`, and the values will be used as-is.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
Raw
```

## See Also

### Clock algorithms
- [SimpleIIR](./simpleiir.md)
  When this value for the clock algorithm is specified, the Host applies a simple IIR filter to the time stamp stream.
- [TwelvePtMovingWindowAverage](./twelveptmovingwindowaverage.md)
  This clock algorithm uses a 12-point moving window average to filter the time stamps returned from `GetCurrentZeroTimestamp()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclockalgorithm/raw)*