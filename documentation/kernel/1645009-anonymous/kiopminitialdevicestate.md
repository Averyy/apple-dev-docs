# kIOPMInitialDeviceState

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIOPMInitialDeviceState = 0x00000100
```

#### Discussion

Indicates the initial power state for the device. If `initialPowerStateForDomainState()` returns a power state with this flag set in the capability field, then the initial power change is performed without calling the driver's `setPowerState()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645009-anonymous/kiopminitialdevicestate)*