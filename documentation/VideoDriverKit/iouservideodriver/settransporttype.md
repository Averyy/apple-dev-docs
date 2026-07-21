# SetTransportType

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetTransportType(IOUserVideoTransportType in_transport_type);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the transport type of the IOUserVideoDriver

Transport type can be changed dynamically.  A notification will be sent to the host to update the object state if successful.

## Parameters

- `in_transport_type`: IOUserVideoTransportType to set.

## See Also

- [GetTransportType](iouservideodriver/gettransporttype.md)
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/settransporttype)*