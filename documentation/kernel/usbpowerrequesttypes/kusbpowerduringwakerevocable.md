# kUSBPowerDuringWakeRevocable

**Framework**: Kernel  
**Kind**: econst

The system requests power reallocation as revocable.

**Availability**:
- macOS 10.8+

## Declaration

```swift
kUSBPowerDuringWakeRevocable = 6
```

#### Discussion

The system uses this extra power while it’s awake, but the [`kUSBPowerRequestWakeRelease`](usbpowerrequesttypes/kusbpowerrequestwakerelease.md) message can take that power away and reallocate it to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerduringwakerevocable)*