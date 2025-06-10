# kIOPMLowPower

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIOPMLowPower = 0x00010000
```

#### Discussion

Indicates device is in a low power state. May be bitwis-OR'd together with kIOPMDeviceUsable flag, to indicate the device is still usable.

A device with a capability of kIOPMLowPower may: Require either 0 or kIOPMPowerOn from its power parent Offer either kIOPMLowPower, kIOPMPowerOn, or 0 (no power at all) to its power plane children.

Useful only as a Capability, although USB drivers should consult USB family documentation for other valid circumstances to use the kIOPMLowPower bit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645009-anonymous/kiopmlowpower)*