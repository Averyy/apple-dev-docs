# IOUSBDFUDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that defines the USB device firmware update descriptor.

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef struct IOUSBDFUDescriptor IOUSBDFUDescriptor;
```

#### Discussion

See the USB Implementers Forum (USB-IF) *Universal Serial Bus Power Delivery Firmware Update Specification* for more information.

## Topics

### Getting the Properties
- [bLength](./iousbdfudescriptor/api-1546015-blength.md)
  The size of the descriptor.
- [bDescriptorType](./iousbdfudescriptor/api-1546426-bdescriptortype.md)
  The type of the descriptor.
- [bmAttributes](./iousbdfudescriptor/api-1546360-bmattributes.md)
  A bitmap encoding of supported device-level features.
- [wDetachTimeout](./iousbdfudescriptor/api-1546084-wdetachtimeout.md)
  The time in milliseconds that the device waits after receipt of a detach request.
- [wTransferSize](./iousbdfudescriptor/api-1546379-wtransfersize.md)
  The maximum number of bytes that the device can accept per control-write transaction.

## See Also

### Device Firmware Update Descriptors
- [IOUSBDFUDescriptorPtr](./iousbdfudescriptorptr.md)
  A pointer to a structure that defines the USB device firmware update descriptor.
### Related Documentation
- [IOUSBDFUDescriptor](../iokit/usb_h_user-space/iousbdfudescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdfudescriptor)*