# IOUSBGetSuperSpeedDeviceCapabilityDescriptor

**Framework**: USBDriverKit  
**Kind**: func

Finds the first SuperSpeed device capability descriptor in a BOS descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBDeviceCapabilitySuperSpeedUSB * IOUSBGetSuperSpeedDeviceCapabilityDescriptor(const IOUSBBOSDescriptor * bosDescriptor);
```

#### Return Value

The descriptor pointer, or `NULL` if no matching descriptor can be found.

#### Discussion

This method uses `getNextCapabilityDescriptorWithType` to fetch the first device capability descriptor.

## Parameters

- `bosDescriptor`: The BOS descriptor that contains the descriptors to iterate through.

## See Also

- [IOUSBGetNextCapabilityDescriptor](iousbgetnextcapabilitydescriptor.md)
  Gets the next device capability descriptor in a BOS descriptor.
- [IOUSBGetNextCapabilityDescriptorWithType](iousbgetnextcapabilitydescriptorwithtype.md)
  Finds the next descriptor matching a given type within a BOS descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetsuperspeeddevicecapabilitydescriptor)*