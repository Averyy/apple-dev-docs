# IOUSBGetNextCapabilityDescriptorWithType

**Framework**: USBDriverKit  
**Kind**: func

Finds the next descriptor matching a given type within a BOS descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBDeviceCapabilityDescriptorHeader * IOUSBGetNextCapabilityDescriptorWithType(const IOUSBBOSDescriptor * bosDescriptor, const IOUSBDeviceCapabilityDescriptorHeader * currentDescriptor, const uint8_t type);
```

#### Return Value

A descriptor pointer, or `NULL` if no matching descriptor is available.

#### Discussion

This method uses `getNextCapabilityDescriptor`, and further validates that the returned descriptor’s `bDevCapabilityType` field matches the type parameter.

## Parameters

- `bosDescriptor`: The BOS descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of the BOS descriptor, or  .
- `type`: The descriptor type to find.

## See Also

- [IOUSBGetNextCapabilityDescriptor](iousbgetnextcapabilitydescriptor.md)
  Gets the next device capability descriptor in a BOS descriptor.
- [IOUSBGetSuperSpeedDeviceCapabilityDescriptor](iousbgetsuperspeeddevicecapabilitydescriptor.md)
  Finds the first SuperSpeed device capability descriptor in a BOS descriptor.
- [IOUSBGetSuperSpeedPlusDeviceCapabilityDescriptor](iousbgetsuperspeedplusdevicecapabilitydescriptor.md)
  Finds the first SuperSpeed Plus device capability descriptor in a BOS descriptor.
- [IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor](iousbgetusb20extensiondevicecapabilitydescriptor.md)
  Finds the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [IOUSBGetContainerIDDescriptor](iousbgetcontaineriddescriptor.md)
  Finds the first Container ID capability descriptor in a BOS descriptor.
- [IOUSBGetPlatformCapabilityDescriptor](iousbgetplatformcapabilitydescriptor.md)
  Finds the first platform capability descriptor in a BOS descriptor.
- [IOUSBGetBillboardDescriptor](iousbgetbillboarddescriptor.md)
  Finds the first billboard capability descriptor in a BOS descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetnextcapabilitydescriptorwithtype)*