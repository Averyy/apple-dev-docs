# CopyConfigurationDescriptor

**Framework**: USBDriverKit  
**Kind**: method

Retrieves the parent configuration descriptor for this interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBConfigurationDescriptor * CopyConfigurationDescriptor();
```

#### Return Value

The configuration descriptor for this interface. It’s your responsibility to free the returned descriptor.

## See Also

- [GetInterfaceDescriptor](iousbhostinterface/getinterfacedescriptor.md)
  Returns the version of the interface descriptor that is associated with the specified configuration.
- [CopyStringDescriptor](iousbhostinterface/copystringdescriptor-83du1.md)
  Returns a descriptor from the device in the specified language.
- [CopyStringDescriptor](iousbhostinterface/copystringdescriptor-8k65j.md)
  Returns a string descriptor from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/copyconfigurationdescriptor)*