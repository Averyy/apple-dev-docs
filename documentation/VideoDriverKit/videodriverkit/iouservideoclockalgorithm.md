# IOUserVideoClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: enum

Clock smoothing algorithm selectors.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
enum IOUserVideoClockAlgorithm : uint32_t;
```

#### Overview

These are the valid values for [`IOUserVideoClockAlgorithm`](videodriverkit/iouservideoclockalgorithm.md).

## Topics

### Clock algorithms
- [Raw](videodriverkit/iouservideoclockalgorithm/raw.md)
  When this value for the clock algorithm is specified, the Host will not apply any filtering to the time stamps returned from `GetCurrentZeroTimeStamp()`, and the values will be used as-is.
- [SimpleIIR](videodriverkit/iouservideoclockalgorithm/simpleiir.md)
  When this value for the clock algorithm is specified, the Host applies a simple IIR filter to the time stamp stream.
- [TwelvePtMovingWindowAverage](videodriverkit/iouservideoclockalgorithm/twelveptmovingwindowaverage.md)
  This clock algorithm uses a 12-point moving window average to filter the time stamps returned from `GetCurrentZeroTimestamp()`.

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
  Sets the algorithm for the video clock device.
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
  Sets the clock stability of the clock device.
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)
  Gets a Boolean value for clock stability of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclockalgorithm)*