# IOUSBBOSDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBBOSDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt16 wTotalLength;
   UInt8 bNumDeviceCaps;
};
```

## Overview

BOS Descriptor for a USB Device. .

## See Also

### Related Documentation
- [IOUSBBOSDescriptor](../../kernel/iousbbosdescriptor.md)
  The structure for storing a binary object store (BOS) descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbbosdescriptor)*