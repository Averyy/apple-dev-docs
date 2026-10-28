# IOUSBDeviceQualifierDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBDeviceQualifierDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt16 bcdUSB;
   UInt8 bDeviceClass;
   UInt8 bDeviceSubClass;
   UInt8 bDeviceProtocol;
   UInt8 bMaxPacketSize0;
   UInt8 bNumConfigurations;
   UInt8 bReserved;
};
```

## Overview

USB Device Qualifier Descriptor. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBDeviceQualifierDescriptor](../../kernel/iousbdevicequalifierdescriptor.md)
  The structure for describing a high-speed capable USB device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbdevicequalifierdescriptor)*