# IOI2CInterface.h User-Space

**Framework**: IOKit  
**Role**: API Collection

## Topics

### Miscellaneous
- [IOFBCopyI2CInterfaceForBus](./api-1410345-iofbcopyi2cinterfaceforbus.md)
  Returns an instance of an I2C bus interface, associated with an IOFramebuffer instance / bus index pair.
- [IOFBGetI2CInterfaceCount](./api-1410333-iofbgeti2cinterfacecount.md)
  Returns a count of I2C interfaces available associated with an IOFramebuffer instance.
- [IOI2CInterfaceClose](./api-1410390-ioi2cinterfaceclose.md)
  Closes an IOI2CConnectRef.
- [IOI2CInterfaceOpen](./api-1410388-ioi2cinterfaceopen.md)
  Opens an instance of an I2C bus interface, allowing I2C requests to be made.
- [IOI2CSendRequest](./api-1410373-ioi2csendrequest.md)
  Carries out the I2C transaction specified by an IOI2CRequest structure.
### Data Types
- [IOI2CBusTiming](./ioi2cinterface_h_user-space/ioi2cbustiming.md)
  A structure defining low level timing for an I2C bus.
- [IOI2CRequest](./ioi2cinterface_h_user-space/ioi2crequest.md)
  A structure defining an I2C bus transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioi2cinterface_h_user-space)*