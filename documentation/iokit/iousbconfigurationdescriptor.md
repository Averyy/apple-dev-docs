# IOUSBConfigurationDescriptor

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBConfigurationDescriptor {
    ...
} IOUSBConfigurationDescriptor;
```

#### Overview

Standard USB Configuration Descriptor. It is variable length, so this only specifies the known fields. We use the wTotalLength field to read the whole descriptor. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## Topics

### Instance Properties
- [MaxPower](./iousbconfigurationdescriptor/api-1425565-maxpower.md)
- [bConfigurationValue](./iousbconfigurationdescriptor/api-1426254-bconfigurationvalue.md)
- [bDescriptorType](./iousbconfigurationdescriptor/api-1426163-bdescriptortype.md)
- [bLength](./iousbconfigurationdescriptor/api-1425946-blength.md)
- [bNumInterfaces](./iousbconfigurationdescriptor/api-1425737-bnuminterfaces.md)
- [bmAttributes](./iousbconfigurationdescriptor/api-1425885-bmattributes.md)
- [iConfiguration](./iousbconfigurationdescriptor/api-1425879-iconfiguration.md)
- [wTotalLength](./iousbconfigurationdescriptor/api-1425444-wtotallength.md)

## See Also

### Related Documentation
- [IOUSBConfigurationDescriptor](./usb_h_user-space/iousbconfigurationdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbconfigurationdescriptor)*