# kIOPMInitialDeviceState

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
kIOPMInitialDeviceState = 0x00000100
```

#### Discussion

Indicates the initial power state for the device. If `initialPowerStateForDomainState()` returns a power state with this flag set in the capability field, then the initial power change is performed without calling the driver's `setPowerState()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1499606-anonymous/kiopminitialdevicestate)*