# IOFBGetI2CInterfaceCount

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns a count of I2C interfaces available associated with an IOFramebuffer instance.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn IOFBGetI2CInterfaceCount(io_service_t framebuffer, IOItemCount *count);
```

#### Return Value

An IOReturn code.

#### Discussion

Returns a count of I2C interfaces available associated with an IOFramebuffer instance.

## Parameters

- `framebuffer`: The io_service_t of an IOFramebuffer instance. CoreGraphics will provide this for a CGDisplay with the CGDisplayIOServicePort() call.
- `count`: Interface count is returned.

## See Also

### Miscellaneous
- [IOFBCopyI2CInterfaceForBus](./api-1410345-iofbcopyi2cinterfaceforbus.md)
  Returns an instance of an I2C bus interface, associated with an IOFramebuffer instance / bus index pair.
- [IOI2CInterfaceClose](./api-1410390-ioi2cinterfaceclose.md)
  Closes an IOI2CConnectRef.
- [IOI2CInterfaceOpen](./api-1410388-ioi2cinterfaceopen.md)
  Opens an instance of an I2C bus interface, allowing I2C requests to be made.
- [IOI2CSendRequest](./api-1410373-ioi2csendrequest.md)
  Carries out the I2C transaction specified by an IOI2CRequest structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1410333-iofbgeti2cinterfacecount)*