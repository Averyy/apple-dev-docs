# kIOUSB30LinkStatePollingDeadline

**Framework**: Kernel  
**Kind**: econst

The polling deadline.

**Availability**:
- macOS 10.15+

## Declaration

```swift
kIOUSB30LinkStatePollingDeadline = (kIOUSB30LinkStatePollingLFPSTimeout + 1 + kIOUSB30LinkStatePollingActiveTimeout + kIOUSB30LinkStatePollingConfigurationTimeout + kIOUSB30LinkStatePollingIdleTimeout)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/tiousb30linkstatetimeout/kiousb30linkstatepollingdeadline)*