# IOUSBDeviceRequestSetSELData

**Framework**: Kernel  
**Kind**: tdef

The structure for receiving system exit latency values.

**Availability**:
- macOS 10.15+

## Declaration

```swift
typedef struct IOUSBDeviceRequestSetSELData IOUSBDeviceRequestSetSELData;
```

#### Discussion

For information about the `Set SEL` request type, see USB 3.2, 9.4.12.

## Topics

### Instance Properties
- [u1Pel](iousbdevicerequestsetseldata/3166578-u1pel.md)
- [u1Sel](iousbdevicerequestsetseldata/3166579-u1sel.md)
- [u2Pel](iousbdevicerequestsetseldata/3166580-u2pel.md)
- [u2Sel](iousbdevicerequestsetseldata/3166581-u2sel.md)

## See Also

- [IOUSBDevReqOOL](iousbdevreqool.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevReqOOLTO](iousbdevreqoolto.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBDevRequest](iousbdevrequest.md)
  A structure that defines a standard device request.
- [IOUSBDevRequestTO](iousbdevrequestto.md)
  A structure that defines a standard device request with timeout.
- [IOUSBDeviceRequest](iousbdevicerequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequestPtr](iousbdevicerequestptr.md)
  A pointer to a structure that defines a standard device request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicerequestsetseldata)*