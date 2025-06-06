# tIOUSBHostConnectionSpeed

**Framework**: USBDriverKit  
**Kind**: enum

Constants indicating the connection speed of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBHostConnectionSpeed : unsigned int;
```

#### Discussion

This enumeration matches the default speed ID mappings defined in XHCI 1.0 Table 147.

## Topics

### Getting the Connection Speeds
- [kIOUSBHostConnectionSpeedNone](tiousbhostconnectionspeed/kiousbhostconnectionspeednone.md)
  No device is connected.
- [kIOUSBHostConnectionSpeedFull](tiousbhostconnectionspeed/kiousbhostconnectionspeedfull.md)
  The connected device runs at 12 megabits per second.
- [kIOUSBHostConnectionSpeedLow](tiousbhostconnectionspeed/kiousbhostconnectionspeedlow.md)
  The connected device runs at 1.5 megabits per second.
- [kIOUSBHostConnectionSpeedHigh](tiousbhostconnectionspeed/kiousbhostconnectionspeedhigh.md)
  The connected device runs at 480 megabits per second.
- [kIOUSBHostConnectionSpeedSuper](tiousbhostconnectionspeed/kiousbhostconnectionspeedsuper.md)
  The connected device runs at 5 gigabits per second.
- [kIOUSBHostConnectionSpeedSuperPlus](tiousbhostconnectionspeed/kiousbhostconnectionspeedsuperplus.md)
  The connected device runs at 10 gigabits per second.
- [kIOUSBHostConnectionSpeedSuperPlusBy2](tiousbhostconnectionspeed/kiousbhostconnectionspeedsuperplusby2.md)
  The connected device runs at 20 gigabits per second.
- [kIOUSBHostConnectionSpeedCount](tiousbhostconnectionspeed/kiousbhostconnectionspeedcount.md)
  The number of available connection speed values.

## See Also

- [GetAddress](iousbhostdevice/getaddress.md)
  Returns the address of the device.
- [GetSpeed](iousbhostdevice/getspeed.md)
  Retrieves the device’s operational speed.
- [GetFrameNumber](iousbhostdevice/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostdevice/getportstatus.md)
  Returns the current port status of the device.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](tiousbhostporttype.md)
  Constants indicating a port’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbhostconnectionspeed)*