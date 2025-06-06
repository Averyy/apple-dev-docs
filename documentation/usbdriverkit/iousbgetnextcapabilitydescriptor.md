# IOUSBGetNextCapabilityDescriptor

**Framework**: USBDriverKit  
**Kind**: func

Gets the next device capability descriptor in a BOS descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBDeviceCapabilityDescriptorHeader * IOUSBGetNextCapabilityDescriptor(const IOUSBBOSDescriptor * bosDescriptor, const IOUSBDeviceCapabilityDescriptorHeader * currentDescriptor);
```

#### Return Value

The device capability descriptor pointer, or `NULL` if no descriptor is available.

#### Discussion

This method advances the current descriptor by its length, and validates that the new descriptor fits within the bounds of the BOS descriptor. Passing `NULL` for `currentDescriptor` returns the first descriptor after the BOS descriptor.

## Parameters

- `bosDescriptor`: The BOS descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of the BOS descriptor, or  .

## See Also

- [IOUSBGetNextCapabilityDescriptorWithType](iousbgetnextcapabilitydescriptorwithtype.md)
  Finds the next descriptor matching a given type within a BOS descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetnextcapabilitydescriptor)*