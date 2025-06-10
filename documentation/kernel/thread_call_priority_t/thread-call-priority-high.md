# THREAD_CALL_PRIORITY_HIGH

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.8+

## Declaration

```swift
THREAD_CALL_PRIORITY_HIGH = 0
```

#### Discussion

Importance above everything but realtime. Thread calls allocated with this priority execute at extremely high priority, above everything but realtime threads. They are generally executed in serial. Though they may execute concurrently under some circumstances, no fan-out is implied. These work items should do very small amounts of work or risk disrupting system responsiveness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/thread_call_priority_t/thread_call_priority_high)*