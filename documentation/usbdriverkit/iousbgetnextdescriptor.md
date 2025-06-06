# IOUSBGetNextDescriptor

**Framework**: USBDriverKit  
**Kind**: func

Gets the next descriptor in a configuration descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBDescriptorHeader * IOUSBGetNextDescriptor(const IOUSBConfigurationDescriptor * configurationDescriptor, const IOUSBDescriptorHeader * currentDescriptor);
```

#### Return Value

The descriptor pointer, or `NULL` if no descriptor can be returned.

#### Discussion

This method advances the current descriptor by its length, and validates that the new descriptor fits within the bounds of the configuration descriptor. Passing `NULL` for the `currentDescriptor` argument returns the first descriptor after the configuration descriptor.

## Parameters

- `configurationDescriptor`: The configuration descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of  , or  .

## See Also

- [IOUSBGetNextDescriptorWithType](iousbgetnextdescriptorwithtype.md)
  Finds the next descriptor matching a given type within a configuration descriptor.
- [IOUSBGetNextAssociatedDescriptor](iousbgetnextassociateddescriptor.md)
  Gets the next descriptor in the specified configuration descriptor that belongs to another container descriptor.
- [IOUSBGetNextAssociatedDescriptorWithType](iousbgetnextassociateddescriptorwithtype.md)
  Finds the next descriptor matching a specific type within a configuration descriptor that belongs to another container descriptor.
- [IOUSBGetConfigurationMaxPowerMilliAmps](iousbgetconfigurationmaxpowermilliamps.md)
  Extracts the maximum bus current a configuration descriptor requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetnextdescriptor)*