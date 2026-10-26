# IOUSBSuperSpeedEndpointCompanionDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBSuperSpeedEndpointCompanionDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bMaxBurst;
   UInt8 bmAttributes;
   UInt16 wBytesPerInterval;
};
```

#### Overview

Descriptor for a SuperSpeed USB Endpoint Companion. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBSuperSpeedEndpointCompanionDescriptor](../../kernel/iousbsuperspeedendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbsuperspeedendpointcompaniondescriptor)*