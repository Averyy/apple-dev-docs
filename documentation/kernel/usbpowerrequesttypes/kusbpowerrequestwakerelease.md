# kUSBPowerRequestWakeRelease

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

The system requests a release of power upon waking.

**Availability**:
- macOS 10.7+

## Declaration

```c
kUSBPowerRequestWakeRelease = 2
```

#### Discussion

When you use this enumeration with [`ReturnExtraPower`](../../iokit/iousbdeviceinterface942/api-2977171-returnextrapower.md), it  sends a message to all devices to return any extra wake power, if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerrequestwakerelease)*