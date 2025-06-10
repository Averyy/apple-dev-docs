# IOUSBHIDDescriptor

**Framework**: Kernel  
**Kind**: tdef

A structure that defines the USB HID descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOUSBHIDDescriptor IOUSBHIDDescriptor;
```

#### Discussion

See the USB Implementers Forum (USB-IF)  for more information.

## Topics

### Getting the Properties
- [descLen](iousbhiddescriptor/1546208-desclen.md)
  The size of the descriptor.
- [descType](iousbhiddescriptor/1546221-desctype.md)
  The type of the descriptor.
- [descVersNum](iousbhiddescriptor/1545993-descversnum.md)
  The verison number of the descriptor.
- [hidCountryCode](iousbhiddescriptor/1546545-hidcountrycode.md)
  The country or region code of the localized hardware.
- [hidDescriptorLengthHi](iousbhiddescriptor/1546246-hiddescriptorlengthhi.md)
  The high byte length of the descriptor.
- [hidDescriptorLengthLo](iousbhiddescriptor/1546304-hiddescriptorlengthlo.md)
  The low byte length of the descriptor.
- [hidDescriptorType](iousbhiddescriptor/1545961-hiddescriptortype.md)
  The class type of the descriptor.
- [hidNumDescriptors](iousbhiddescriptor/1546017-hidnumdescriptors.md)
  The number of class descriptors.

## See Also

- [IOUSBHIDData](iousbhiddata.md)
  Data related to the mouse and keyboard.
- [IOUSBHIDDataPtr](iousbhiddataptr.md)
  A pointer to a structure related to mouse and keyboard data.
- [IOUSBHIDDescriptorPtr](iousbhiddescriptorptr.md)
  A pointer to a structure that defines the USB HID descriptor.
- [IOUSBHIDReportDesc](iousbhidreportdesc.md)
  A structure that defines the USB HID report descriptor header.
- [IOUSBHIDReportDescPtr](iousbhidreportdescptr.md)
  A pointer to a structure that defines the USB HID report descriptor header.
- [IOUSBHIDDescriptor](../iokit/usb_h_user-space/iousbhiddescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhiddescriptor)*