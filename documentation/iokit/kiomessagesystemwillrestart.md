# kIOMessageSystemWillRestart

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```c
#define kIOMessageSystemWillRestart
```

## Discussion

Indicates an imminent system restart. Recipients have a limited amount of time to respond, otherwise the system will timeout and restart even without a response. Delivered to in-kernel IOKit drivers via `IOService::systemWillShutdown()`, and to clients of `registerPrioritySleepWakeInterest()`. Never delivered to user space notification clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagesystemwillrestart)*