# IOUSBDescriptor

**Framework**: USBDriverKit  
**Kind**: typealias

The base descriptor type.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
typedef IOUSBDescriptorHeader IOUSBDescriptor;
```

#### Discussion

Use this type to represent generic descriptor definitions. For more information about descriptors, see section 9.5 of the USB 2.0 specification at [`https://www.usb.org/`](https://developer.apple.comhttps://www.usb.org/).

## See Also

- [IOUSBDescriptorHeader](iousbdescriptorheader.md)
  The base descriptor header.
- [tIOUSBDescriptorType](tiousbdescriptortype.md)
  Constants describing the types of descriptors available for a USB device.
- [tIOUSBDescriptorSize](tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbdescriptor)*