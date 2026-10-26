# IOUSBHIDDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBHIDDescriptor {
   UInt8 descLen;
   UInt8 descType;
   UInt16 descVersNum;
   UInt8 hidCountryCode;
   UInt8 hidNumDescriptors;
   UInt8 hidDescriptorType;
   UInt8 hidDescriptorLengthLo;
   UInt8 hidDescriptorLengthHi;
};
```

#### Overview

USB HID Descriptor. See the USB HID Specification at [http://www.usb.org](http://www.usb.org). (This structure should have used the #pragma pack(1) compiler directive to get byte alignment.

## See Also

### Related Documentation
- [IOUSBHIDDescriptor](../../kernel/iousbhiddescriptor.md)
  A structure that defines the USB HID descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbhiddescriptor)*