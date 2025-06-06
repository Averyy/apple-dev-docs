# Descriptor Utilities

**Framework**: USBDriverKit

Iterate over the descriptors of a USB device and fetch specific values.

## Topics

### Configuration Descriptors
- [IOUSBGetNextDescriptor](iousbgetnextdescriptor.md)
  Gets the next descriptor in a configuration descriptor.
- [IOUSBGetNextDescriptorWithType](iousbgetnextdescriptorwithtype.md)
  Finds the next descriptor matching a given type within a configuration descriptor.
- [IOUSBGetNextAssociatedDescriptor](iousbgetnextassociateddescriptor.md)
  Gets the next descriptor in the specified configuration descriptor that belongs to another container descriptor.
- [IOUSBGetNextAssociatedDescriptorWithType](iousbgetnextassociateddescriptorwithtype.md)
  Finds the next descriptor matching a specific type within a configuration descriptor that belongs to another container descriptor.
- [IOUSBGetConfigurationMaxPowerMilliAmps](iousbgetconfigurationmaxpowermilliamps.md)
  Extracts the maximum bus current a configuration descriptor requires.
### Interface Descriptors
- [IOUSBGetNextInterfaceDescriptor](iousbgetnextinterfacedescriptor.md)
  Finds the next interface descriptor in a configuration descriptor.
- [IOUSBGetNextInterfaceAssociationDescriptor](iousbgetnextinterfaceassociationdescriptor.md)
  Finds the next interface association descriptor in a configuration descriptor.
### Endpoint Descriptors
- [IOUSBGetNextEndpointDescriptor](iousbgetnextendpointdescriptor.md)
  Finds the next endpoint descriptor associated with an interface descriptor.
- [IOUSBGetEndpointAddress](iousbgetendpointaddress.md)
  Extracts the direction and number of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointBurstSize](iousbgetendpointburstsize.md)
  Extracts the burst size from endpoint descriptors.
- [IOUSBGetEndpointDirection](iousbgetendpointdirection.md)
  Extracts the direction of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointIntervalEncodedMicroframes](iousbgetendpointintervalencodedmicroframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointIntervalFrames](iousbgetendpointintervalframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointIntervalMicroframes](iousbgetendpointintervalmicroframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointMaxPacketSize](iousbgetendpointmaxpacketsize.md)
  Extracts the maximum packet size from an endpoint descriptor.
- [IOUSBGetEndpointMaxStreams](iousbgetendpointmaxstreams.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointMaxStreamsEncoded](iousbgetendpointmaxstreamsencoded.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointMult](iousbgetendpointmult.md)
  Extracts the mult count from endpoint descriptors.
- [IOUSBGetEndpointNumber](iousbgetendpointnumber.md)
  Extracts the number of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointType](iousbgetendpointtype.md)
  Extracts the type of an endpoint from an endpoint descriptor.
### BOS Descriptors
- [IOUSBGetNextCapabilityDescriptor](iousbgetnextcapabilitydescriptor.md)
  Gets the next device capability descriptor in a BOS descriptor.
- [IOUSBGetNextCapabilityDescriptorWithType](iousbgetnextcapabilitydescriptorwithtype.md)
  Finds the next descriptor matching a given type within a BOS descriptor.
- [IOUSBGetSuperSpeedDeviceCapabilityDescriptor](iousbgetsuperspeeddevicecapabilitydescriptor.md)
  Finds the first SuperSpeed device capability descriptor in a BOS descriptor.
- [IOUSBGetSuperSpeedPlusDeviceCapabilityDescriptor](iousbgetsuperspeedplusdevicecapabilitydescriptor.md)
  Finds the first SuperSpeed Plus device capability descriptor in a BOS descriptor.
- [IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor](iousbgetusb20extensiondevicecapabilitydescriptor.md)
  Finds the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [IOUSBGetContainerIDDescriptor](iousbgetcontaineriddescriptor.md)
  Finds the first Container ID capability descriptor in a BOS descriptor.
- [IOUSBGetPlatformCapabilityDescriptor](iousbgetplatformcapabilitydescriptor.md)
  Finds the first platform capability descriptor in a BOS descriptor.
- [IOUSBGetBillboardDescriptor](iousbgetbillboarddescriptor.md)
  Finds the first billboard capability descriptor in a BOS descriptor.

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
- [tIOUSBDeviceRequestRecipientValue](tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/descriptor-utilities)*