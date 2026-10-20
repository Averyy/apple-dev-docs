# kIOUSBHostPortStatusResetting

**Framework**: USBDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A port that is currently resetting the link.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
kIOUSBHostPortStatusResetting
```

## See Also

### Getting the Port Status Flags
- [kIOUSBHostPortStatusPortTypeMask](./kiousbhostportstatusporttypemask.md)
  A mask for isolating the port bits.
- [kIOUSBHostPortStatusPortTypePhase](./kiousbhostportstatusporttypephase.md)
  The starting phase for port types.
- [kIOUSBHostPortStatusPortTypeStandard](./kiousbhostportstatusporttypestandard.md)
  A general-purpose USB port.
- [kIOUSBHostPortStatusPortTypeCaptive](./kiousbhostportstatusporttypecaptive.md)
  A device that cannot be physically disconnected from the port.
- [kIOUSBHostPortStatusPortTypeInternal](./kiousbhostportstatusporttypeinternal.md)
  A device that cannot be physically disconnected from the host machine.
- [kIOUSBHostPortStatusPortTypeAccessory](./kiousbhostportstatusporttypeaccessory.md)
  A device that might require authentication before drivers can access it.
- [kIOUSBHostPortStatusPortTypeReserved](./kiousbhostportstatusporttypereserved.md)
  A mask for isolating reserved port types.
- [kIOUSBHostPortStatusConnectedSpeedMask](./kiousbhostportstatusconnectedspeedmask.md)
  A mask for isolating the connection state bits.
- [kIOUSBHostPortStatusConnectedSpeedPhase](./kiousbhostportstatusconnectedspeedphase.md)
  The initial phase for connected state bits.
- [kIOUSBHostPortStatusConnectedSpeedNone](./kiousbhostportstatusconnectedspeednone.md)
  A port with no device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedFull](./kiousbhostportstatusconnectedspeedfull.md)
  A port with a full-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedLow](./kiousbhostportstatusconnectedspeedlow.md)
  A port with a low-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedHigh](./kiousbhostportstatusconnectedspeedhigh.md)
  A port with a high-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedSuper](./kiousbhostportstatusconnectedspeedsuper.md)
  A port with a super-speed device connected to it.
- [kIOUSBHostPortStatusConnectedSpeedSuperPlus](./kiousbhostportstatusconnectedspeedsuperplus.md)
  A port with a super-speed plus device connected to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbhostportstatus/kiousbhostportstatusresetting)*