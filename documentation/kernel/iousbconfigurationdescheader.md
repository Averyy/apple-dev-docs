# IOUSBConfigurationDescHeader

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

The header of a configuration descriptor.

**Availability**:
- macOS 10.1+

## Declaration

```c
typedef struct IOUSBConfigurationDescHeader IOUSBConfigurationDescHeader;
```

## Discussion

The header of a [`IOUSBConfigurationDescriptor`](../iokit/iousbconfigurationdescriptor.md) that returns the total length of the descriptor.

## Topics

### Getting the Properties
- [bLength](./iousbconfigurationdescheader/api-1546382-blength.md)
  The size of the descriptor.
- [bDescriptorType](./iousbconfigurationdescheader/api-1546140-bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](./iousbconfigurationdescheader/api-1546394-wtotallength.md)
  The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.

## See Also

### Configuration Descriptors
- [IOUSBConfigurationDescriptor](./iousbconfigurationdescriptor.md)
  The structure for storing a USB configuration descriptor.
- [IOUSBConfigurationDescriptorPtr](./iousbconfigurationdescriptorptr.md)
  A pointer to a configuration descriptor.
- [IOUSBConfigurationDescHeaderPtr](./iousbconfigurationdescheaderptr.md)
  A pointer to a configuration descriptor header.
### Related Documentation
- [IOUSBConfigurationDescHeader](../iokit/usb_h_user-space/iousbconfigurationdescheader.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbconfigurationdescheader)*