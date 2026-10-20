# IOUSBBOSDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

The structure for storing a binary object store (BOS) descriptor.

**Availability**:
- macOS 10.7+

## Declaration

```c
typedef struct IOUSBBOSDescriptor IOUSBBOSDescriptor;
```

#### Discussion

For more information about this descriptor type, see USB 3.2, 9.6.2.

## Topics

### Getting the Properties
- [bLength](./iousbbosdescriptor/api-1545985-blength.md)
  The size of the descriptor.
- [bDescriptorType](./iousbbosdescriptor/api-1546245-bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](./iousbbosdescriptor/api-1546141-wtotallength.md)
  The length of this descriptor and all of its subdescriptors.
- [bNumDeviceCaps](./iousbbosdescriptor/api-1546040-bnumdevicecaps.md)
  The number of separate device capability descriptors in the binary object store.

## See Also

### BOS Descriptors
- [IOUSBBOSDescriptorPtr](./iousbbosdescriptorptr.md)
  A pointer to a structure for storing a binary object store (BOS) descriptor.
### Related Documentation
- [IOUSBBOSDescriptor](../iokit/usb_h_user-space/iousbbosdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbbosdescriptor)*