# SetClockIsStable

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the clock stability of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetClockIsStable(bool in_clock_is_stable);
```

## Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `in_clock_is_stable`: True if clock is stable. False if clock is unstable.

## See Also

### Working with clock device behavior
- [SetClockAlgorithm](./setclockalgorithm.md)
  Sets the algorithm for the video clock device.
- [GetClockAlgorithm](./getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserVideoClockAlgorithm](../videodriverkit-page/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
- [GetClockIsStable](./getclockisstable.md)
  Gets a Boolean value for clock stability of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setclockisstable)*