# IOCoreAnalyticsSendEventProc

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 12.0+

## Declaration

```c
typedef kern_return_t (*IOCoreAnalyticsSendEventProc)(uint64_t options, OSString *eventName, OSDictionary *eventPayload);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocoreanalyticssendeventproc)*