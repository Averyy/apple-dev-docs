# IOUSBEndpointDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBEndpointDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bEndpointAddress;
   UInt8 bmAttributes;
   UInt16 wMaxPacketSize;
   UInt8 bInterval;
};
```

#### Overview

Descriptor for a USB Endpoint. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBEndpointDescriptor](../../kernel/iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbendpointdescriptor)*