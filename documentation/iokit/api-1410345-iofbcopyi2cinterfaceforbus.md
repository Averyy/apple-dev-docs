# IOFBCopyI2CInterfaceForBus

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns an instance of an I2C bus interface, associated with an IOFramebuffer instance / bus index pair.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn IOFBCopyI2CInterfaceForBus(io_service_t framebuffer, IOOptionBits bus, io_service_t *interface);
```

## Return Value

An IOReturn code.

## Discussion

Some graphics devices will allow access to an I2C bus routed through a display connector in order to control external devices on that bus. This function returns an instance of an I2C bus interface, associated with an IOFramebuffer instance / bus index pair. The number of I2C buses is available from the IOFBGetI2CInterfaceCount() call. The interface may be used with the IOI2CInterfaceOpen/Close/SendRequest() calls to carry out I2C transactions on that bus. Not all graphics devices support this functionality.

## Parameters

- `bus`: The zero based index of the bus on the requested framebuffer.
- `interface`: The interface instance is returned. The caller should release this instance with IOObjectRelease().

## See Also

### Miscellaneous
- [IOFBGetI2CInterfaceCount](./api-1410333-iofbgeti2cinterfacecount.md)
  Returns a count of I2C interfaces available associated with an IOFramebuffer instance.
- [IOI2CInterfaceClose](./api-1410390-ioi2cinterfaceclose.md)
  Closes an IOI2CConnectRef.
- [IOI2CInterfaceOpen](./api-1410388-ioi2cinterfaceopen.md)
  Opens an instance of an I2C bus interface, allowing I2C requests to be made.
- [IOI2CSendRequest](./api-1410373-ioi2csendrequest.md)
  Carries out the I2C transaction specified by an IOI2CRequest structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1410345-iofbcopyi2cinterfaceforbus)*