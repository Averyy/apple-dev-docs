# SetTransportType

**Framework**: VideoDriverKit  
**Kind**: method

Sets the transport type of the clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetTransportType(IOUserVideoTransportType in_transport_type);
```

#### Discussion

Drivers can change the transport type of the clock device dynamically. The object sends a notification to the host to update the object state on success.

## Parameters

- `in_transport_type`: IOUserVideoTransportType to set

## See Also

- [GetTransportType](iouservideoclockdevice/gettransporttype.md)
  Gets the transport type of the IOUserVideoClockDevice.
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
  The transport type of a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/settransporttype)*