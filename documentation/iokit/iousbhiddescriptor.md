# IOUSBHIDDescriptor

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBHIDDescriptor {
    ...
} IOUSBHIDDescriptor;
```

## Overview

USB HID Descriptor. See the USB HID Specification at [http://www.usb.org](http://www.usb.org). (This structure should have used the #pragma pack(1) compiler directive to get byte alignment.

## Topics

### Instance Properties
- [descLen](./iousbhiddescriptor/api-1426203-desclen.md)
- [descType](./iousbhiddescriptor/api-1426322-desctype.md)
- [descVersNum](./iousbhiddescriptor/api-1425858-descversnum.md)
- [hidCountryCode](./iousbhiddescriptor/api-1425535-hidcountrycode.md)
- [hidDescriptorLengthHi](./iousbhiddescriptor/api-1426191-hiddescriptorlengthhi.md)
- [hidDescriptorLengthLo](./iousbhiddescriptor/api-1425379-hiddescriptorlengthlo.md)
- [hidDescriptorType](./iousbhiddescriptor/api-1426111-hiddescriptortype.md)
- [hidNumDescriptors](./iousbhiddescriptor/api-1425584-hidnumdescriptors.md)

## See Also

### Related Documentation
- [IOUSBHIDDescriptor](./usb_h_user-space/iousbhiddescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbhiddescriptor)*