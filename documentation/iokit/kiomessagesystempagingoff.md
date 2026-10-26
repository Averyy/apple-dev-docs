# kIOMessageSystemPagingOff

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```c
#define kIOMessageSystemPagingOff
```

#### Discussion

Indicates an imminent system shutdown, paging device now unavailable. Recipients have a limited amount of time to respond, otherwise the system will timeout and shutdown even without a response. Delivered to clients of `registerPrioritySleepWakeInterest()`. Never delivered to user space notification clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagesystempagingoff)*