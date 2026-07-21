# SetClockAlgorithm

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetClockAlgorithm(IOUserVideoClockAlgorithm in_clock_algorithm);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the IOUserVideoClockAlgorithm value of the IOUserVideoClockDevice

Drivers can change the clock algorithm  of the clock device dynamically.  A notification will be sent to the host to update the object state if successful.

## Parameters

- `in_clock_algorithm`: IOUserVideoClockAlgorithm  to set

## See Also

- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setclockalgorithm)*