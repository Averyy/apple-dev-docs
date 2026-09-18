# SimpleIIR

**Framework**: VideoDriverKit  
**Kind**: case

When this value for the clock algorithm is specified, the Host applies a simple IIR filter to the time stamp stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
SimpleIIR
```

#### Discussion

This is the default algorithm used for devices that don’t implement `DevicePropertyClockAlgorithm`.

## See Also

- [Raw](videodriverkit/iouservideoclockalgorithm/raw.md)
  When this value for the clock algorithm is specified, the Host will not apply any filtering to the time stamps returned from `GetCurrentZeroTimeStamp()`, and the values will be used as-is.
- [TwelvePtMovingWindowAverage](videodriverkit/iouservideoclockalgorithm/twelveptmovingwindowaverage.md)
  This clock algorithm uses a 12-point moving window average to filter the time stamps returned from `GetCurrentZeroTimestamp()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclockalgorithm/simpleiir)*