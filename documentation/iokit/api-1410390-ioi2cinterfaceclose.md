# IOI2CInterfaceClose

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Closes an IOI2CConnectRef.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn IOI2CInterfaceClose(IOI2CConnectRef connect, IOOptionBits options);
```

## Return Value

An IOReturn code.

## Discussion

Frees the resources associated with an IOI2CConnectRef.

## Parameters

- `connect`: The opaque IOI2CConnectRef returned by IOI2CInterfaceOpen().
- `options`: Pass kNilOptions.

## See Also

### Miscellaneous
- [IOFBCopyI2CInterfaceForBus](./api-1410345-iofbcopyi2cinterfaceforbus.md)
  Returns an instance of an I2C bus interface, associated with an IOFramebuffer instance / bus index pair.
- [IOFBGetI2CInterfaceCount](./api-1410333-iofbgeti2cinterfacecount.md)
  Returns a count of I2C interfaces available associated with an IOFramebuffer instance.
- [IOI2CInterfaceOpen](./api-1410388-ioi2cinterfaceopen.md)
  Opens an instance of an I2C bus interface, allowing I2C requests to be made.
- [IOI2CSendRequest](./api-1410373-ioi2csendrequest.md)
  Carries out the I2C transaction specified by an IOI2CRequest structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1410390-ioi2cinterfaceclose)*