# tIOUSBHostPortType

**Framework**: USBDriverKit  
**Kind**: enum

Constants indicating a port’s type.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBHostPortType : unsigned int;
```

## Topics

### Getting the Port Types
- [kIOUSBHostPortTypeStandard](tiousbhostporttype/kiousbhostporttypestandard.md)
  A general-purpose USB port.
- [kIOUSBHostPortTypeCaptive](tiousbhostporttype/kiousbhostporttypecaptive.md)
  A port for which the device cannot be physically disconnected.
- [kIOUSBHostPortTypeInternal](tiousbhostporttype/kiousbhostporttypeinternal.md)
  A port that cannot be physically disconnected from the host machine.
- [kIOUSBHostPortTypeAccessory](tiousbhostporttype/kiousbhostporttypeaccessory.md)
  A port for which the device might require additional authentication before a driver can access it.
- [kIOUSBHostPortTypeExpressCard](tiousbhostporttype/kiousbhostporttypeexpresscard.md)
  A port containing an expansion card.
- [kIOUSBHostPortTypeCount](tiousbhostporttype/kiousbhostporttypecount.md)
  The number of port types.

## See Also

- [GetAddress](iousbhostdevice/getaddress.md)
  Returns the address of the device.
- [GetSpeed](iousbhostdevice/getspeed.md)
  Retrieves the device’s operational speed.
- [GetFrameNumber](iousbhostdevice/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostdevice/getportstatus.md)
  Returns the current port status of the device.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbhostporttype)*