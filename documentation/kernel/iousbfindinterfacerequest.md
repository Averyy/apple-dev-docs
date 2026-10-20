# IOUSBFindInterfaceRequest

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

The structure for finding an interface request.

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBFindInterfaceRequest IOUSBFindInterfaceRequest;
```

## Topics

### Getting the Properties
- [bAlternateSetting](./iousbfindinterfacerequest/api-1546002-balternatesetting.md)
  The alternative setting to find.
- [bInterfaceClass](./iousbfindinterfacerequest/api-1546291-binterfaceclass.md)
  The interface class to find.
- [bInterfaceProtocol](./iousbfindinterfacerequest/api-1546022-binterfaceprotocol.md)
  The interface protocol to find.
- [bInterfaceSubClass](./iousbfindinterfacerequest/api-1546058-binterfacesubclass.md)
  The interface subclass to find.

## See Also

### Communication Requests
- [IOUSBBulkPipeReq](./iousbbulkpipereq.md)
  The structure that represents a bulk pipe request.
- [IOUSBFindEndpointRequest](./iousbfindendpointrequest.md)
  The structure that represents an endoint request to locate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbfindinterfacerequest)*