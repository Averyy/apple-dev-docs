# IOUSBDevReqOOLTO

**Framework**: Kernel  
**Kind**: tdef

An internal structure to pass parameters between IOUSBLib and UserClient.

**Availability**:
- macOS 10.1+

## Declaration

```swift
typedef struct IOUSBDevReqOOLTO IOUSBDevReqOOLTO;
```

## Topics

### Getting the Properties
- [bmRequestType](iousbdevreqoolto/1546443-bmrequesttype.md)
  The type of the request.
- [bRequest](iousbdevreqoolto/1546099-brequest.md)
  The request code.
- [wValue](iousbdevreqoolto/1546109-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](iousbdevreqoolto/1545920-windex.md)
  The 16-bit parameter for the request.
- [wLength](iousbdevreqoolto/1546286-wlength.md)
  The length of the data part of the request.
- [pData](iousbdevreqoolto/1546044-pdata.md)
  The pointer to the data for the request.
- [wLenDone](iousbdevreqoolto/1546113-wlendone.md)
  The number of data bytes that the system actually transferred.
- [pipeRef](iousbdevreqoolto/1546157-piperef.md)
  A reference to the USB pipe.
- [completionTimeout](iousbdevreqoolto/1546368-completiontimeout.md)
  The value of the completion timeout in milliseconds.
- [noDataTimeout](iousbdevreqoolto/1546132-nodatatimeout.md)
  The value of the completion timeout in milliseconds if there’s no data.

## See Also

- [IOUSBDevReqOOL](iousbdevreqool.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevRequest](iousbdevrequest.md)
  A structure that defines a standard device request.
- [IOUSBDevRequestTO](iousbdevrequestto.md)
  A structure that defines a standard device request with timeout.
- [IOUSBDeviceRequest](iousbdevicerequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequestPtr](iousbdevicerequestptr.md)
  A pointer to a structure that defines a standard device request.
- [IOUSBDeviceRequestSetSELData](iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevreqoolto)*