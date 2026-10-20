# kIOUSBHostPortTypeStandard

**Framework**: USBDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A general-purpose USB port.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
kIOUSBHostPortTypeStandard
```

## See Also

### Getting the Port Types
- [kIOUSBHostPortTypeCaptive](./kiousbhostporttypecaptive.md)
  A port for which the device cannot be physically disconnected.
- [kIOUSBHostPortTypeInternal](./kiousbhostporttypeinternal.md)
  A port that cannot be physically disconnected from the host machine.
- [kIOUSBHostPortTypeAccessory](./kiousbhostporttypeaccessory.md)
  A port for which the device might require additional authentication before a driver can access it.
- [kIOUSBHostPortTypeExpressCard](./kiousbhostporttypeexpresscard.md)
  A port containing an expansion card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbhostporttype/kiousbhostporttypestandard)*