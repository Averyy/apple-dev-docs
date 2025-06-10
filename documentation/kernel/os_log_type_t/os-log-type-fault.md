# OS_LOG_TYPE_FAULT

**Framework**: Kernel  
**Kind**: econst

Fault-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Fault-level messages are intended for capturing system-level or multi-process errors only. If an activity object exists, logging at this level captures information for the entire process chain. Logging a message at this level is equivalent to calling the `os_log_fault` function.

**Availability**:
- macOS 10.12+

## Declaration

```swift
OS_LOG_TYPE_FAULT
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_fault)*