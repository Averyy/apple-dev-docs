# IOUSBDevReqOOL

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

An internal structure to pass parameters between IOUSBLib and UserClient.

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBDevReqOOL IOUSBDevReqOOL;
```

## Topics

### Getting the Properties
- [bmRequestType](./iousbdevreqool/api-1546195-bmrequesttype.md)
  The type of the request.
- [bRequest](./iousbdevreqool/api-1546179-brequest.md)
  The request code.
- [wValue](./iousbdevreqool/api-1546508-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](./iousbdevreqool/api-1546401-windex.md)
  The 16-bit parameter for the request.
- [wLength](./iousbdevreqool/api-1545970-wlength.md)
  The length of the data part of the request.
- [pData](./iousbdevreqool/api-1546153-pdata.md)
  The pointer to the data for the request.
- [wLenDone](./iousbdevreqool/api-1546159-wlendone.md)
  The number of data bytes that the system actually transferred.
- [pipeRef](./iousbdevreqool/api-1546299-piperef.md)
  A reference to the USB pipe.

## See Also

### Device Requests
- [IOUSBDevReqOOLTO](./iousbdevreqoolto.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevRequest](./iousbdevrequest.md)
  A structure that defines a standard device request.
- [IOUSBDevRequestTO](./iousbdevrequestto.md)
  A structure that defines a standard device request with timeout.
- [IOUSBDeviceRequest](./iousbdevicerequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequestPtr](./iousbdevicerequestptr.md)
  A pointer to a structure that defines a standard device request.
- [IOUSBDeviceRequestSetSELData](./iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevreqool)*