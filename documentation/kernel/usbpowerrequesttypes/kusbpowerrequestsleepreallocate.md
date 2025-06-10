# kUSBPowerRequestSleepReallocate

**Framework**: Kernel  
**Kind**: econst

The system requests power reallocation upon sleeping.

**Availability**:
- macOS 10.7+

## Declaration

```swift
kUSBPowerRequestSleepReallocate = 5
```

#### Discussion

When you use this enumeration with [`ReturnExtraPower`](https://developer.apple.com/documentation/iokit/iousbdeviceinterface942/2977171-returnextrapower), it sends a message to all devices to return more sleep power because some devices have released it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerrequestsleepreallocate)*