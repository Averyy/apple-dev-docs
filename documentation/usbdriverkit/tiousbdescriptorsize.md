# tIOUSBDescriptorSize

**Framework**: USBDriverKit  
**Kind**: enum

Constants for the number of bytes in descriptor structures.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBDescriptorSize : unsigned int;
```

## Topics

### Getting the Descriptor Size
- [kIOUSBDescriptorHeaderSize](tiousbdescriptorsize/kiousbdescriptorheadersize.md)
  The size of a descriptor header.
- [kIOUSBDescriptorSizeDevice](tiousbdescriptorsize/kiousbdescriptorsizedevice.md)
  The size of a device descriptor.
- [kIOUSBDescriptorSizeConfiguration](tiousbdescriptorsize/kiousbdescriptorsizeconfiguration.md)
  The size of a configuration descriptor.
- [kIOUSBDescriptorSizeInterface](tiousbdescriptorsize/kiousbdescriptorsizeinterface.md)
  The size of an interface descriptor.
- [kIOUSBDescriptorSizeEndpoint](tiousbdescriptorsize/kiousbdescriptorsizeendpoint.md)
  The size of an endpoint descriptor.
- [kIOUSBDescriptorSizeStringMinimum](tiousbdescriptorsize/kiousbdescriptorsizestringminimum.md)
  The minimum size of a string descriptor.
- [kIOUSBDescriptorSizeStringMaximum](tiousbdescriptorsize/kiousbdescriptorsizestringmaximum.md)
  The maximum size of a string descriptor.
- [kIOUSBDescriptorSizeDeviceQualifier](tiousbdescriptorsize/kiousbdescriptorsizedevicequalifier.md)
  The size of a device qualifier descriptor.
- [kIOUSBDescriptorSizeInterfaceAssociation](tiousbdescriptorsize/kiousbdescriptorsizeinterfaceassociation.md)
  The size of an interface association descriptor.
- [kIOUSBDescriptorSizeBOS](tiousbdescriptorsize/kiousbdescriptorsizebos.md)
  The size of a binary object store descriptor.
- [kIOUSBDescriptorSizeDeviceCapability](tiousbdescriptorsize/kiousbdescriptorsizedevicecapability.md)
  The size of a device capability descriptor.
- [kIOUSBDescriptorSizeUSB20ExtensionCapability](tiousbdescriptorsize/kiousbdescriptorsizeusb20extensioncapability.md)
  The size of a USB 2.0 extension capability descriptor.
- [kIOUSBDescriptorSizeSuperSpeedUSBDeviceCapability](tiousbdescriptorsize/kiousbdescriptorsizesuperspeedusbdevicecapability.md)
  The size of a super-speed device capability descriptor.
- [kIOUSBDescriptorSizeContainerIDCapability](tiousbdescriptorsize/kiousbdescriptorsizecontaineridcapability.md)
  The size of a container ID capability descriptor.
- [kIOUSBDescriptorSizeHubMinimum](tiousbdescriptorsize/kiousbdescriptorsizehubminimum.md)
  The minimum size of a hub descriptor.
- [kIOUSBDescriptorSizeHubMaximum](tiousbdescriptorsize/kiousbdescriptorsizehubmaximum.md)
  The maximum size of a hub descriptor.
- [kIOUSBDescriptorSizeSuperSpeedHub](tiousbdescriptorsize/kiousbdescriptorsizesuperspeedhub.md)
  The size of a super-speed hub descriptor.
- [kIOUSBDescriptorSizeSuperSpeedUSBEndpointCompanion](tiousbdescriptorsize/kiousbdescriptorsizesuperspeedusbendpointcompanion.md)
  The size of a super-speed endpoint companion descriptor.
- [kIOUSBDescriptorSizeSuperSpeedPlusIsochronousEndpointCompanion](tiousbdescriptorsize/kiousbdescriptorsizesuperspeedplusisochronousendpointcompanion.md)
  The size of a super-speed plus isochronous endpoint companion descriptor.
- [kIOUSBDescriptorSizeBillboardDeviceMinimum](tiousbdescriptorsize/kiousbdescriptorsizebillboarddeviceminimum.md)
  The minimum size of a billboard descriptor.
- [kIOUSBDescriptorSizeBillboardDeviceMaximum](tiousbdescriptorsize/kiousbdescriptorsizebillboarddevicemaximum.md)
  The maximum size of a billboard descriptor.
- [kIOUSBDescriptorSizePlatformECIDCapability](tiousbdescriptorsize/kiousbdescriptorsizeplatformecidcapability.md)
  The size of a platform ECID capability descriptor.
- [kIOUSBDescriptorSizePlatformCapability](tiousbdescriptorsize/kiousbdescriptorsizeplatformcapability.md)
  The size of a platform capability descriptor.

## See Also

- [IOUSBDescriptorHeader](iousbdescriptorheader.md)
  The base descriptor header.
- [IOUSBDescriptor](iousbdescriptor.md)
  The base descriptor type.
- [tIOUSBDescriptorType](tiousbdescriptortype.md)
  Constants describing the types of descriptors available for a USB device.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbdescriptorsize)*