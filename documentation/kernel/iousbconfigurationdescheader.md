# IOUSBConfigurationDescHeader

**Framework**: Kernel  
**Kind**: tdef

The header of a configuration descriptor.

**Availability**:
- macOS 10.1+

## Declaration

```swift
typedef struct IOUSBConfigurationDescHeader IOUSBConfigurationDescHeader;
```

#### Discussion

The header of a [`IOUSBConfigurationDescriptor`](https://developer.apple.com/documentation/iokit/iousbconfigurationdescriptor) that returns the total length of the descriptor.

## Topics

### Getting the Properties
- [bLength](iousbconfigurationdescheader/1546382-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbconfigurationdescheader/1546140-bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](iousbconfigurationdescheader/1546394-wtotallength.md)
  The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.

## See Also

- [IOUSBConfigurationDescriptor](iousbconfigurationdescriptor.md)
  The structure for storing a USB configuration descriptor.
- [IOUSBConfigurationDescriptorPtr](iousbconfigurationdescriptorptr.md)
  A pointer to a configuration descriptor.
- [IOUSBConfigurationDescHeaderPtr](iousbconfigurationdescheaderptr.md)
  A pointer to a configuration descriptor header.
- [IOUSBConfigurationDescHeader](../iokit/usb_h_user-space/iousbconfigurationdescheader.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbconfigurationdescheader)*