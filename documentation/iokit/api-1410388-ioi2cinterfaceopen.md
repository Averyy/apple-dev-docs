# IOI2CInterfaceOpen

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Opens an instance of an I2C bus interface, allowing I2C requests to be made.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn IOI2CInterfaceOpen(io_service_t interface, IOOptionBits options, IOI2CConnectRef *connect);
```

#### Return Value

An IOReturn code.

#### Discussion

An instance of an I2C bus interface, obtained by IOFBCopyI2CInterfaceForBus, is opened with this function allowing I2C requests to be made.

## Parameters

- `interface`: An I2C bus interface (see IOFBCopyI2CInterfaceForBus). The interface may be released after this call is made.
- `options`: Pass kNilOptions.
- `connect`: The opaque IOI2CConnectRef is returned, for use with IOI2CSendRequest() and IOI2CInterfaceClose().

## See Also

### Miscellaneous
- [IOFBCopyI2CInterfaceForBus](./api-1410345-iofbcopyi2cinterfaceforbus.md)
  Returns an instance of an I2C bus interface, associated with an IOFramebuffer instance / bus index pair.
- [IOFBGetI2CInterfaceCount](./api-1410333-iofbgeti2cinterfacecount.md)
  Returns a count of I2C interfaces available associated with an IOFramebuffer instance.
- [IOI2CInterfaceClose](./api-1410390-ioi2cinterfaceclose.md)
  Closes an IOI2CConnectRef.
- [IOI2CSendRequest](./api-1410373-ioi2csendrequest.md)
  Carries out the I2C transaction specified by an IOI2CRequest structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1410388-ioi2cinterfaceopen)*