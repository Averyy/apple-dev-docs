# kIOUSB30LinkStateSSResumeDeadline

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```c
kIOUSB30LinkStateSSResumeDeadline = (kIOUSB30LinkStateU3WakeupRetryDelay /* accomodation for retimer */ + kIOUSB30LinkStateU3NoLFPSResponseTimeout + kIOUSB30LinkStateRecoveryActiveTimeout + kIOUSB30LinkStateRecoveryConfigurationTimeout + kIOUSB30LinkStateRecoveryIdleTimeout)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/tiousb30linkstatetimeout/kiousb30linkstatessresumedeadline)*