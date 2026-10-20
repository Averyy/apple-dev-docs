# bNumEndpoints

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The number of endpoints that this interface uses.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bNumEndpoints;
```

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The size of this descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  A constant value indicating an interface descriptor.
- [bInterfaceNumber](./binterfacenumber.md)
  The zero-based index of this interface in the current configuration.
- [bAlternateSetting](./balternatesetting.md)
  The alternative setting for the interface.
- [bInterfaceClass](./binterfaceclass.md)
  The class code indicating the behavior of this interface.
- [bInterfaceSubClass](./binterfacesubclass.md)
  The subclass code that further defines the behavior of this interface.
- [bInterfaceProtocol](./binterfaceprotocol.md)
  The protocol that this interface supports.
- [iInterface](./iinterface.md)
  The index of a string descriptor that describes this interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbinterfacedescriptor/bnumendpoints)*