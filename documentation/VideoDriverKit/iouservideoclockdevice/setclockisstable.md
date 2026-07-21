# SetClockIsStable

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetClockIsStable(bool in_clock_is_stable);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set bool for clock stability of the IOUserVideoClockDevice.

Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_clock_is_stable`: True if clock is stable. False if clock is unstable.

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setclockisstable)*