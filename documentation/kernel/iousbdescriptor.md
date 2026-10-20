# IOUSBDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

The base descriptor type.

**Availability**:
- macOS 10.15+

## Declaration

```c
typedef IOUSBDescriptorHeader IOUSBDescriptor;
```

#### Discussion

Use this type to represent generic descriptor definitions. For more information about descriptors, see USB 3.2, 9.5.

## See Also

### Descriptor Fundamentals
- [IOUSBDescriptorHeader](./iousbdescriptorheader.md)
  The base descriptor header.
- [tIOUSBDescriptorType](./tiousbdescriptortype.md)
  Constants describing the types of descriptors available for a USB device.
- [tIOUSBDescriptorSize](./tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [IOUSBDescriptorHeaderPtr](./iousbdescriptorheaderptr.md)
  A pointer to a USB descriptor header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdescriptor)*