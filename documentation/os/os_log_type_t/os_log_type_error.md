# OS_LOG_TYPE_ERROR

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

The error log level.

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
OS_LOG_TYPE_ERROR
```

#### Discussion

Logging a message of this type is equivalent to calling the [`os_log_error`](../os_log_error.md) function. Use this log level to report process-level errors.

Error-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. If an activity object exists, logging at this level captures information for the entire process chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_error)*