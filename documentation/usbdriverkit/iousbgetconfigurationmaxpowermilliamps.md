# IOUSBGetConfigurationMaxPowerMilliAmps

**Framework**: USBDriverKit  
**Kind**: func

Extracts the maximum bus current a configuration descriptor requires.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint32_t IOUSBGetConfigurationMaxPowerMilliAmps(uint32_t usbDeviceSpeed, const IOUSBConfigurationDescriptor * descriptor);
```

#### Return Value

The milliamps required.

#### Discussion

This method parses a configuration descriptor and returns the number of milliamps required to power the device.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The configuration descriptor to parse.

## See Also

- [IOUSBGetNextDescriptor](iousbgetnextdescriptor.md)
  Gets the next descriptor in a configuration descriptor.
- [IOUSBGetNextDescriptorWithType](iousbgetnextdescriptorwithtype.md)
  Finds the next descriptor matching a given type within a configuration descriptor.
- [IOUSBGetNextAssociatedDescriptor](iousbgetnextassociateddescriptor.md)
  Gets the next descriptor in the specified configuration descriptor that belongs to another container descriptor.
- [IOUSBGetNextAssociatedDescriptorWithType](iousbgetnextassociateddescriptorwithtype.md)
  Finds the next descriptor matching a specific type within a configuration descriptor that belongs to another container descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetconfigurationmaxpowermilliamps)*