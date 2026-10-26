# IOUSBDescriptorHeader

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBDescriptorHeader {
    ...
} IOUSBDescriptorHeader;
```

#### Overview

Standard header used for all USB descriptors. Used to read the length of a descriptor so that we can allocate storage for the whole descriptor later on.

## Topics

### Instance Properties
- [bDescriptorType](./iousbdescriptorheader/api-1425797-bdescriptortype.md)
- [bLength](./iousbdescriptorheader/api-1425367-blength.md)

## See Also

### Related Documentation
- [IOUSBDescriptorHeader](./usb_h_user-space/iousbdescriptorheader.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdescriptorheader)*