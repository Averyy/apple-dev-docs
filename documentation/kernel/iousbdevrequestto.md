# IOUSBDevRequestTO

**Framework**: Kernel  
**Kind**: tdef

A structure that defines a standard device request with timeout.

**Availability**:
- macOS 10.1+

## Declaration

```swift
typedef struct IOUSBDevRequestTO IOUSBDevRequestTO;
```

## Topics

### Getting the Properties
- [bmRequestType](iousbdevrequestto/1546240-bmrequesttype.md)
  The type of the request.
- [bRequest](iousbdevrequestto/1546186-brequest.md)
  The request code.
- [wValue](iousbdevrequestto/1546569-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](iousbdevrequestto/1545983-windex.md)
  The 16-bit parameter for the request.
- [wLength](iousbdevrequestto/1546424-wlength.md)
  The length of the data part of the request.
- [pData](iousbdevrequestto/1546393-pdata.md)
  The pointer to the data for the request.
- [wLenDone](iousbdevrequestto/1546065-wlendone.md)
  The number of data bytes that the system actually transferred.
- [completionTimeout](iousbdevrequestto/1546188-completiontimeout.md)
  The value of the completion timeout in milliseconds.
- [noDataTimeout](iousbdevrequestto/1546538-nodatatimeout.md)
  The value of the completion timeout in milliseconds if there’s no data.

## See Also

- [IOUSBDevReqOOL](iousbdevreqool.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevReqOOLTO](iousbdevreqoolto.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevRequest](iousbdevrequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequest](iousbdevicerequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequestPtr](iousbdevicerequestptr.md)
  A pointer to a structure that defines a standard device request.
- [IOUSBDeviceRequestSetSELData](iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevrequestto)*