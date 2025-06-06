# os_log_type_t

**Framework**: Kernel  
**Kind**: enum

**Availability**:
- macOS 10.12+

## Declaration

```swift
typedef enum os_log_type_t : uint8_t {
    ...
} os_log_type_t;
```

## Topics

### Constants
- [OS_LOG_TYPE_DEBUG](os_log_type_t/os_log_type_debug.md)
  Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting. Messages logged at this level contain information that may be useful during development or while troubleshooting a specific problem. Debug logging is intended for use in a development environment and not in shipping software. Logging a message of this type is equivalent to calling the `os_log_debug` function.
- [OS_LOG_TYPE_DEFAULT](os_log_type_t/os_log_type_default.md)
  Default-level messages are initially stored in memory buffers. Without a configuration change, they are compressed and moved to the data store as memory buffers fill. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information about things that  result a failure. Logging a message of this type is equivalent to calling the `os_log` function.
- [OS_LOG_TYPE_ERROR](os_log_type_t/os_log_type_error.md)
  Error-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Error-level messages are intended for reporting process-level errors. If an activity object exists, logging at this level captures information for the entire process chain. Logging a message of this type is equivalent to calling the `os_log_error` function.
- [OS_LOG_TYPE_FAULT](os_log_type_t/os_log_type_fault.md)
  Fault-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Fault-level messages are intended for capturing system-level or multi-process errors only. If an activity object exists, logging at this level captures information for the entire process chain. Logging a message at this level is equivalent to calling the `os_log_fault` function.
- [OS_LOG_TYPE_INFO](os_log_type_t/os_log_type_info.md)
  Info-level messages are initially stored in memory buffers. Without a configuration change, they are not moved to the data store and are purged as memory buffers fill. They are, however, captured in the data store when faults and, optionally, errors occur. When info-level messages are added to the data store, they remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information that may be helpful, but isn’t essential, for troubleshooting errors. Logging a message of this type is equivalent to calling the `os_log_info` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_log_type_t)*