# IOUSBHIDReportDesc

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that defines the USB HID report descriptor header.

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBHIDReportDesc IOUSBHIDReportDesc;
```

## Discussion

See the USB Implementers Forum (USB-IF) *Device Class Definition for Human Interface Devices (HID)* for more information.

## Topics

### Getting the Properties
- [hidDescriptorType](./iousbhidreportdesc/api-1546546-hiddescriptortype.md)
  The type of the descriptor.
- [hidDescriptorLengthHi](./iousbhidreportdesc/api-1546199-hiddescriptorlengthhi.md)
  The high byte length of the descriptor.
- [hidDescriptorLengthLo](./iousbhidreportdesc/api-1546355-hiddescriptorlengthlo.md)
  The low byte length of the descriptor.

## See Also

### HID Descriptors
- [IOUSBHIDData](./iousbhiddata.md)
  Data related to the mouse and keyboard.
- [IOUSBHIDDataPtr](./iousbhiddataptr.md)
  A pointer to a structure related to mouse and keyboard data.
- [IOUSBHIDDescriptor](./iousbhiddescriptor.md)
  A structure that defines the USB HID descriptor.
- [IOUSBHIDDescriptorPtr](./iousbhiddescriptorptr.md)
  A pointer to a structure that defines the USB HID descriptor.
- [IOUSBHIDReportDescPtr](./iousbhidreportdescptr.md)
  A pointer to a structure that defines the USB HID report descriptor header.
### Related Documentation
- [IOUSBHIDReportDesc](../iokit/usb_h_user-space/iousbhidreportdesc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhidreportdesc)*