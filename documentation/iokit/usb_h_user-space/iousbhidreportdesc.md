# IOUSBHIDReportDesc

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBHIDReportDesc {
   UInt8 hidDescriptorType;
   UInt8 hidDescriptorLengthLo;
   UInt8 hidDescriptorLengthHi;
};
```

#### Overview

USB HID Report Descriptor header. See the USB HID Specification at [http://www.usb.org](http://www.usb.org). (This structure should have used the #pragma pack(1) compiler directive to get byte alignment.

## See Also

### Related Documentation
- [IOUSBHIDReportDesc](../../kernel/iousbhidreportdesc.md)
  A structure that defines the USB HID report descriptor header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbhidreportdesc)*