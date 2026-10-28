# IOUSBDeviceRequest

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that defines a standard device request.

**Availability**:
- macOS 10.15+

## Declaration

```c
typedef struct IOUSBDeviceRequest IOUSBDeviceRequest;
```

## Discussion

For information about device requests, see USB 3.2, 9.3.

## Topics

### Instance Properties
- [bRequest](./iousbdevicerequest/api-3166572-brequest.md)
- [bmRequestType](./iousbdevicerequest/api-3166573-bmrequesttype.md)
- [wIndex](./iousbdevicerequest/api-3166574-windex.md)
- [wLength](./iousbdevicerequest/api-3166575-wlength.md)
- [wValue](./iousbdevicerequest/api-3166576-wvalue.md)

## See Also

### Device Requests
- [IOUSBDevReqOOL](./iousbdevreqool.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevReqOOLTO](./iousbdevreqoolto.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevRequest](./iousbdevrequest.md)
  A structure that defines a standard device request.
- [IOUSBDevRequestTO](./iousbdevrequestto.md)
  A structure that defines a standard device request with timeout.
- [IOUSBDeviceRequestPtr](./iousbdevicerequestptr.md)
  A pointer to a structure that defines a standard device request.
- [IOUSBDeviceRequestSetSELData](./iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicerequest)*