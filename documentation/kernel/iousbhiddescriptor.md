# IOUSBHIDDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that defines the USB HID descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBHIDDescriptor IOUSBHIDDescriptor;
```

## Discussion

See the USB Implementers Forum (USB-IF) *Device Class Definition for Human Interface Devices (HID)* for more information.

## Topics

### Getting the Properties
- [descLen](./iousbhiddescriptor/api-1546208-desclen.md)
  The size of the descriptor.
- [descType](./iousbhiddescriptor/api-1546221-desctype.md)
  The type of the descriptor.
- [descVersNum](./iousbhiddescriptor/api-1545993-descversnum.md)
  The verison number of the descriptor.
- [hidCountryCode](./iousbhiddescriptor/api-1546545-hidcountrycode.md)
  The country or region code of the localized hardware.
- [hidDescriptorLengthHi](./iousbhiddescriptor/api-1546246-hiddescriptorlengthhi.md)
  The high byte length of the descriptor.
- [hidDescriptorLengthLo](./iousbhiddescriptor/api-1546304-hiddescriptorlengthlo.md)
  The low byte length of the descriptor.
- [hidDescriptorType](./iousbhiddescriptor/api-1545961-hiddescriptortype.md)
  The class type of the descriptor.
- [hidNumDescriptors](./iousbhiddescriptor/api-1546017-hidnumdescriptors.md)
  The number of class descriptors.

## See Also

### HID Descriptors
- [IOUSBHIDData](./iousbhiddata.md)
  Data related to the mouse and keyboard.
- [IOUSBHIDDataPtr](./iousbhiddataptr.md)
  A pointer to a structure related to mouse and keyboard data.
- [IOUSBHIDDescriptorPtr](./iousbhiddescriptorptr.md)
  A pointer to a structure that defines the USB HID descriptor.
- [IOUSBHIDReportDesc](./iousbhidreportdesc.md)
  A structure that defines the USB HID report descriptor header.
- [IOUSBHIDReportDescPtr](./iousbhidreportdescptr.md)
  A pointer to a structure that defines the USB HID report descriptor header.
### Related Documentation
- [IOUSBHIDDescriptor](../iokit/usb_h_user-space/iousbhiddescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhiddescriptor)*