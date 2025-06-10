# kUSBPowerRequestSleepRelease

**Framework**: Kernel  
**Kind**: econst

The system requests a release of power upon sleeping.

**Availability**:
- macOS 10.7+

## Declaration

```swift
kUSBPowerRequestSleepRelease = 3
```

#### Discussion

When you use this enumeration with [`ReturnExtraPower`](https://developer.apple.com/documentation/iokit/iousbdeviceinterface942/2977171-returnextrapower), it sends a message to all devices to return any sleep power, if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerrequestsleeprelease)*