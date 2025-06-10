# kUSBPowerDuringWakeUSB3

**Framework**: Kernel  
**Kind**: econst

The system requests extra power allocation.

**Availability**:
- macOS 10.8+

## Declaration

```swift
kUSBPowerDuringWakeUSB3 = 7
```

#### Discussion

The USB stack uses this enumeration to allocate the 400 milliamps extra for USB 3.0 above the 500 milliamps that USB 2.0 allocates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerduringwakeusb3)*