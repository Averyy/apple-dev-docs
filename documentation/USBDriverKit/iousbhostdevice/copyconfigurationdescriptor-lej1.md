# CopyConfigurationDescriptor

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the configuration descriptor with the specified index.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual const IOUSBConfigurationDescriptor * CopyConfigurationDescriptor(uint8_t index);
```

#### Return Value

A pointer to the configuration descriptor, or `NULL` if the descriptor wasn’t found. It’s your responsibility to free the returned descriptor.

#### Discussion

This method searches the descriptor cache for the specified descriptor. If the descriptor isn’t in the cache, the method retrieves it from the device using a `GET_DESCRIPTOR` control request (USB 2.0, section 9.4.3) and adds it to the cache. When making a `GET_DESCRIPTOR` control request, this method acquires the service’s workloop lock and may call [`commandSleep`](../../kernel/iocommandgate/api-1573818-commandsleep.md).

## Parameters

- `index`: The index number of the configuration.

## See Also

### Getting the Device Descriptors
- [CopyCapabilityDescriptors](./copycapabilitydescriptors.md)
  Returns the device’s capability descriptors.
- [CopyConfigurationDescriptor](./copyconfigurationdescriptor-6qgew.md)
  Returns the currently selected configuration descriptor.
- [CopyConfigurationDescriptorWithValue](./copyconfigurationdescriptorwithvalue.md)
  Returns the configuration descriptor with the specified configuration value.
- [CopyDeviceDescriptor](./copydevicedescriptor.md)
  Returns the device descriptor.
- [CopyStringDescriptor](./copystringdescriptor-28ybo.md)
  Returns a string descriptor from the device.
- [CopyStringDescriptor](./copystringdescriptor-9h8l2.md)
  Returns a string descriptor from the device.
- [CopyDescriptor](./copydescriptor.md)
  Retrieves any type of descriptor from the cache or the device.
- [tIOUSBDeviceRequestTypeValue](../tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [tIOUSBDeviceRequestRecipientValue](../tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.
- [Descriptor Utilities](../descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/copyconfigurationdescriptor-lej1)*