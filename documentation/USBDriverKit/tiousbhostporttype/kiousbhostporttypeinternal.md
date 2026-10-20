# kIOUSBHostPortTypeInternal

**Framework**: USBDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A port that cannot be physically disconnected from the host machine.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
kIOUSBHostPortTypeInternal
```

## See Also

### Getting the Port Types
- [kIOUSBHostPortTypeStandard](./kiousbhostporttypestandard.md)
  A general-purpose USB port.
- [kIOUSBHostPortTypeCaptive](./kiousbhostporttypecaptive.md)
  A port for which the device cannot be physically disconnected.
- [kIOUSBHostPortTypeAccessory](./kiousbhostporttypeaccessory.md)
  A port for which the device might require additional authentication before a driver can access it.
- [kIOUSBHostPortTypeExpressCard](./kiousbhostporttypeexpresscard.md)
  A port containing an expansion card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbhostporttype/kiousbhostporttypeinternal)*