# os_signpost_enabled

**Framework**: os  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether signposts are in an enabled state for the specified log.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
extern bool os_signpost_enabled(os_log_t log);
```

## Parameters

- `log`: The [`OS_LOG_DEFAULT`](./os_log_default.md) constant or a custom log object that you create with the [`os_log_create`](./os_log_create.md) function.

## See Also

### Getting Log Configuration
- [os_log_info_enabled](./os_log_info_enabled.md)
  Returns a Boolean value that indicates whether info-level logging is in an enabled state for a specified log object.
- [os_log_debug_enabled](./os_log_debug_enabled.md)
  Returns a Boolean value that indicates whether debug-level logging is in an enabled state for a specified log object.
- [func isEnabled(type: OSLogType) -> Bool](./oslog/isenabled%28type%29.md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost_enabled)*