# IOUSBGetNextDescriptorWithType

**Framework**: USBDriverKit  
**Kind**: func

Finds the next descriptor matching a given type within a configuration descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBDescriptorHeader * IOUSBGetNextDescriptorWithType(const IOUSBConfigurationDescriptor * configurationDescriptor, const IOUSBDescriptorHeader * currentDescriptor, const uint8_t type);
```

#### Return Value

A descriptor pointer, or `NULL` if no matching descriptor can be found.

#### Discussion

This method uses `getNextDescriptor`, and further validates that the returned descriptor’s bDescriptorType field matches the type parameter.

## Parameters

- `configurationDescriptor`: The configuration descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of the configuration descriptor, or  .
- `type`: The type of descriptor to find.

## See Also

- [IOUSBGetNextDescriptor](iousbgetnextdescriptor.md)
  Gets the next descriptor in a configuration descriptor.
- [IOUSBGetNextAssociatedDescriptor](iousbgetnextassociateddescriptor.md)
  Gets the next descriptor in the specified configuration descriptor that belongs to another container descriptor.
- [IOUSBGetNextAssociatedDescriptorWithType](iousbgetnextassociateddescriptorwithtype.md)
  Finds the next descriptor matching a specific type within a configuration descriptor that belongs to another container descriptor.
- [IOUSBGetConfigurationMaxPowerMilliAmps](iousbgetconfigurationmaxpowermilliamps.md)
  Extracts the maximum bus current a configuration descriptor requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetnextdescriptorwithtype)*