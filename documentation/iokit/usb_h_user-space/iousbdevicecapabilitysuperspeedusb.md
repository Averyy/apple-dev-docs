# IOUSBDeviceCapabilitySuperSpeedUSB

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBDeviceCapabilitySuperSpeedUSB {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bDevCapabilityType;
   UInt8 bmAttributes;
   UInt16 wSpeedsSupported;
   UInt8 bFunctionalitySupport;
   UInt8 bU1DevExitLat;
   UInt16 wU2DevExitLat;
};
```

## Overview

Device Capability SuperSpeed USB

## See Also

### Related Documentation
- [IOUSBDeviceCapabilitySuperSpeedUSB](../../kernel/iousbdevicecapabilitysuperspeedusb.md)
  The structure for the SuperSpeed USB device capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbdevicecapabilitysuperspeedusb)*