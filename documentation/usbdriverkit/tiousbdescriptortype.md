# tIOUSBDescriptorType

**Framework**: USBDriverKit  
**Kind**: enum

Constants describing the types of descriptors available for a USB device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBDescriptorType : unsigned int;
```

#### Overview

When you fetch descriptors from a USB device, the data includes a one-byte value that indicates the type of the descriptor. Use these constants to determine the type.

For detailed information about the descriptor types, see Table 9-5 of the USB 2.0 specification and Table 9-6 of the USB 3.0 specification at [`https://www.usb.org/`](https://developer.apple.comhttps://www.usb.org/).

## Topics

### Getting the Descriptor Type
- [kIOUSBDescriptorTypeDevice](tiousbdescriptortype/kiousbdescriptortypedevice.md)
  The type for a device descriptor.
- [kIOUSBDescriptorTypeConfiguration](tiousbdescriptortype/kiousbdescriptortypeconfiguration.md)
  The type for a configuration descriptor.
- [kIOUSBDescriptorTypeString](tiousbdescriptortype/kiousbdescriptortypestring.md)
  The type for a string descriptor.
- [kIOUSBDescriptorTypeInterface](tiousbdescriptortype/kiousbdescriptortypeinterface.md)
  The type for an interface descriptor.
- [kIOUSBDescriptorTypeEndpoint](tiousbdescriptortype/kiousbdescriptortypeendpoint.md)
  The type for an endpoint descriptor.
- [kIOUSBDescriptorTypeDeviceQualifier](tiousbdescriptortype/kiousbdescriptortypedevicequalifier.md)
  The type for a device qualifier descriptor.
- [kIOUSBDescriptorTypeOtherSpeedConfiguration](tiousbdescriptortype/kiousbdescriptortypeotherspeedconfiguration.md)
  The type for an other speed configuration descriptor.
- [kIOUSBDescriptorTypeInterfacePower](tiousbdescriptortype/kiousbdescriptortypeinterfacepower.md)
  The type for an interface power descriptor.
- [kIOUSBDescriptorTypeOTG](tiousbdescriptortype/kiousbdescriptortypeotg.md)
  The type for an on-the-go descriptor.
- [kIOUSBDescriptorTypeDebug](tiousbdescriptortype/kiousbdescriptortypedebug.md)
  The type for a debug descriptor.
- [kIOUSBDescriptorTypeInterfaceAssociation](tiousbdescriptortype/kiousbdescriptortypeinterfaceassociation.md)
  The type for an interface association descriptor.
- [kIOUSBDescriptorTypeBOS](tiousbdescriptortype/kiousbdescriptortypebos.md)
  The type for a binary object store descriptor.
- [kIOUSBDescriptorTypeDeviceCapability](tiousbdescriptortype/kiousbdescriptortypedevicecapability.md)
  The type for a capability descriptor.
- [kIOUSBDecriptorTypeHID](tiousbdescriptortype/kiousbdecriptortypehid.md)
  The type for a human interaction device descriptor.
- [kIOUSBDecriptorTypeReport](tiousbdescriptortype/kiousbdecriptortypereport.md)
  The type for a report descriptor.
- [kIOUSBDescriptorTypePhysical](tiousbdescriptortype/kiousbdescriptortypephysical.md)
  The type for a physical descriptor.
- [kIOUSBDescriptorTypeHub](tiousbdescriptortype/kiousbdescriptortypehub.md)
  The type for a hub descriptor.
- [kIOUSBDescriptorTypeSuperSpeedHub](tiousbdescriptortype/kiousbdescriptortypesuperspeedhub.md)
  The type for a super-speed hub descriptor.
- [kIOUSBDescriptorTypeSuperSpeedUSBEndpointCompanion](tiousbdescriptortype/kiousbdescriptortypesuperspeedusbendpointcompanion.md)
  The type for a super-speed endpoint companion descriptor.
- [kIOUSBDescriptorTypeSuperSpeedPlusIsochronousEndpointCompanion](tiousbdescriptortype/kiousbdescriptortypesuperspeedplusisochronousendpointcompanion.md)
  The type for a super-speed plus isochronous endpoint companion descriptor.

## See Also

- [IOUSBDescriptorHeader](iousbdescriptorheader.md)
  The base descriptor header.
- [IOUSBDescriptor](iousbdescriptor.md)
  The base descriptor type.
- [tIOUSBDescriptorSize](tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbdescriptortype)*