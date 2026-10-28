# os_log_info_enabled

**Framework**: os  
**Kind**: macro  
**Role**: Macro

Returns a Boolean value that indicates whether info-level logging is in an enabled state for a specified log object.

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
#define os_log_info_enabled(log)
```

## Return Value

[`true`](../Swift/true.md) if info-level logging is in an enabled state; otherwise, [`false`](../Swift/false.md).

## Parameters

- `log`: The [`OS_LOG_DEFAULT`](./os_log_default.md) constant or a custom log object that you create with the [`os_log_create`](./os_log_create.md) function.

## See Also

### Related Documentation
- [OS_LOG_TYPE_INFO](../kernel/os_log_type_t/os_log_type_info.md)
  Info-level messages are initially stored in memory buffers. Without a configuration change, they are not moved to the data store and are purged as memory buffers fill. They are, however, captured in the data store when faults and, optionally, errors occur. When info-level messages are added to the data store, they remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information that may be helpful, but isn't essential, for troubleshooting errors. Logging a message of this type is equivalent to calling the  function.
### Getting Log Configuration
- [os_log_debug_enabled](./os_log_debug_enabled.md)
  Returns a Boolean value that indicates whether debug-level logging is in an enabled state for a specified log object.
- [func isEnabled(type: OSLogType) -> Bool](./oslog/isenabled%28type%29.md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [os_signpost_enabled](./os_signpost_enabled.md)
  Returns a Boolean value that indicates whether signposts are in an enabled state for the specified log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_info_enabled)*