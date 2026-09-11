# TwelvePtMovingWindowAverage

**Framework**: VideoDriverKit  
**Kind**: case

This clock algorithm uses a 12-point moving window average to filter the time stamps returned from `GetCurrentZeroTimestamp()`.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
TwelvePtMovingWindowAverage
```

## See Also

- [Raw](videodriverkit/iouservideoclockalgorithm/raw.md)
  When this value for the clock algorithm is specified, the Host will not apply any filtering to the time stamps returned from `GetCurrentZeroTimeStamp()`, and the values will be used as-is.
- [SimpleIIR](videodriverkit/iouservideoclockalgorithm/simpleiir.md)
  When this value for the clock algorithm is specified, the Host applies a simple IIR filter to the time stamp stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclockalgorithm/twelveptmovingwindowaverage)*