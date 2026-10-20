# kUSBPowerDuringWakeRevocable

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

The system requests power reallocation as revocable.

**Availability**:
- macOS 10.8+

## Declaration

```c
kUSBPowerDuringWakeRevocable = 6
```

#### Discussion

The system uses this extra power while it’s awake, but the [`kUSBPowerRequestWakeRelease`](./kusbpowerrequestwakerelease.md) message can take that power away and reallocate it to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerduringwakerevocable)*