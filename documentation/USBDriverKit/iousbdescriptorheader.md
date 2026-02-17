# IOUSBDescriptorHeader

**Framework**: USBDriverKit  
**Kind**: struct

The base descriptor header.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBDescriptorHeader;
```

#### Overview

For more information about descriptors, see section 9.5 of the USB 2.0 specification at [`https://www.usb.org/`](https://developer.apple.comhttps://www.usb.org/).

## Topics

### Getting the Descriptor Properties
- [bLength](iousbdescriptorheader/blength.md)
  The number of bytes in the descriptor.
- [bDescriptorType](iousbdescriptorheader/bdescriptortype.md)
  The type of the descriptor.

## See Also

- [IOUSBDescriptor](iousbdescriptor.md)
  The base descriptor type.
- [tIOUSBDescriptorType](tiousbdescriptortype.md)
  Constants describing the types of descriptors available for a USB device.
- [tIOUSBDescriptorSize](tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbdescriptorheader)*