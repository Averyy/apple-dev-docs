# OS_LOG_TYPE_DEFAULT

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

The default log level.

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
OS_LOG_TYPE_DEFAULT
```

## Discussion

Logging a message of this type is equivalent to calling the [`os_log`](../os_log.md) function. Use this level to capture information about things that might result in a failure.

Default-level messages are initially stored in memory buffers. Without a configuration change, they are compressed and moved to the data store as memory buffers fill. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_default)*