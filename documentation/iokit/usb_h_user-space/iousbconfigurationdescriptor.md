# IOUSBConfigurationDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBConfigurationDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt16 wTotalLength;
   UInt8 bNumInterfaces;
   UInt8 bConfigurationValue;
   UInt8 iConfiguration;
   UInt8 bmAttributes;
   UInt8 MaxPower;
};
```

## Overview

Standard USB Configuration Descriptor. It is variable length, so this only specifies the known fields. We use the wTotalLength field to read the whole descriptor. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBConfigurationDescriptor](../../kernel/iousbconfigurationdescriptor.md)
  The structure for storing a USB configuration descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbconfigurationdescriptor)*