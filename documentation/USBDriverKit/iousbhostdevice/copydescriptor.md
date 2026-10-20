# CopyDescriptor

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Retrieves any type of descriptor from the cache or the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t CopyDescriptor(uint8_t type, uint16_t *length, uint8_t index, uint16_t languageID, uint8_t requestType, uint8_t requestRecipient, uint8_t *descriptor);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

This method searches the descriptor cache for the descriptor that matches the specified parameters. If the descriptor isn’t in the cache, the method retrieves it from the device using a `GET_DESCRIPTOR` control request (USB 2.0, section 9.4.3) and adds it to the cache. (The method puts the `index` value in the low byte of the `wValue` field, and puts the `languageID` value in the `wIndex` field of the request structure.) When making the `GET_DESCRIPTOR` control request, this method acquires the service’s workloop lock and may call [`commandSleep`](../../kernel/iocommandgate/api-1573818-commandsleep.md).

## Parameters

- `type`: The descriptor type to find. For a list of possible types, see [`tIOUSBDescriptorType`](../tiousbdescriptortype.md).
- `length`: A pointer to a variable containing the size of the descriptor you want to fetch. Typically, you use the `sizeof` keyword to specify the size of the descriptor structure you want. On return, this method replaces that value with the actual size of the descriptor, which might include additional child descriptors. Use the returned value when fetching variable-length configuration or BOS descriptors, or when fetching nonstandard descriptor types.
- `index`: The descriptor’s index value.
- `languageID`: The descriptor language ID.
- `requestType`: The request type to use. For a list of possible values, see [`tIOUSBDeviceRequestTypeValue`](../tiousbdevicerequesttypevalue.md).
- `requestRecipient`: The request recipient to use. For a list of possible values, see [`tIOUSBDeviceRequestRecipientValue`](../tiousbdevicerequestrecipientvalue.md).
- `descriptor`: A pointer to a variable. On output, this variable contains the retrieved descriptor. The descriptor must be the same size, or larger than, the input value in the `length` parameter.

## See Also

### Getting the Device Descriptors
- [CopyCapabilityDescriptors](./copycapabilitydescriptors.md)
  Returns the device’s capability descriptors.
- [CopyConfigurationDescriptor](./copyconfigurationdescriptor-lej1.md)
  Returns the configuration descriptor with the specified index.
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
- [tIOUSBDeviceRequestTypeValue](../tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [tIOUSBDeviceRequestRecipientValue](../tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.
- [Descriptor Utilities](../descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/copydescriptor)*