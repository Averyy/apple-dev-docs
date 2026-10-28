# kIOPMRootDomainState

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```c
kIOPMRootDomainState = 0x00000200
```

## Discussion

An indication that the power flags represent the state of the root power domain. This bit must not be set in the IOPMPowerState structure. Power Management may pass this bit to initialPowerStateForDomainState() or powerStateForDomainState() to map from a global system state to the desired device state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1499606-anonymous/kiopmrootdomainstate)*