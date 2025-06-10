# kIOUSB30LinkStateSSResumeDeadline

**Framework**: Kernel  
**Kind**: econst

The SuperSpeed resume deadline.

**Availability**:
- macOS 10.15+

## Declaration

```swift
kIOUSB30LinkStateSSResumeDeadline = (kIOUSB30LinkStateU3WakeupRetryDelay /* accomodation for retimer */ + kIOUSB30LinkStateU3NoLFPSResponseTimeout + kIOUSB30LinkStateRecoveryActiveTimeout + kIOUSB30LinkStateRecoveryConfigurationTimeout + kIOUSB30LinkStateRecoveryIdleTimeout)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/tiousb30linkstatetimeout/kiousb30linkstatessresumedeadline)*