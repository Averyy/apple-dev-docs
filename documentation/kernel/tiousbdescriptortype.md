# tIOUSBDescriptorType

**Framework**: Kernel  
**Kind**: tdef

Constants describing the types of descriptors available for a USB device.

**Availability**:
- macOS 10.15+

## Declaration

```swift
typedef enum tIOUSBDescriptorType tIOUSBDescriptorType;
```

#### Discussion

When you fetch descriptors from a USB device, the data includes a one-byte value that indicates the type of the descriptor. Use these constants to determine the type. 

For detailed information about the descriptor types, see USB 3.2, 9.4.

## Topics

### Getting the Descriptor Type
- [kIOUSBDecriptorTypeHID](tiousbdescriptortype/kiousbdecriptortypehid.md)
  The type for a human interaction device descriptor.
- [kIOUSBDecriptorTypeReport](tiousbdescriptortype/kiousbdecriptortypereport.md)
  The type for a report descriptor.
- [kIOUSBDescriptorTypePhysical](tiousbdescriptortype/kiousbdescriptortypephysical.md)
  The type for a physical descriptor.
### Constants
- [kIOUSBDescriptorTypeBOS](tiousbdescriptortype/kiousbdescriptortypebos.md)
- [kIOUSBDescriptorTypeConfiguration](tiousbdescriptortype/kiousbdescriptortypeconfiguration.md)
- [kIOUSBDescriptorTypeDebug](tiousbdescriptortype/kiousbdescriptortypedebug.md)
- [kIOUSBDescriptorTypeDevice](tiousbdescriptortype/kiousbdescriptortypedevice.md)
- [kIOUSBDescriptorTypeDeviceCapability](tiousbdescriptortype/kiousbdescriptortypedevicecapability.md)
- [kIOUSBDescriptorTypeDeviceQualifier](tiousbdescriptortype/kiousbdescriptortypedevicequalifier.md)
- [kIOUSBDescriptorTypeEndpoint](tiousbdescriptortype/kiousbdescriptortypeendpoint.md)
- [kIOUSBDescriptorTypeHub](tiousbdescriptortype/kiousbdescriptortypehub.md)
- [kIOUSBDescriptorTypeInterface](tiousbdescriptortype/kiousbdescriptortypeinterface.md)
- [kIOUSBDescriptorTypeInterfaceAssociation](tiousbdescriptortype/kiousbdescriptortypeinterfaceassociation.md)
- [kIOUSBDescriptorTypeInterfacePower](tiousbdescriptortype/kiousbdescriptortypeinterfacepower.md)
- [kIOUSBDescriptorTypeOTG](tiousbdescriptortype/kiousbdescriptortypeotg.md)
- [kIOUSBDescriptorTypeOtherSpeedConfiguration](tiousbdescriptortype/kiousbdescriptortypeotherspeedconfiguration.md)
- [kIOUSBDescriptorTypeString](tiousbdescriptortype/kiousbdescriptortypestring.md)
- [kIOUSBDescriptorTypeSuperSpeedHub](tiousbdescriptortype/kiousbdescriptortypesuperspeedhub.md)
- [kIOUSBDescriptorTypeSuperSpeedPlusIsochronousEndpointCompanion](tiousbdescriptortype/kiousbdescriptortypesuperspeedplusisochronousendpointcompanion.md)
- [kIOUSBDescriptorTypeSuperSpeedUSBEndpointCompanion](tiousbdescriptortype/kiousbdescriptortypesuperspeedusbendpointcompanion.md)

## See Also

- [IOUSBDescriptorHeader](iousbdescriptorheader.md)
  The base descriptor header.
- [IOUSBDescriptor](iousbdescriptor.md)
  The base descriptor type.
- [tIOUSBDescriptorSize](tiousbdescriptorsize.md)
  Constants for the number of bytes in descriptor structures.
- [IOUSBDescriptorHeaderPtr](iousbdescriptorheaderptr.md)
  A pointer to a USB descriptor header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/tiousbdescriptortype)*