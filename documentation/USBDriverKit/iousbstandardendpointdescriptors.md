# IOUSBStandardEndpointDescriptors

**Framework**: USBDriverKit  
**Kind**: struct

Encapsulates the descriptors for a single endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBStandardEndpointDescriptors;
```

#### Discussion

Use this structure to intialize and adjust pipes in the system. You must initialize the bcdUSB member to the USB revision supported by the device. Acceptable values are `0x0110`, `0x0200`, `0x0300`, `0x0310`.

Initialize the descriptor field with a pointer to a valid endpoint descriptor. The [`ssCompanionDescriptor`](iousbstandardendpointdescriptors/sscompaniondescriptor.md) and [`sspCompanionDescriptor`](iousbstandardendpointdescriptors/sspcompaniondescriptor.md) fields may be required for USB versions `0x0300` and greater, depending on device operating speed and values set in the descriptors.

For more information on when you must use these descriptors, see section 9.5 of the USB 3.1 specification.

## Topics

### Getting the Descriptors
- [bcdUSB](iousbstandardendpointdescriptors/bcdusb.md)
  The USB version supported by the device, specified as a binary-coded decimal value.
- [descriptor](iousbstandardendpointdescriptors/descriptor.md)
  A valid endpoint descriptor.
- [ssCompanionDescriptor](iousbstandardendpointdescriptors/sscompaniondescriptor.md)
  The companion descriptor for super-speed devices.
- [sspCompanionDescriptor](iousbstandardendpointdescriptors/sspcompaniondescriptor.md)
  The companion descriptor for super-speed plus devices.

## See Also

- [GetDescriptors](iousbhostpipe/getdescriptors.md)
  Retrieves the endpoint descriptors associated with this pipe.
- [IOUSBGetEndpointDescriptorOptions](iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbstandardendpointdescriptors)*