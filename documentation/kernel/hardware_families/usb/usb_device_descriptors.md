# USB Device Descriptors

**Framework**: Kernel

Structures and functions for working with device descriptors.

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
- [IOUSBDescriptorHeaderPtr](iousbdescriptorheaderptr.md)
  A pointer to a USB descriptor header.
### Device Descriptors
- [IOUSBDeviceDescriptor](iousbdevicedescriptor.md)
  The structure for storing a USB device descriptor.
- [IOUSBDeviceDescriptorPtr](iousbdevicedescriptorptr.md)
  A pointer to a USB device descriptor.
- [IOUSBDeviceQualifierDescriptor](iousbdevicequalifierdescriptor.md)
  The structure for describing a high-speed capable USB device.
- [IOUSBDeviceQualifierDescriptorPtr](iousbdevicequalifierdescriptorptr.md)
  A pointer to a qualifier descriptor.
### Configuration Descriptors
- [IOUSBConfigurationDescriptor](iousbconfigurationdescriptor.md)
  The structure for storing a USB configuration descriptor.
- [IOUSBConfigurationDescHeader](iousbconfigurationdescheader.md)
  The header of a configuration descriptor.
- [IOUSBConfigurationDescriptorPtr](iousbconfigurationdescriptorptr.md)
  A pointer to a configuration descriptor.
- [IOUSBConfigurationDescHeaderPtr](iousbconfigurationdescheaderptr.md)
  A pointer to a configuration descriptor header.
### Interface Descriptors
- [IOUSBInterfaceDescriptor](iousbinterfacedescriptor.md)
  A descriptor for a specific interface of a USB device.
- [IOUSBInterfaceDescriptorPtr](iousbinterfacedescriptorptr.md)
  A pointer to a USB interface descriptor.
- [IOUSBInterfaceAssociationDescriptor](iousbinterfaceassociationdescriptor.md)
  The descriptor that associates multiple interfaces to the same function.
- [IOUSBInterfaceAssociationDescriptorPtr](iousbinterfaceassociationdescriptorptr.md)
  A pointer to a USB interface association descriptor.
### Endpoint Descriptors
- [IOUSBEndpointDescriptor](iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.
- [IOUSBStandardEndpointDescriptors](iousbstandardendpointdescriptors.md)
  A container for descriptors for a single endpoint.
- [IOUSBEndpointDescriptorPtr](iousbendpointdescriptorptr.md)
  A pointer to the endpoint descriptor.
- [IOUSBEndpointProperties](iousbendpointproperties.md)
  A structure that holds USB endpoint properties.
- [IOUSBEndpointPropertiesPtr](iousbendpointpropertiesptr.md)
  A pointer to an endpoint properties object.
- [IOUSBGetEndpointDescriptorOptions](iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.
### Capability Descriptors
- [IOUSBPlatformCapabilityDescriptor](iousbplatformcapabilitydescriptor.md)
  The structure for the platform capability descriptor.
- [IOUSBPlatformCapabilityDescriptorPtr](iousbplatformcapabilitydescriptorptr.md)
  A pointer to a USB platform capability descriptor.
- [IOUSBDeviceCapabilityBillboard](iousbdevicecapabilitybillboard.md)
  The structure for the billboard device capability.
- [IOUSBDeviceCapabilityBillboardAltConfig](iousbdevicecapabilitybillboardaltconfig.md)
  The structure for the billboard alternative configuration device capability.
- [IOUSBDeviceCapabilityBillboardAltConfigCompatibility](iousbdevicecapabilitybillboardaltconfigcompatibility.md)
  The structure for the billboard alternative configuration compatibility device capability.
- [IOUSBDeviceCapabilityBillboardAltConfigPtr](iousbdevicecapabilitybillboardaltconfigptr.md)
  A pointer to a USB device capability billboard alternative configuration structure.
- [IOUSBDeviceCapabilityBillboardAltMode](iousbdevicecapabilitybillboardaltmode.md)
  The structure for the billboard alternative mode device capability.
- [IOUSBDeviceCapabilityBillboardAltModePtr](iousbdevicecapabilitybillboardaltmodeptr.md)
  A pointer to a USB device capability billboard alternative mode structure.
- [IOUSBDeviceCapabilityBillboardPtr](iousbdevicecapabilitybillboardptr.md)
  A pointer to a USB device capability billboard object.
- [IOUSBDeviceCapabilityContainerID](iousbdevicecapabilitycontainerid.md)
  The structure for the container ID device capability.
- [IOUSBDeviceCapabilityContainerIDPtr](iousbdevicecapabilitycontaineridptr.md)
  A pointer to a USB device capability container ID.
- [IOUSBDeviceCapabilityDescriptorHeader](iousbdevicecapabilitydescriptorheader.md)
  The device capability descriptor header.
- [IOUSBDeviceCapabilityDescriptorHeaderPtr](iousbdevicecapabilitydescriptorheaderptr.md)
  A pointer to a device capability descriptor header.
- [IOUSBDeviceCapabilitySuperSpeedPlusUSB](iousbdevicecapabilitysuperspeedplususb.md)
  The structure for the SuperSpeedPlus USB device capability.
- [IOUSBDeviceCapabilitySuperSpeedPlusUSBPtr](iousbdevicecapabilitysuperspeedplususbptr.md)
  A pointer to a SuperSpeedPlus USB device capability structure.
- [IOUSBDeviceCapabilitySuperSpeedUSB](iousbdevicecapabilitysuperspeedusb.md)
  The structure for the SuperSpeed USB device capability.
- [IOUSBDeviceCapabilitySuperSpeedUSBPtr](iousbdevicecapabilitysuperspeedusbptr.md)
  A pointer to a SuperSpeed USB device capability structure.
- [IOUSBDeviceCapabilityUSB2Extension](iousbdevicecapabilityusb2extension.md)
  The structure for the USB 2.0 extension device capability.
- [IOUSBDeviceCapabilityUSB2ExtensionPtr](iousbdevicecapabilityusb2extensionptr.md)
  A pointer to a USB 2.0 extension device capability structure.
### USB Descriptors
- [IOUSBStringDescriptor](iousbstringdescriptor.md)
  The structure for storing a string descriptor.
- [IOUSBStringDescriptorPtr](iousbstringdescriptorptr.md)
  A pointer to a string descriptor structure.
- [IOUSBSuperSpeedEndpointCompanionDescriptor](iousbsuperspeedendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [IOUSBSuperSpeedEndpointCompanionDescriptorPtr](iousbsuperspeedendpointcompaniondescriptorptr.md)
  A pointer to a SuperSpeed USB endpoint companion descriptor.
- [IOUSBSuperSpeedHubDescriptor](iousbsuperspeedhubdescriptor.md)
  A structure that defines the descriptor for a SuperSpeed USB hub.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbsuperspeedplusisochronousendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptorPtr](iousbsuperspeedplusisochronousendpointcompaniondescriptorptr.md)
  A pointer to a SuperSpeedPlus isochronous USB endpoint companion descriptor.
### HID Descriptors
- [IOUSBHIDData](iousbhiddata.md)
  Data related to the mouse and keyboard.
- [IOUSBHIDDataPtr](iousbhiddataptr.md)
  A pointer to a structure related to mouse and keyboard data.
- [IOUSBHIDDescriptor](iousbhiddescriptor.md)
  A structure that defines the USB HID descriptor.
- [IOUSBHIDDescriptorPtr](iousbhiddescriptorptr.md)
  A pointer to a structure that defines the USB HID descriptor.
- [IOUSBHIDReportDesc](iousbhidreportdesc.md)
  A structure that defines the USB HID report descriptor header.
- [IOUSBHIDReportDescPtr](iousbhidreportdescptr.md)
  A pointer to a structure that defines the USB HID report descriptor header.
### Device Firmware Update Descriptors
- [IOUSBDFUDescriptor](iousbdfudescriptor.md)
  A structure that defines the USB device firmware update descriptor.
- [IOUSBDFUDescriptorPtr](iousbdfudescriptorptr.md)
  A pointer to a structure that defines the USB device firmware update descriptor.
### BOS Descriptors
- [IOUSBBOSDescriptor](iousbbosdescriptor.md)
  The structure for storing a binary object store (BOS) descriptor.
- [IOUSBBOSDescriptorPtr](iousbbosdescriptorptr.md)
  A pointer to a structure for storing a binary object store (BOS) descriptor.
### Hub Descriptors
- [IOUSB20HubDescriptor](iousb20hubdescriptor.md)
  A structure that defines the descriptor for a USB 2.0 hub.
- [IOUSB3HubDescriptor](iousb3hubdescriptor.md)
  A structure that defines the descriptor for a USB 3.0 hub.
- [IOUSBHubDescriptor](iousbhubdescriptor.md)
  A structure that defines the descriptor for a USB hub.
- [IOUSBHubPortReEnumerateParam](iousbhubportreenumerateparam.md)
  A structure for USB hub port reenumeration.

## See Also

- [IOUSBIsochronousFrame](iousbisochronousframe.md)
  A structure representing a single frame in an isochronous transfer.
- [Additional Specifications](hardware_families/usb/additional_specifications.md)
  Structures related to hubs, devices, and endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/usb/usb_device_descriptors)*