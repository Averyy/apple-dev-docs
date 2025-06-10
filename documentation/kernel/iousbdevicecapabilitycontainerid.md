# IOUSBDeviceCapabilityContainerID

**Framework**: Kernel  
**Kind**: tdef

The structure for the container ID device capability.

**Availability**:
- macOS 10.7+

## Declaration

```swift
typedef struct IOUSBDeviceCapabilityContainerID IOUSBDeviceCapabilityContainerID;
```

#### Discussion

See USB 3.2, 9.6.2.3 for more information.

## Topics

### Getting the Properties
- [bLength](iousbdevicecapabilitycontainerid/1546211-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbdevicecapabilitycontainerid/1546207-bdescriptortype.md)
  The type of the descriptor.
- [bDevCapabilityType](iousbdevicecapabilitycontainerid/1546363-bdevcapabilitytype.md)
  The device capability type.
- [bReservedID](iousbdevicecapabilitycontainerid/1546323-breservedid.md)
  Reserved for future use.
- [containerID](iousbdevicecapabilitycontainerid/1545924-containerid.md)
  A number that uniquely identifies the device instance across all modes of operation.

## See Also

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
- [IOUSBDeviceCapabilityContainerID](../iokit/usb_h_user-space/iousbdevicecapabilitycontainerid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitycontainerid)*