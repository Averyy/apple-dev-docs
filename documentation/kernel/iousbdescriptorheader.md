# IOUSBDescriptorHeader

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

The base descriptor header.

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBDescriptorHeader IOUSBDescriptorHeader;
```

#### Discussion

This structure is the standard header for all USB descriptors. Use it to read the length of a descriptor so that it can allocate storage for the whole descriptor.

## Topics

### Getting the Descriptor Properties
- [bLength](./iousbdescriptorheader/api-1546043-blength.md)
  The size of the descriptor.
- [bDescriptorType](./iousbdescriptorheader/api-1546469-bdescriptortype.md)
  The type of the descriptor.

## See Also

### Descriptor Fundamentals
- [IOUSBDescriptor](./iousbdescriptor.md)
  The base descriptor type.
- [tIOUSBDescriptorType](./tiousbdescriptortype.md)
  Constants describing the types of descriptors available for a USB device.
- [tIOUSBDescriptorSize](./tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [IOUSBDescriptorHeaderPtr](./iousbdescriptorheaderptr.md)
  A pointer to a USB descriptor header.
### Related Documentation
- [IOUSBDescriptorHeader](../iokit/usb_h_user-space/iousbdescriptorheader.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdescriptorheader)*