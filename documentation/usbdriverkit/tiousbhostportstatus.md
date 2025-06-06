# tIOUSBHostPortStatus

**Framework**: USBDriverKit  
**Kind**: enum

Constants indicating the state of a port.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBHostPortStatus : unsigned int;
```

## Topics

### Getting the Port Status Flags
- [kIOUSBHostPortStatusPortTypeMask](tiousbhostportstatus/kiousbhostportstatusporttypemask.md)
  A mask for isolating the port bits.
- [kIOUSBHostPortStatusPortTypePhase](tiousbhostportstatus/kiousbhostportstatusporttypephase.md)
  The starting phase for port types.
- [kIOUSBHostPortStatusPortTypeStandard](tiousbhostportstatus/kiousbhostportstatusporttypestandard.md)
  A general-purpose USB port.
- [kIOUSBHostPortStatusPortTypeCaptive](tiousbhostportstatus/kiousbhostportstatusporttypecaptive.md)
  A device that cannot be physically disconnected from the port.
- [kIOUSBHostPortStatusPortTypeInternal](tiousbhostportstatus/kiousbhostportstatusporttypeinternal.md)
  A device that cannot be physically disconnected from the host machine.
- [kIOUSBHostPortStatusPortTypeAccessory](tiousbhostportstatus/kiousbhostportstatusporttypeaccessory.md)
  A device that might require authentication before drivers can access it.
- [kIOUSBHostPortStatusPortTypeReserved](tiousbhostportstatus/kiousbhostportstatusporttypereserved.md)
  A mask for isolating reserved port types.
- [kIOUSBHostPortStatusConnectedSpeedMask](tiousbhostportstatus/kiousbhostportstatusconnectedspeedmask.md)
  A mask for isolating the connection state bits.
- [kIOUSBHostPortStatusConnectedSpeedPhase](tiousbhostportstatus/kiousbhostportstatusconnectedspeedphase.md)
  The initial phase for connected state bits.
- [kIOUSBHostPortStatusConnectedSpeedNone](tiousbhostportstatus/kiousbhostportstatusconnectedspeednone.md)
  A port with no device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedFull](tiousbhostportstatus/kiousbhostportstatusconnectedspeedfull.md)
  A port with a full-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedLow](tiousbhostportstatus/kiousbhostportstatusconnectedspeedlow.md)
  A port with a low-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedHigh](tiousbhostportstatus/kiousbhostportstatusconnectedspeedhigh.md)
  A port with a high-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedSuper](tiousbhostportstatus/kiousbhostportstatusconnectedspeedsuper.md)
  A port with a super-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedSuperPlus](tiousbhostportstatus/kiousbhostportstatusconnectedspeedsuperplus.md)
  A port with a super-speed plus device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedSuperPlusBy2](tiousbhostportstatus/kiousbhostportstatusconnectedspeedsuperplusby2.md)
  A port with a super-speed plus two device connected to it.
- [kIOUSBHostPortStatusResetting](tiousbhostportstatus/kiousbhostportstatusresetting.md)
  A port that is currently resetting the link.
- [kIOUSBHostPortStatusEnabled](tiousbhostportstatus/kiousbhostportstatusenabled.md)
  A port that is enabled and allows packets to reach the device.
- [kIOUSBHostPortStatusSuspended](tiousbhostportstatus/kiousbhostportstatussuspended.md)
  A port that is suspended.
- [kIOUSBHostPortStatusOvercurrent](tiousbhostportstatus/kiousbhostportstatusovercurrent.md)
  A port that is in the overcurrent condition.
- [kIOUSBHostPortStatusTestMode](tiousbhostportstatus/kiousbhostportstatustestmode.md)
  A port that is in test mode.

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
- [tIOUSBHostPortType](tiousbhostporttype.md)
  Constants indicating a port’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbhostportstatus)*