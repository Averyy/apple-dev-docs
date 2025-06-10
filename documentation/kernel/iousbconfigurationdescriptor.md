# IOUSBConfigurationDescriptor

**Framework**: Kernel  
**Kind**: tdef

The structure for storing a USB configuration descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOUSBConfigurationDescriptor IOUSBConfigurationDescriptor;
```

#### Discussion

This descriptor contains information about a specific configuration of a device, including the interfaces that configuration provides. This structure has a variable length so it defines only the known fields. Use the `wTotalLength` field to read the entire descriptor.

For more information about this descriptor type, see USB 3.2, 9.6.3.

## Topics

### Getting the Properties
- [bLength](iousbconfigurationdescriptor/1546137-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbconfigurationdescriptor/1546155-bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](iousbconfigurationdescriptor/1546253-wtotallength.md)
  The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.
- [bNumInterfaces](iousbconfigurationdescriptor/1546162-bnuminterfaces.md)
  The number of interfaces this configuration supports.
- [bConfigurationValue](iousbconfigurationdescriptor/1546567-bconfigurationvalue.md)
  The value to use when selecting this configuration.
- [iConfiguration](iousbconfigurationdescriptor/1546218-iconfiguration.md)
  The index of the string descriptor that describes this configuration.
- [bmAttributes](iousbconfigurationdescriptor/1546539-bmattributes.md)
  A bit mask indicating the configuration’s characteristics.
- [MaxPower](iousbconfigurationdescriptor/1545938-maxpower.md)
  The maximum power consumption of the USB device expressed in 2 milliamp units.

## See Also

- [IOUSBConfigurationDescHeader](iousbconfigurationdescheader.md)
  The header of a configuration descriptor.
- [IOUSBConfigurationDescriptorPtr](iousbconfigurationdescriptorptr.md)
  A pointer to a configuration descriptor.
- [IOUSBConfigurationDescHeaderPtr](iousbconfigurationdescheaderptr.md)
  A pointer to a configuration descriptor header.
- [IOUSBConfigurationDescriptor](../iokit/usb_h_user-space/iousbconfigurationdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbconfigurationdescriptor)*