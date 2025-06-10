# IOUSBBulkPipeReq

**Framework**: Kernel  
**Kind**: tdef

The structure that represents a bulk pipe request.

**Availability**:
- macOS 10.1+

## Declaration

```swift
typedef struct IOUSBBulkPipeReq IOUSBBulkPipeReq;
```

## Topics

### Getting the Properties
- [pipeRef](iousbbulkpipereq/1545941-piperef.md)
  A reference to the USB pipe.
- [buf](iousbbulkpipereq/1546177-buf.md)
  A pointer to the request buffer.
- [size](iousbbulkpipereq/1546366-size.md)
  The requested size of the pipe.
- [noDataTimeout](iousbbulkpipereq/1546036-nodatatimeout.md)
  The timeout if no data is available.
- [completionTimeout](iousbbulkpipereq/1545958-completiontimeout.md)
  The completion timeout value.

## See Also

- [IOUSBFindInterfaceRequest](iousbfindinterfacerequest.md)
  The structure for finding an interface request.
- [IOUSBFindEndpointRequest](iousbfindendpointrequest.md)
  The structure that represents an endoint request to locate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbbulkpipereq)*