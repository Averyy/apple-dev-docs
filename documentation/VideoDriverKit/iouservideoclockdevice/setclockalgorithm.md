# SetClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: method

Sets the algorithm for the video clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetClockAlgorithm(IOUserVideoClockAlgorithm in_clock_algorithm);
```

#### Return Value

A kern_return_t value indicating success or failure.

#### Discussion

Drivers can change the clock algorithm of the clock device dynamically. If successful, the clock device sends a notification to the host to update the object state.

## Parameters

- `in_clock_algorithm`: The IOUserVideoClockAlgorithm value to set.

## See Also

- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
  Sets the clock stability of the clock device.
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)
  Gets a Boolean value for clock stability of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setclockalgorithm)*