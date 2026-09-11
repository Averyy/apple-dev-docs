# GetTransportType

**Framework**: VideoDriverKit  
**Kind**: method

Gets the transport type of the IOUserVideoClockDevice.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
IOUserVideoTransportType GetTransportType();
```

#### Return Value

The transport type of the clock device.

#### Discussion

The object’s work queue synchronizes access to this value.

## See Also

- [SetTransportType](iouservideoclockdevice/settransporttype.md)
  Sets the transport type of the clock device.
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
  The transport type of a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/gettransporttype)*