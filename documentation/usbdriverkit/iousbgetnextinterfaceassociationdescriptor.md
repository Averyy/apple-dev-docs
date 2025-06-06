# IOUSBGetNextInterfaceAssociationDescriptor

**Framework**: USBDriverKit  
**Kind**: func

Finds the next interface association descriptor in a configuration descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBInterfaceAssociationDescriptor * IOUSBGetNextInterfaceAssociationDescriptor(const IOUSBConfigurationDescriptor * configurationDescriptor, const IOUSBDescriptorHeader * currentDescriptor);
```

#### Return Value

An interface association descriptor pointer, or `NULL` if no matching descriptor can be found.

#### Discussion

This method uses `getNextDescriptorWithType` to fetch the next interface association descriptor.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of the configuration descriptor, or  .

## See Also

- [IOUSBGetNextInterfaceDescriptor](iousbgetnextinterfacedescriptor.md)
  Finds the next interface descriptor in a configuration descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetnextinterfaceassociationdescriptor)*