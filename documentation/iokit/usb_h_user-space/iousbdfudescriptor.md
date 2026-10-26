# IOUSBDFUDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBDFUDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bmAttributes;
   UInt16 wDetachTimeout;
   UInt16 wTransferSize;
};
```

#### Overview

USB Device Firmware Update Descriptor. See the USB Device Firmware Update Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBDFUDescriptor](../../kernel/iousbdfudescriptor.md)
  A structure that defines the USB device firmware update descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbdfudescriptor)*