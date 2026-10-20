# kIOUSB30LinkStateRecoveryDeadline

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 12.0+

## Declaration

```c
kIOUSB30LinkStateRecoveryDeadline = (kIOUSB30LinkStateRecoveryActiveTimeout + kIOUSB30LinkStateRecoveryConfigurationTimeout + kIOUSB30LinkStateRecoveryIdleTimeout + 1 /* margin */)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/tiousb30linkstatetimeout/kiousb30linkstaterecoverydeadline)*