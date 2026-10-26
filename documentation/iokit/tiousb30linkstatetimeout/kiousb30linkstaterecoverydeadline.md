# kIOUSB30LinkStateRecoveryDeadline

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```c
kIOUSB30LinkStateRecoveryDeadline = (kIOUSB30LinkStateRecoveryActiveTimeout + kIOUSB30LinkStateRecoveryConfigurationTimeout + kIOUSB30LinkStateRecoveryIdleTimeout + 1 /* margin */)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/tiousb30linkstatetimeout/kiousb30linkstaterecoverydeadline)*