# IOUSBDescriptorHeader

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBDescriptorHeader {
   UInt8 bLength;
   UInt8 bDescriptorType;
};
```

## Overview

Standard header used for all USB descriptors. Used to read the length of a descriptor so that we can allocate storage for the whole descriptor later on.

## See Also

### Related Documentation
- [IOUSBDescriptorHeader](../../kernel/iousbdescriptorheader.md)
  The base descriptor header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbdescriptorheader)*