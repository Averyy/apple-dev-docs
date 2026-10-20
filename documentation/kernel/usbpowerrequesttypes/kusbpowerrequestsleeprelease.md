# kUSBPowerRequestSleepRelease

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

The system requests a release of power upon sleeping.

**Availability**:
- macOS 10.7+

## Declaration

```c
kUSBPowerRequestSleepRelease = 3
```

#### Discussion

When you use this enumeration with [`ReturnExtraPower`](../../iokit/iousbdeviceinterface942/api-2977171-returnextrapower.md), it sends a message to all devices to return any sleep power, if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerrequestsleeprelease)*