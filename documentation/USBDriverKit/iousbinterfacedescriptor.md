# IOUSBInterfaceDescriptor

**Framework**: USBDriverKit  
**Kind**: struct

A descriptor for a specific interface of a USB device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBInterfaceDescriptor;
```

#### Overview

An [`IOUSBInterfaceDescriptor`](iousbinterfacedescriptor.md) object contains information about one of the device’s supported interfaces. A device’s configuration provides one or more interfaces, each with zero or more endpoints that define how to configure the pipes for that device.

For more information about this descriptor type, see section 9.6.5 of the USB 2.0 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Accessing the Descriptor Properties
- [bLength](iousbinterfacedescriptor/blength.md)
  The size of this descriptor in bytes.
- [bDescriptorType](iousbinterfacedescriptor/bdescriptortype.md)
  A constant value indicating an interface descriptor.
- [bInterfaceNumber](iousbinterfacedescriptor/binterfacenumber.md)
  The zero-based index of this interface in the current configuration.
- [bAlternateSetting](iousbinterfacedescriptor/balternatesetting.md)
  The alternative setting for the interface.
- [bNumEndpoints](iousbinterfacedescriptor/bnumendpoints.md)
  The number of endpoints that this interface uses.
- [bInterfaceClass](iousbinterfacedescriptor/binterfaceclass.md)
  The class code indicating the behavior of this interface.
- [bInterfaceSubClass](iousbinterfacedescriptor/binterfacesubclass.md)
  The subclass code that further defines the behavior of this interface.
- [bInterfaceProtocol](iousbinterfacedescriptor/binterfaceprotocol.md)
  The protocol that this interface supports.
- [iInterface](iousbinterfacedescriptor/iinterface.md)
  The index of a string descriptor that describes this interface.

## See Also

- [IOUSBInterfaceAssociationDescriptor](iousbinterfaceassociationdescriptor.md)
  The USB Interface Association Descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbinterfacedescriptor)*