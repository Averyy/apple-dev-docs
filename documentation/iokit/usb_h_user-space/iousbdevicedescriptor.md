# IOUSBDeviceDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBDeviceDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt16 bcdUSB;
   UInt8 bDeviceClass;
   UInt8 bDeviceSubClass;
   UInt8 bDeviceProtocol;
   UInt8 bMaxPacketSize0;
   UInt16 idVendor;
   UInt16 idProduct;
   UInt16 bcdDevice;
   UInt8 iManufacturer;
   UInt8 iProduct;
   UInt8 iSerialNumber;
   UInt8 bNumConfigurations;
};
```

#### Overview

Descriptor for a USB Device. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBDeviceDescriptor](../../kernel/iousbdevicedescriptor.md)
  The structure for storing a USB device descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbdevicedescriptor)*