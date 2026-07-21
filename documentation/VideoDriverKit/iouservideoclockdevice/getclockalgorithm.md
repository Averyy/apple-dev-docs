# GetClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOUserVideoClockAlgorithm GetClockAlgorithm();
```

#### Return Value

Returns IOUserVideoClockAlgorithm

#### Discussion

Get the IOUserVideoClockAlgorithm of the IOUserVideoClockDevice.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getclockalgorithm)*