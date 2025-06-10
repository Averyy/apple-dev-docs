# kIOPMRootDomainState

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIOPMRootDomainState = 0x00000200
```

#### Discussion

An indication that the power flags represent the state of the root power domain. This bit must not be set in the IOPMPowerState structure. Power Management may pass this bit to initialPowerStateForDomainState() or powerStateForDomainState() to map from a global system state to the desired device state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645009-anonymous/kiopmrootdomainstate)*