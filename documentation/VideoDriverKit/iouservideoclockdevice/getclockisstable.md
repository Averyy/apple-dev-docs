# GetClockIsStable

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
bool GetClockIsStable();
```

#### Return Value

Returns bool

#### Discussion

Get bool for clock stability of the IOUserVideoClockDevice.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getclockisstable)*