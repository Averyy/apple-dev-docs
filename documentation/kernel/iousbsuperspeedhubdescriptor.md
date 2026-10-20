# IOUSBSuperSpeedHubDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that defines the descriptor for a SuperSpeed USB hub.

**Availability**:
- macOS 10.15+

## Declaration

```c
typedef struct IOUSBSuperSpeedHubDescriptor IOUSBSuperSpeedHubDescriptor;
```

#### Discussion

For more information about this descriptor type, see USB 3.2, 10.15.2.1.

## Topics

### Instance Properties
- [bDescriptorType](./iousbsuperspeedhubdescriptor/api-3166583-bdescriptortype.md)
- [bHubControllerCurrent](./iousbsuperspeedhubdescriptor/api-3166584-bhubcontrollercurrent.md)
- [bHubDecodeLatency](./iousbsuperspeedhubdescriptor/api-3166585-bhubdecodelatency.md)
- [bLength](./iousbsuperspeedhubdescriptor/api-3166586-blength.md)
- [bNumberPorts](./iousbsuperspeedhubdescriptor/api-3166587-bnumberports.md)
- [bPowerOnToPowerGood](./iousbsuperspeedhubdescriptor/api-3166588-bpowerontopowergood.md)
- [deviceRemovable](./iousbsuperspeedhubdescriptor/api-3166589-deviceremovable.md)
- [wHubCharacteristics](./iousbsuperspeedhubdescriptor/api-3166590-whubcharacteristics.md)
- [wHubDelay](./iousbsuperspeedhubdescriptor/api-3166591-whubdelay.md)

## See Also

### USB Descriptors
- [IOUSBStringDescriptor](./iousbstringdescriptor.md)
  The structure for storing a string descriptor.
- [IOUSBStringDescriptorPtr](./iousbstringdescriptorptr.md)
  A pointer to a string descriptor structure.
- [IOUSBSuperSpeedEndpointCompanionDescriptor](./iousbsuperspeedendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [IOUSBSuperSpeedEndpointCompanionDescriptorPtr](./iousbsuperspeedendpointcompaniondescriptorptr.md)
  A pointer to a SuperSpeed USB endpoint companion descriptor.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](./iousbsuperspeedplusisochronousendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptorPtr](./iousbsuperspeedplusisochronousendpointcompaniondescriptorptr.md)
  A pointer to a SuperSpeedPlus isochronous USB endpoint companion descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbsuperspeedhubdescriptor)*