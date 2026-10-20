# GetTransportType

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the transport type of the IOUserVideoClockDevice.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
IOUserVideoTransportType GetTransportType();
```

#### Return Value

The transport type of the clock device.

#### Discussion

The object’s work queue synchronizes access to this value.

## See Also

### Working with transport type
- [SetTransportType](./settransporttype.md)
  Sets the transport type of the clock device.
- [IOUserVideoTransportType](../videodriverkit-page/iouservideotransporttype.md)
  The transport type of a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/gettransporttype)*