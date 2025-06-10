# OS_LOG_TYPE_INFO

**Framework**: Kernel  
**Kind**: econst

Info-level messages are initially stored in memory buffers. Without a configuration change, they are not moved to the data store and are purged as memory buffers fill. They are, however, captured in the data store when faults and, optionally, errors occur. When info-level messages are added to the data store, they remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information that may be helpful, but isn’t essential, for troubleshooting errors. Logging a message of this type is equivalent to calling the `os_log_info` function.

**Availability**:
- macOS 10.12+

## Declaration

```swift
OS_LOG_TYPE_INFO
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_info)*