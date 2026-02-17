# USB Device Descriptors

**Framework**: USBDriverKit

Determine the capabilities and configuration of a device using descriptors from the USB specification.

## Topics

### Descriptor Fundamentals
- [IOUSBDescriptorHeader](iousbdescriptorheader.md)
  The base descriptor header.
- [IOUSBDescriptor](iousbdescriptor.md)
  The base descriptor type.
- [tIOUSBDescriptorType](tiousbdescriptortype.md)
  Constants describing the types of descriptors available for a USB device.
- [tIOUSBDescriptorSize](tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.
### Device Descriptors
- [IOUSBDeviceDescriptor](iousbdevicedescriptor.md)
  The structure for storing a USB device descriptor.
- [IOUSBDeviceQualifierDescriptor](iousbdevicequalifierdescriptor.md)
  The structure for storing a USB device qualifier descriptor.
- [Apple’s Vendor ID](apple_s_vendor_id-enum.md)
  Apple’s vendor ID, assigned by the USB-IF.
### Configuration Descriptors
- [IOUSBConfigurationDescriptor](iousbconfigurationdescriptor.md)
  The structure for storing a USB configuration descriptor.
- [IOUSBConfigurationDescHeader](iousbconfigurationdescheader.md)
  The header of a configuration descriptor.
- [Power Configuration Settings](power_configuration_settings-enum.md)
  Constants for configuring the power settings.
### Interface Descriptors
- [IOUSBInterfaceDescriptor](iousbinterfacedescriptor.md)
  A descriptor for a specific interface of a USB device.
- [IOUSBInterfaceAssociationDescriptor](iousbinterfaceassociationdescriptor.md)
  The USB Interface Association Descriptor.
### Endpoint Descriptors
- [IOUSBEndpointDescriptor](iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.
- [IOUSBSuperSpeedEndpointCompanionDescriptor](iousbsuperspeedendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeed USB Endpoint Companion.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbsuperspeedplusisochronousendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus Isochronous USB Endpoint Companion.
- [tIOUSBEndpointType](tiousbendpointtype.md)
  Constants describing the types of endpoints.
- [Endpoint Attributes](endpoint_attributes-enum.md)
  Constants for endpoint attributes.
- [SuperSpeed USB Endpoint Descriptor Options](superspeed_usb_endpoint_descript-enum.md)
  Constants for super-speed endpoint attributes.
- [tIOUSBEndpointDirection](tiousbendpointdirection.md)
  The direction of data transfers on an endpoint.
- [tIOUSBEndpointSynchronizationType](tiousbendpointsynchronizationtype.md)
  Constants for the endpoint synchronization types.
- [tIOUSBEndpointUsageType](tiousbendpointusagetype.md)
  Constants for the endpoint usage types.
- [tIOUSBLanguageID](tiousblanguageid.md)
  Constants for the USB language identifiers.
### String Descriptor
- [IOUSBStringDescriptor](iousbstringdescriptor.md)
  The structure for storing a string descriptor.
### Capability Descriptors
- [IOUSBBOSDescriptor](iousbbosdescriptor.md)
  The structure for storing a binary object store (BOS) descriptor.
- [IOUSBDeviceCapabilityDescriptorHeader](iousbdevicecapabilitydescriptorheader.md)
  The device capability descriptor header.
- [IOUSBDeviceCapabilityBillboard](iousbdevicecapabilitybillboard.md)
  The structure for the billboard device capability.
- [IOUSBDeviceCapabilityBillboardAltConfig](iousbdevicecapabilitybillboardaltconfig.md)
  The structure for the billboard alternative configuration device capability.
- [IOUSBDeviceCapabilityBillboardAltConfigCompatibility](iousbdevicecapabilitybillboardaltconfigcompatibility.md)
  The structure for the billboard alternative configuration compatibility device capability.
- [IOUSBDeviceCapabilityBillboardAltMode](iousbdevicecapabilitybillboardaltmode.md)
  The structure for the billboard alternative mode device capability.
- [IOUSBDeviceCapabilityContainerID](iousbdevicecapabilitycontainerid.md)
  The structure for the container ID device capability.
- [IOUSBDeviceCapabilitySuperSpeedUSB](iousbdevicecapabilitysuperspeedusb.md)
  The structure for the super-speed USB device capability.
- [IOUSBDeviceCapabilitySuperSpeedPlusUSB](iousbdevicecapabilitysuperspeedplususb.md)
  The structure for the super-speed plus USB device capability.
- [IOUSBDeviceCapabilityUSB2Extension](iousbdevicecapabilityusb2extension.md)
  The structure for the USB 2 extension device capability.
- [IOUSBPlatformCapabilityDescriptor](iousbplatformcapabilitydescriptor.md)
  The structure for the platform capability descriptor.
- [tIOUSBDeviceCapabilityType](tiousbdevicecapabilitytype.md)
  Constants for the device capability types.
- [SuperSpeed Device Capabilities](superspeed_device_capabilities-enum.md)
  Constants for configuring super-speed device capabilities.
- [SuperSpeedPlus Device Capabilities](superspeedplus_device_capabiliti-enum.md)
  Constants for configuring super-speed plus device capabilities.
### USB Descriptors
- [IOUSB20HubDescriptor](iousb20hubdescriptor.md)
  A structure that defines the descriptor for a USB hub.
- [IOUSBSuperSpeedHubDescriptor](iousbsuperspeedhubdescriptor.md)
  A structure that defines the descriptor for a Super Speed USB hub.
- [SuperSpeed Hub Characteristics](superspeed_hub_characteristics-enum.md)
  Constants for specifying super-speed hub characteristics.
- [UASPipeDescriptor](uaspipedescriptor.md)
  A structure that defines the Mass Storage Specific UAS pipe usage descriptor.
### HID Descriptors
- [IOUSBHIDDescriptor](iousbhiddescriptor.md)
  A structure that defines the USB HID Descriptor.
- [IOUSBHIDReportDesc](iousbhidreportdesc.md)
  A structure that defines the USB HID Report Descriptor header.
### Firmware Update Descriptor
- [IOUSBDFUDescriptor](iousbdfudescriptor.md)
  A structure that defines the USB device firmware update descriptor.

## See Also

- [Additional Specifications](additional-specifications.md)
  Request information from a device and get hardware and timing information.
- [Registry Property Names](registry-property-names.md)
  Search for specific keys in the device registry.
- [Utilities](utilities.md)
  Manipulate bit structures and convert integers between device- and platform-native formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/usb-device-descriptors)*