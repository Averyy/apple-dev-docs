# GetClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: method

Gets the clock algorithm of the clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOUserVideoClockAlgorithm GetClockAlgorithm();
```

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
  Sets the algorithm for the video clock device.
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
  Sets the clock stability of the clock device.
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)
  Gets a Boolean value for clock stability of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getclockalgorithm)*