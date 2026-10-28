# kUSBPowerDuringWakeRevocable

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
kUSBPowerDuringWakeRevocable = 6
```

## Discussion

The power is to be used while the system is awake (i.e not sleeping), but can be taken away (via the kUSBPowerRequestWakeRelease message). The system can then allocate that extra power to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes/kusbpowerduringwakerevocable)*