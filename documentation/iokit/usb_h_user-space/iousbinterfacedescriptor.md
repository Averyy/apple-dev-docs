# IOUSBInterfaceDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBInterfaceDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bInterfaceNumber;
   UInt8 bAlternateSetting;
   UInt8 bNumEndpoints;
   UInt8 bInterfaceClass;
   UInt8 bInterfaceSubClass;
   UInt8 bInterfaceProtocol;
   UInt8 iInterface;
};
```

#### Overview

Descriptor for a USB Interface. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBInterfaceDescriptor](../../kernel/iousbinterfacedescriptor.md)
  A descriptor for a specific interface of a USB device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbinterfacedescriptor)*