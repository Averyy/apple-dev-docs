# OS_LOG_TYPE_ERROR

**Framework**: Kernel  
**Kind**: econst

Error-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Error-level messages are intended for reporting process-level errors. If an activity object exists, logging at this level captures information for the entire process chain. Logging a message of this type is equivalent to calling the `os_log_error` function.

**Availability**:
- macOS 10.12+

## Declaration

```swift
OS_LOG_TYPE_ERROR
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_error)*