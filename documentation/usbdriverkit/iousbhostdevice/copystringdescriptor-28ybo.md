# CopyStringDescriptor

**Framework**: USBDriverKit  
**Kind**: method

Returns a string descriptor from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBStringDescriptor * CopyStringDescriptor(uint8_t index, uint16_t languageID);
```

#### Return Value

A pointer to the descriptor, if found. It’s your responsibility to free the returned descriptor.

#### Discussion

This method searches the descriptor cache for the specified descriptor. If the descriptor isn’t in the cache, the method retrieves it from the device using a `GET_DESCRIPTOR` control request (USB 2.0, section 9.4.3) and adds it to the cache. When making a `GET_DESCRIPTOR` control request, this method acquires the service’s workloop lock and may call [`commandSleep`](https://developer.apple.com/documentation/kernel/iocommandgate/1573818-commandsleep).

## Parameters

- `index`: The descriptor index value. This parameter corresponds to the low byte of   of the   control request (USB 2.0, section 9.4.8).
- `languageID`: The descriptor language ID. This parameter corresponds to the   value of the   control request (USB 2.0, section 9.4.8).

## See Also

- [CopyCapabilityDescriptors](iousbhostdevice/copycapabilitydescriptors.md)
  Returns the device’s capability descriptors.
- [CopyConfigurationDescriptor](iousbhostdevice/copyconfigurationdescriptor-lej1.md)
  Returns the configuration descriptor with the specified index.
- [CopyConfigurationDescriptor](iousbhostdevice/copyconfigurationdescriptor-6qgew.md)
  Returns the currently selected configuration descriptor.
- [CopyConfigurationDescriptorWithValue](iousbhostdevice/copyconfigurationdescriptorwithvalue.md)
  Returns the configuration descriptor with the specified configuration value.
- [CopyDeviceDescriptor](iousbhostdevice/copydevicedescriptor.md)
  Returns the device descriptor.
- [CopyStringDescriptor](iousbhostdevice/copystringdescriptor-9h8l2.md)
  Returns a string descriptor from the device.
- [CopyDescriptor](iousbhostdevice/copydescriptor.md)
  Retrieves any type of descriptor from the cache or the device.
- [tIOUSBDeviceRequestTypeValue](tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [tIOUSBDeviceRequestRecipientValue](tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/copystringdescriptor-28ybo)*