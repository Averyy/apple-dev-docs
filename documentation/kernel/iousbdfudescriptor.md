# IOUSBDFUDescriptor

**Framework**: Kernel  
**Kind**: tdef

A structure that defines the USB device firmware update descriptor.

**Availability**:
- macOS 10.2+

## Declaration

```swift
typedef struct IOUSBDFUDescriptor IOUSBDFUDescriptor;
```

#### Discussion

See the USB Implementers Forum (USB-IF)  for more information.

## Topics

### Getting the Properties
- [bLength](iousbdfudescriptor/1546015-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbdfudescriptor/1546426-bdescriptortype.md)
  The type of the descriptor.
- [bmAttributes](iousbdfudescriptor/1546360-bmattributes.md)
  A bitmap encoding of supported device-level features.
- [wDetachTimeout](iousbdfudescriptor/1546084-wdetachtimeout.md)
  The time in milliseconds that the device waits after receipt of a detach request.
- [wTransferSize](iousbdfudescriptor/1546379-wtransfersize.md)
  The maximum number of bytes that the device can accept per control-write transaction.

## See Also

- [IOUSBDFUDescriptorPtr](iousbdfudescriptorptr.md)
  A pointer to a structure that defines the USB device firmware update descriptor.
- [IOUSBDFUDescriptor](../iokit/usb_h_user-space/iousbdfudescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdfudescriptor)*