# kUSBAddExtraResetTimeBit

**Framework**: Kernel  
**Kind**: econst

Request extra time after reset.

**Availability**:
- macOS 10.3+

## Declaration

```swift
kUSBAddExtraResetTimeBit = 31
```

#### Discussion

Setting this bit causes the hub driver to wait 100 milliseconds before addressing the device after the reset following the reenumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbreenumerateoptions/kusbaddextraresettimebit)*