# IOUSBConfigurationDescHeader

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBConfigurationDescHeader {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt16 wTotalLength;
};
```

## Overview

Header of a IOUSBConfigurationDescriptor. Used to get the total length of the descriptor.

## See Also

### Related Documentation
- [IOUSBConfigurationDescHeader](../../kernel/iousbconfigurationdescheader.md)
  The header of a configuration descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbconfigurationdescheader)*