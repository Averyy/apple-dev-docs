# tIOUSBDeviceRequestRecipientValue

**Framework**: USBDriverKit  
**Kind**: enum

Constants indicating the type of object that receives the results of a request.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBDeviceRequestRecipientValue : unsigned int;
```

## Topics

### Getting the Request Recipient
- [kIOUSBDeviceRequestRecipientValueDevice](tiousbdevicerequestrecipientvalue/kiousbdevicerequestrecipientvaluedevice.md)
  The recipient is a device object.
- [kIOUSBDeviceRequestRecipientValueInterface](tiousbdevicerequestrecipientvalue/kiousbdevicerequestrecipientvalueinterface.md)
  The recipient is an interface object.
- [kIOUSBDeviceRequestRecipientValueEndpoint](tiousbdevicerequestrecipientvalue/kiousbdevicerequestrecipientvalueendpoint.md)
  The recipient is an endpoint.
- [kIOUSBDeviceRequestRecipientValueOther](tiousbdevicerequestrecipientvalue/kiousbdevicerequestrecipientvalueother.md)
  The recipient is another type of entity.

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
- [CopyStringDescriptor](iousbhostdevice/copystringdescriptor-28ybo.md)
  Returns a string descriptor from the device.
- [CopyStringDescriptor](iousbhostdevice/copystringdescriptor-9h8l2.md)
  Returns a string descriptor from the device.
- [CopyDescriptor](iousbhostdevice/copydescriptor.md)
  Retrieves any type of descriptor from the cache or the device.
- [tIOUSBDeviceRequestTypeValue](tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbdevicerequestrecipientvalue)*