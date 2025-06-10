# OS_LOG_TYPE_DEFAULT

**Framework**: Kernel  
**Kind**: econst

Default-level messages are initially stored in memory buffers. Without a configuration change, they are compressed and moved to the data store as memory buffers fill. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information about things that  result a failure. Logging a message of this type is equivalent to calling the `os_log` function.

**Availability**:
- macOS 10.12+

## Declaration

```swift
OS_LOG_TYPE_DEFAULT
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_default)*