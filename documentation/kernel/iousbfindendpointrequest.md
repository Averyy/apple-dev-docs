# IOUSBFindEndpointRequest

**Framework**: Kernel  
**Kind**: tdef

The structure that represents an endoint request to locate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOUSBFindEndpointRequest IOUSBFindEndpointRequest;
```

## Topics

### Getting the Properties
- [type](iousbfindendpointrequest/1546255-type.md)
  The type of endpoint.
- [direction](iousbfindendpointrequest/1546504-direction.md)
  The direction of the endpoint.
- [maxPacketSize](iousbfindendpointrequest/1546175-maxpacketsize.md)
  The maximum packet size of the endpoint.
- [interval](iousbfindendpointrequest/1546078-interval.md)
  The polling interval for the endpoint in milliseconds.

## See Also

- [IOUSBFindInterfaceRequest](iousbfindinterfacerequest.md)
  The structure for finding an interface request.
- [IOUSBBulkPipeReq](iousbbulkpipereq.md)
  The structure that represents a bulk pipe request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbfindendpointrequest)*