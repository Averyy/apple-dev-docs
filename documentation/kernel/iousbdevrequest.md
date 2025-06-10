# IOUSBDevRequest

**Framework**: Kernel  
**Kind**: tdef

A structure that defines a standard device request.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOUSBDevRequest IOUSBDevRequest;
```

## Topics

### Getting the Properties
- [bmRequestType](iousbdevrequest/1546317-bmrequesttype.md)
  The type of the request.
- [bRequest](iousbdevrequest/1546404-brequest.md)
  The request code.
- [wValue](iousbdevrequest/1546433-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](iousbdevrequest/1546579-windex.md)
  The 16-bit parameter for the request.
- [wLength](iousbdevrequest/1545928-wlength.md)
  The length of the data part of the request.
- [pData](iousbdevrequest/1546431-pdata.md)
  The pointer to the data for the request.
- [wLenDone](iousbdevrequest/1546308-wlendone.md)
  The number of data bytes that the system actually transferred.

## See Also

- [IOUSBDevReqOOL](iousbdevreqool.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevReqOOLTO](iousbdevreqoolto.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevRequestTO](iousbdevrequestto.md)
  A structure that defines a standard device request with timeout.
- [IOUSBDeviceRequest](iousbdevicerequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequestPtr](iousbdevicerequestptr.md)
  A pointer to a structure that defines a standard device request.
- [IOUSBDeviceRequestSetSELData](iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevrequest)*