# GetInterfaceDescriptor

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the version of the interface descriptor that is associated with the specified configuration.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual const IOUSBInterfaceDescriptor * GetInterfaceDescriptor(const IOUSBConfigurationDescriptor *configurationDescriptor);
```

## Return Value

The interface descriptor structure.

## Parameters

- `configurationDescriptor`: The configuration descriptor that owns the interface.

## See Also

### Getting Interface-Related Descriptors
- [CopyConfigurationDescriptor](./copyconfigurationdescriptor.md)
  Retrieves the parent configuration descriptor for this interface.
- [CopyStringDescriptor](./copystringdescriptor-83du1.md)
  Returns a descriptor from the device in the specified language.
- [CopyStringDescriptor](./copystringdescriptor-8k65j.md)
  Returns a string descriptor from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/getinterfacedescriptor)*