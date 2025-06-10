# kIOPMPreventIdleSleep

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIOPMPreventIdleSleep = 0x00000040
```

#### Discussion

In the capability field of a power state, disallows idle system sleep while the device is in that state.

For example, displays and disks set this capability for their ON power state; since the system may not idle sleep while the display (and thus keyboard or mouse) or the disk is active.

Useful only as a Capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645009-anonymous/kiopmpreventidlesleep)*