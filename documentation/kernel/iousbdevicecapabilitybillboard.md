# IOUSBDeviceCapabilityBillboard

**Framework**: Kernel  
**Kind**: tdef

The structure for the billboard device capability.

**Availability**:
- macOS 10.12+

## Declaration

```swift
typedef struct IOUSBDeviceCapabilityBillboard IOUSBDeviceCapabilityBillboard;
```

#### Discussion

For more information about this descriptor type, see USB 3.2, 9.6.2.

## Topics

### Getting the Properties
- [bLength](iousbdevicecapabilitybillboard/1646375-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbdevicecapabilitybillboard/1646372-bdescriptortype.md)
  The type of the descriptor.
- [bDevCapabilityType](iousbdevicecapabilitybillboard/1646365-bdevcapabilitytype.md)
  The device capability descriptor type.
- [iAdditionalInfoURL](iousbdevicecapabilitybillboard/1646386-iadditionalinfourl.md)
  The index of a string descriptor providing a URL for detailed information about the product and supported modes.
- [bNumberOfAlternateModes](iousbdevicecapabilitybillboard/1646385-bnumberofalternatemodes.md)
  The number of alternative supported modes.
- [bPreferredAlternateMode](iousbdevicecapabilitybillboard/1646361-bpreferredalternatemode.md)
  The index of the preferred alternative mode.
- [vCONNPower](iousbdevicecapabilitybillboard/1646367-vconnpower.md)
  The power that the adapter needs for full functionality.
- [bmConfigured](iousbdevicecapabilitybillboard/1646380-bmconfigured.md)
  A value that indicates the state of the alternative modes.
- [bcdVersion](iousbdevicecapabilitybillboard/1792100-bcdversion.md)
  The billboard capability version number.
- [bAdditionalFailureInfo](iousbdevicecapabilitybillboard/1792101-badditionalfailureinfo.md)
  A value that indicates additional information on failures.
- [bReserved](iousbdevicecapabilitybillboard/1646357-breserved.md)
  Reserved for future use.
- [pAltConfigurations](iousbdevicecapabilitybillboard/1646374-paltconfigurations.md)
  An array of alternative configurations.

## See Also

- [IOUSBPlatformCapabilityDescriptor](iousbplatformcapabilitydescriptor.md)
  The structure for the platform capability descriptor.
- [IOUSBPlatformCapabilityDescriptorPtr](iousbplatformcapabilitydescriptorptr.md)
  A pointer to a USB platform capability descriptor.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboard)*