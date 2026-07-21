# IOUserVideoClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoClockAlgorithm : uint32_t;
```

#### Overview

Clock Smoothing Algorithm Selectors.  The valid values for IOUserVideoClockAlgorithm

When this value for the clock algorithm is specified, the Host will not apply any filtering to the time stamps returned from GetCurrentZeroTimeStamp(). The values will be used as-is.

When this value for the clock algorithm is specified, the Host applies a simple IIR filter to the time stamp stream. This is the default algorithm used for devices that don’t implement DevicePropertyClockAlgorithm.

This clock algorithm uses a 12 point moving window average to filter the time stamps returned from GetCurrentZeroTimeStamp().

## Topics

### Clock algorithms
- [Raw](videodriverkit/iouservideoclockalgorithm/raw.md)
- [SimpleIIR](videodriverkit/iouservideoclockalgorithm/simpleiir.md)
- [TwelvePtMovingWindowAverage](videodriverkit/iouservideoclockalgorithm/twelveptmovingwindowaverage.md)

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclockalgorithm)*