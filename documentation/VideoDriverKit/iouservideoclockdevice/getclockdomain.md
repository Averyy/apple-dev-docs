# GetClockDomain

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetClockDomain();
```

#### Return Value

Returns uint32_t

#### Discussion

Get the uint32_t clock domain value of the IOUserVideoClockDevice.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetClockDomain](iouservideoclockdevice/setclockdomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getclockdomain)*