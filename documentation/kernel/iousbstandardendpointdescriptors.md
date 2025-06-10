# IOUSBStandardEndpointDescriptors

**Framework**: Kernel  
**Kind**: tag

A container for descriptors for a single endpoint.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct IOUSBStandardEndpointDescriptors {
    ...
};
```

#### Discussion

Use this structure to intialize and adjust pipes in the system. You must initialize the `bcdUSB` descriptor to the USB version that the device supports. Acceptable values are `0x0110`, `0x0200`, `0x0300`, `0x0310`. 

Initialize the descriptor field with a pointer to a valid endpoint descriptor. USB versions `0x0300` and greater may require the [`ssCompanionDescriptor`](https://developer.apple.com/documentation/usbdriverkit/iousbstandardendpointdescriptors/sscompaniondescriptor) and [`sspCompanionDescriptor`](https://developer.apple.com/documentation/usbdriverkit/iousbstandardendpointdescriptors/sspcompaniondescriptor) fields, depending on device operating speed and values set in the descriptors. 

For more information on when you must use these descriptors, see USB 3.2, 9.5.

## Topics

### Getting the Properties
- [bcdUSB](iousbstandardendpointdescriptors/3294859-bcdusb.md)
  A binary-coded decimal value that indicates the USB version that the device supports.
- [descriptor](iousbstandardendpointdescriptors/3294860-descriptor.md)
  A valid endpoint descriptor.
- [ssCompanionDescriptor](iousbstandardendpointdescriptors/3294861-sscompaniondescriptor.md)
  The companion descriptor for SuperSpeed devices.
- [sspCompanionDescriptor](iousbstandardendpointdescriptors/3294862-sspcompaniondescriptor.md)
  The companion descriptor for SuperSpeedPlus devices.

## See Also

- [IOUSBEndpointDescriptor](iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.
- [IOUSBEndpointDescriptorPtr](iousbendpointdescriptorptr.md)
  A pointer to the endpoint descriptor.
- [IOUSBEndpointProperties](iousbendpointproperties.md)
  A structure that holds USB endpoint properties.
- [IOUSBEndpointPropertiesPtr](iousbendpointpropertiesptr.md)
  A pointer to an endpoint properties object.
- [IOUSBGetEndpointDescriptorOptions](iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbstandardendpointdescriptors)*