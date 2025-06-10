# IOUSBInterfaceDescriptor

**Framework**: Kernel  
**Kind**: tdef

A descriptor for a specific interface of a USB device.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOUSBInterfaceDescriptor IOUSBInterfaceDescriptor;
```

#### Discussion

An `IOUSBInterfaceDescriptor` object contains information about one of the device’s supported interfaces. A device’s configuration provides one or more interfaces, each with zero or more endpoints that define how to configure the pipes for that device.

For more information about this descriptor type, see USB 3.2, 9.6.5.

## Topics

### Getting the Properties
- [bLength](iousbinterfacedescriptor/1546453-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbinterfacedescriptor/1546203-bdescriptortype.md)
  The type of the descriptor.
- [bInterfaceNumber](iousbinterfacedescriptor/1545982-binterfacenumber.md)
  The number of this interface.
- [bAlternateSetting](iousbinterfacedescriptor/1546130-balternatesetting.md)
  The value for selecting an alternative setting for the interface that the interface number references.
- [bNumEndpoints](iousbinterfacedescriptor/1546478-bnumendpoints.md)
  The number of endpoints that the interface uses.
- [bInterfaceClass](iousbinterfacedescriptor/1546292-binterfaceclass.md)
  The class code.
- [bInterfaceSubClass](iousbinterfacedescriptor/1546353-binterfacesubclass.md)
  The subclass code.
- [bInterfaceProtocol](iousbinterfacedescriptor/1545890-binterfaceprotocol.md)
  The protocol code.
- [iInterface](iousbinterfacedescriptor/1545956-iinterface.md)
  The index of the string descriptor describing this interface.

## See Also

- [IOUSBInterfaceDescriptorPtr](iousbinterfacedescriptorptr.md)
  A pointer to a USB interface descriptor.
- [IOUSBInterfaceAssociationDescriptor](iousbinterfaceassociationdescriptor.md)
  The descriptor that associates multiple interfaces to the same function.
- [IOUSBInterfaceAssociationDescriptorPtr](iousbinterfaceassociationdescriptorptr.md)
  A pointer to a USB interface association descriptor.
- [IOUSBInterfaceDescriptor](../iokit/usb_h_user-space/iousbinterfacedescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbinterfacedescriptor)*