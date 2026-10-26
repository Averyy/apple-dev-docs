# kIOPSPowerSourceIDKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFNumber key uniquely identifying a UPS attached to the system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPSPowerSourceIDKey
```

#### Discussion

- Apple UPS power sources will publish this key.
- Callers should not set this key; macOS power management will publish this key for UPS's.
- Type CFNumber, kCFNumberIntType, uniquely identifying an attached UPS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopspowersourceidkey)*