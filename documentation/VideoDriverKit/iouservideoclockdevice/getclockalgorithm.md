# GetClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the clock algorithm of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
IOUserVideoClockAlgorithm GetClockAlgorithm();
```

## Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Working with clock device behavior
- [SetClockAlgorithm](./setclockalgorithm.md)
  Sets the algorithm for the video clock device.
- [IOUserVideoClockAlgorithm](../videodriverkit-page/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
- [SetClockIsStable](./setclockisstable.md)
  Sets the clock stability of the clock device.
- [GetClockIsStable](./getclockisstable.md)
  Gets a Boolean value for clock stability of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getclockalgorithm)*