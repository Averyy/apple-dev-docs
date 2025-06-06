# IOUSBBOSDescriptor

**Framework**: USBDriverKit  
**Kind**: struct

The structure for storing a binary object store (BOS) descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBBOSDescriptor;
```

#### Overview

For more information about this descriptor type, see section 9.6.2 of the USB 3.2 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Accessing the Descriptor Properties
- [bLength](iousbbosdescriptor/blength.md)
  The size of the descriptor in bytes.
- [bDescriptorType](iousbbosdescriptor/bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](iousbbosdescriptor/wtotallength.md)
  The length, in bytes, of the descriptor and all of its subdescriptors.
- [bNumDeviceCaps](iousbbosdescriptor/bnumdevicecaps.md)
  The number of separate device capability descriptors in the binary object store.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbbosdescriptor)*