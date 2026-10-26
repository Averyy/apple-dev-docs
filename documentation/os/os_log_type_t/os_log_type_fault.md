# OS_LOG_TYPE_FAULT

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

The fault log level.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
OS_LOG_TYPE_FAULT
```

#### Discussion

Logging a message at this level is equivalent to calling the [`os_log_fault`](../os_log_fault.md) function. Use this level only to capture system-level or multi-process information when reporting system errors.

Fault-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. If an activity object exists, logging at this level captures information for the entire process chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_fault)*