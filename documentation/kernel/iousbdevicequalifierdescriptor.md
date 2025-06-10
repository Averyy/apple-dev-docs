# IOUSBDeviceQualifierDescriptor

**Framework**: Kernel  
**Kind**: tdef

The structure for describing a high-speed capable USB device.

**Availability**:
- macOS 10.2+

## Declaration

```swift
typedef struct IOUSBDeviceQualifierDescriptor IOUSBDeviceQualifierDescriptor;
```

#### Discussion

For information about this descriptor, see USB 2.0, 9.6.2.

## Topics

### Getting the Properties
- [bLength](iousbdevicequalifierdescriptor/1546586-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbdevicequalifierdescriptor/1546232-bdescriptortype.md)
  The type of the descriptor.
- [bcdUSB](iousbdevicequalifierdescriptor/1546098-bcdusb.md)
  The USB specification version number.
- [bDeviceClass](iousbdevicequalifierdescriptor/1546116-bdeviceclass.md)
  The class code.
- [bDeviceSubClass](iousbdevicequalifierdescriptor/1546256-bdevicesubclass.md)
  The subclass code.
- [bDeviceProtocol](iousbdevicequalifierdescriptor/1546390-bdeviceprotocol.md)
  The protocol code.
- [bMaxPacketSize0](iousbdevicequalifierdescriptor/1546534-bmaxpacketsize0.md)
  The maximum packet size for other speed.
- [bNumConfigurations](iousbdevicequalifierdescriptor/1546367-bnumconfigurations.md)
  The number of other-speed configurations.
- [bReserved](iousbdevicequalifierdescriptor/1546522-breserved.md)
  Reserved for future use.

## See Also

- [IOUSBDeviceDescriptor](iousbdevicedescriptor.md)
  The structure for storing a USB device descriptor.
- [IOUSBDeviceDescriptorPtr](iousbdevicedescriptorptr.md)
  A pointer to a USB device descriptor.
- [IOUSBDeviceQualifierDescriptorPtr](iousbdevicequalifierdescriptorptr.md)
  A pointer to a qualifier descriptor.
- [IOUSBDeviceQualifierDescriptor](../iokit/usb_h_user-space/iousbdevicequalifierdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicequalifierdescriptor)*