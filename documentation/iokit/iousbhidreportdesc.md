# IOUSBHIDReportDesc

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBHIDReportDesc {
    ...
} IOUSBHIDReportDesc;
```

## Overview

USB HID Report Descriptor header. See the USB HID Specification at [http://www.usb.org](http://www.usb.org). (This structure should have used the #pragma pack(1) compiler directive to get byte alignment.

## Topics

### Instance Properties
- [hidDescriptorLengthHi](./iousbhidreportdesc/api-1426294-hiddescriptorlengthhi.md)
- [hidDescriptorLengthLo](./iousbhidreportdesc/api-1425781-hiddescriptorlengthlo.md)
- [hidDescriptorType](./iousbhidreportdesc/api-1425638-hiddescriptortype.md)

## See Also

### Related Documentation
- [IOUSBHIDReportDesc](./usb_h_user-space/iousbhidreportdesc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbhidreportdesc)*