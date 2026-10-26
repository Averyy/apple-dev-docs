# IOUSBDeviceCapabilityContainerID

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBDeviceCapabilityContainerID {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bDevCapabilityType;
   UInt8 bReservedID;
   UInt8 containerID[16];
};
```

#### Overview

Device Capability Container ID

## See Also

### Related Documentation
- [IOUSBDeviceCapabilityContainerID](../../kernel/iousbdevicecapabilitycontainerid.md)
  The structure for the container ID device capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbdevicecapabilitycontainerid)*