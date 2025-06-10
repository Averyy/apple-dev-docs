# IOUSBSuperSpeedEndpointCompanionDescriptor

**Framework**: Kernel  
**Kind**: tdef

The descriptor for a SuperSpeed USB endpoint companion.

**Availability**:
- macOS 10.7+

## Declaration

```swift
typedef struct IOUSBSuperSpeedEndpointCompanionDescriptor IOUSBSuperSpeedEndpointCompanionDescriptor;
```

#### Discussion

For more information about this descriptor type, see USB 3.2, 9.6.7.

## Topics

### Getting the Properties
- [bLength](iousbsuperspeedendpointcompaniondescriptor/1546150-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbsuperspeedendpointcompaniondescriptor/1546448-bdescriptortype.md)
  The type of the descriptor.
- [bMaxBurst](iousbsuperspeedendpointcompaniondescriptor/1545987-bmaxburst.md)
  The maximum number of packets the endpoint can send or receive as part of a burst.
- [bmAttributes](iousbsuperspeedendpointcompaniondescriptor/1545944-bmattributes.md)
  A bitmap encoding of supported device-level features.
- [wBytesPerInterval](iousbsuperspeedendpointcompaniondescriptor/1546415-wbytesperinterval.md)
  The total number of bytes this endpoint transfers every service interval.

## See Also

- [IOUSBStringDescriptor](iousbstringdescriptor.md)
  The structure for storing a string descriptor.
- [IOUSBStringDescriptorPtr](iousbstringdescriptorptr.md)
  A pointer to a string descriptor structure.
- [IOUSBSuperSpeedEndpointCompanionDescriptorPtr](iousbsuperspeedendpointcompaniondescriptorptr.md)
  A pointer to a SuperSpeed USB endpoint companion descriptor.
- [IOUSBSuperSpeedHubDescriptor](iousbsuperspeedhubdescriptor.md)
  A structure that defines the descriptor for a SuperSpeed USB hub.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbsuperspeedplusisochronousendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptorPtr](iousbsuperspeedplusisochronousendpointcompaniondescriptorptr.md)
  A pointer to a SuperSpeedPlus isochronous USB endpoint companion descriptor.
- [IOUSBSuperSpeedEndpointCompanionDescriptor](../iokit/usb_h_user-space/iousbsuperspeedendpointcompaniondescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbsuperspeedendpointcompaniondescriptor)*