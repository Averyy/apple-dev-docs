# OS_LOG_TYPE_INFO

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

The informational log level.

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
OS_LOG_TYPE_INFO
```

## Discussion

Logging a message of this type is equivalent to calling the [`os_log_info`](../os_log_info.md) function. Use this level to capture information that may be helpful, but not essential, for troubleshooting errors.

Info-level messages are initially stored in memory buffers. Without a configuration change, they are purged as memory buffers fill. They are, however, captured in the data store when faults and, optionally, errors occur. When info-level messages are added to the data store, they remain there until a storage quota is exceeded, at which point, the oldest messages are purged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_info)*