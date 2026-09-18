# GetClockIsStable

**Framework**: VideoDriverKit  
**Kind**: method

Gets a Boolean value for clock stability of the clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
bool GetClockIsStable();
```

#### Return Value

A Boolean value that indicates whether the clock is stable.

#### Discussion

The object’s work queue synchronizes access to this value.

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
  Sets the algorithm for the video clock device.
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
  Sets the clock stability of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getclockisstable)*