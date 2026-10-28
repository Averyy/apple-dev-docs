# SetTransportType

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the transport type of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetTransportType(IOUserVideoTransportType in_transport_type);
```

## Discussion

Drivers can change the transport type of the clock device dynamically. The object sends a notification to the host to update the object state on success.

## Parameters

- `in_transport_type`: IOUserVideoTransportType to set

## See Also

### Working with transport type
- [GetTransportType](./gettransporttype.md)
  Gets the transport type of the IOUserVideoClockDevice.
- [IOUserVideoTransportType](../videodriverkit-page/iouservideotransporttype.md)
  The transport type of a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/settransporttype)*