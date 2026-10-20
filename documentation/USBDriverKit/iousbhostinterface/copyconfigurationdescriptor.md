# CopyConfigurationDescriptor

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the parent configuration descriptor for this interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual const IOUSBConfigurationDescriptor * CopyConfigurationDescriptor();
```

#### Return Value

The configuration descriptor for this interface. It’s your responsibility to free the returned descriptor.

## See Also

### Getting Interface-Related Descriptors
- [GetInterfaceDescriptor](./getinterfacedescriptor.md)
  Returns the version of the interface descriptor that is associated with the specified configuration.
- [CopyStringDescriptor](./copystringdescriptor-83du1.md)
  Returns a descriptor from the device in the specified language.
- [CopyStringDescriptor](./copystringdescriptor-8k65j.md)
  Returns a string descriptor from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/copyconfigurationdescriptor)*