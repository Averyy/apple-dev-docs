# USB.h User-Space

**Framework**: IOKit  
**Role**: API Collection

#### Overview

##### Included Headers

- <libkern/OSByteOrder.h>
- <IOKit/IOMemoryDescriptor.h>
- <libkern/OSByteOrder.h>
- <IOKit/IOTypes.h>

## Topics

### UNKNOWN OBJECT 
- [iokit_usb_err](./iokit_usb_err.md)
- [iokit_usb_msg](./iokit_usb_msg.md)
### Miscellaneous
- [EncodeRequest](./encoderequest.md)
- [USBmakebmRequestType](./usbmakebmrequesttype.md)
### Callbacks
- [IOUSBCompletionAction](./iousbcompletionaction.md)
- [IOUSBCompletionActionWithTimeStamp](./iousbcompletionactionwithtimestamp.md)
- [IOUSBIsocCompletionAction](./iousbisoccompletionaction.md)
- [IOUSBLowLatencyIsocCompletionAction](./iousblowlatencyisoccompletionaction.md)
### Data Types
- [IOUSBBOSDescriptor](./iousbbosdescriptor.md)
- [IOUSBCompletion](./iousbcompletion.md)
- [IOUSBCompletionWithTimeStamp](./iousbcompletionwithtimestamp.md)
- [IOUSBConfigurationDescHeader](./iousbconfigurationdescheader.md)
- [IOUSBConfigurationDescriptor](./iousbconfigurationdescriptor.md)
- [IOUSBDescriptorHeader](./iousbdescriptorheader.md)
- [IOUSBDeviceCapabilityContainerID](./iousbdevicecapabilitycontainerid.md)
- [IOUSBDeviceCapabilityDescriptorHeader](./iousbdevicecapabilitydescriptorheader.md)
- [IOUSBDeviceCapabilitySuperSpeedUSB](./iousbdevicecapabilitysuperspeedusb.md)
- [IOUSBDeviceCapabilityUSB2Extension](./iousbdevicecapabilityusb2extension.md)
- [IOUSBDeviceDescriptor](./iousbdevicedescriptor.md)
- [IOUSBDeviceQualifierDescriptor](./iousbdevicequalifierdescriptor.md)
- [IOUSBDevRequest](./iousbdevrequest.md)
- [IOUSBDevRequestDesc](../kernel/iousbdevrequestdesc.md)
- [IOUSBDevRequestTO](./iousbdevrequestto.md)
- [IOUSBDFUDescriptor](./iousbdfudescriptor.md)
- [IOUSBEndpointDescriptor](./iousbendpointdescriptor.md)
- [IOUSBFindEndpointRequest](./iousbfindendpointrequest.md)
- [IOUSBFindInterfaceRequest](./iousbfindinterfacerequest.md)
- [IOUSBGetFrameStruct](./iousbgetframestruct.md)
- [IOUSBHIDDescriptor](./iousbhiddescriptor.md)
- [IOUSBHIDReportDesc](./iousbhidreportdesc.md)
- [IOUSBInterfaceAssociationDescriptor](./iousbinterfaceassociationdescriptor.md)
- [IOUSBInterfaceDescriptor](./iousbinterfacedescriptor.md)
- [IOUSBIsocCompletion](./iousbisoccompletion.md)
- [IOUSBIsocFrame](./iousbisocframe.md)
- [IOUSBLowLatencyIsocCompletion](./iousblowlatencyisoccompletion.md)
- [IOUSBLowLatencyIsocFrame](./iousblowlatencyisocframe.md)
- [IOUSBSuperSpeedEndpointCompanionDescriptor](./iousbsuperspeedendpointcompaniondescriptor.md)
- [USBDeviceInformationBits](./usbdeviceinformationbits.md)
- [USBLowLatencyBufferType](./usblowlatencybuffertype.md)
- [USBPowerRequestTypes](./usbpowerrequesttypes.md)
- [USBReEnumerateOptions](./usbreenumerateoptions.md)
- [USBStatus](./usbstatus.md)
- [IOUSBBOSDescriptor](./usb_h_user-space/iousbbosdescriptor.md)
- [IOUSBConfigurationDescHeader](./usb_h_user-space/iousbconfigurationdescheader.md)
- [IOUSBConfigurationDescriptor](./usb_h_user-space/iousbconfigurationdescriptor.md)
- [IOUSBDescriptorHeader](./usb_h_user-space/iousbdescriptorheader.md)
- [IOUSBDeviceCapabilityContainerID](./usb_h_user-space/iousbdevicecapabilitycontainerid.md)
- [IOUSBDeviceCapabilityDescriptorHeader](./usb_h_user-space/iousbdevicecapabilitydescriptorheader.md)
- [IOUSBDeviceCapabilitySuperSpeedUSB](./usb_h_user-space/iousbdevicecapabilitysuperspeedusb.md)
- [IOUSBDeviceCapabilityUSB2Extension](./usb_h_user-space/iousbdevicecapabilityusb2extension.md)
- [IOUSBDeviceDescriptor](./usb_h_user-space/iousbdevicedescriptor.md)
- [IOUSBDeviceQualifierDescriptor](./usb_h_user-space/iousbdevicequalifierdescriptor.md)
- [IOUSBDFUDescriptor](./usb_h_user-space/iousbdfudescriptor.md)
- [IOUSBEndpointDescriptor](./usb_h_user-space/iousbendpointdescriptor.md)
- [IOUSBHIDDescriptor](./usb_h_user-space/iousbhiddescriptor.md)
- [IOUSBHIDReportDesc](./usb_h_user-space/iousbhidreportdesc.md)
- [IOUSBInterfaceAssociationDescriptor](./usb_h_user-space/iousbinterfaceassociationdescriptor.md)
- [IOUSBInterfaceDescriptor](./usb_h_user-space/iousbinterfacedescriptor.md)
- [IOUSBLowLatencyIsocFrame](./usb_h_user-space/iousblowlatencyisocframe.md)
- [IOUSBSuperSpeedEndpointCompanionDescriptor](./usb_h_user-space/iousbsuperspeedendpointcompaniondescriptor.md)
### Constants
- [Endian conversion definitions](./usb_h_user-space/endian_conversion_definitions.md)
  Public Interfaces to the USB implementation in macOS.
- [IOUSBFamily error codes](./usb_h_user-space/iousbfamily_error_codes.md)
- [IOUSBFamily hardware error codes](./usb_h_user-space/iousbfamily_hardware_error_codes.md)
- [IOUSBFamily message codes](./usb_h_user-space/iousbfamily_message_codes.md)
- [Property Definitions](./usb_h_user-space/property_definitions.md)
- [Miscellaneous Defines](./usb_h_user-space/miscellaneous_defines.md)
- [bRequest Shifts and Masks](./api-1425528-brequest_shifts_and_masks.md)
- [Default timeout values](./api-1425913-default_timeout_values.md)
- [IOUSBFamilyIOOptionBit](./usb_h_user-space/iousbfamilyiooptionbit.md)
- [kIOUSBFindInterfaceDontCare](./api-1425505-kiousbfindinterfacedontcare.md)
- [kIOUSBVendorIDApple](./api-1426107-kiousbvendoridapple.md)
- [kUSBMaxIsocFrameReqCount](./api-1426268-kusbmaxisocframereqcount.md)
- [MicrosecondsInFrame](./api-1425805-microsecondsinframe.md)
- [Miscellaneous Constants](./api-1426201-miscellaneous_constants.md)
- [Standard Device Requests](./api-1425485-standard_device_requests.md)
- [USBDeviceSpeed](./api-1425357-usbdevicespeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space)*