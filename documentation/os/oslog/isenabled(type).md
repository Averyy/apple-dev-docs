# isEnabled(type:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the log can write messages with the specified log type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func isEnabled(type: OSLogType) -> Bool
```

```c
extern bool os_log_type_enabled(os_log_t oslog, os_log_type_t type);
```

#### Return Value

[`true`](../../Swift/true.md) if logging at the specified level is in an enabled state; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `type`: A log type constant, such as [`OS_LOG_TYPE_DEFAULT`](../os_log_type_t/os_log_type_default.md), [`OS_LOG_TYPE_INFO`](../os_log_type_t/os_log_type_info.md), [`OS_LOG_TYPE_DEBUG`](../os_log_type_t/os_log_type_debug.md), [`OS_LOG_TYPE_ERROR`](../os_log_type_t/os_log_type_error.md), or [`OS_LOG_TYPE_FAULT`](../os_log_type_t/os_log_type_fault.md), that specifies the level of logging to check.

## See Also

### Getting Log Configuration
- [os_log_info_enabled](../os_log_info_enabled.md)
  Returns a Boolean value that indicates whether info-level logging is in an enabled state for a specified log object.
- [os_log_debug_enabled](../os_log_debug_enabled.md)
  Returns a Boolean value that indicates whether debug-level logging is in an enabled state for a specified log object.
- [os_signpost_enabled](../os_signpost_enabled.md)
  Returns a Boolean value that indicates whether signposts are in an enabled state for the specified log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/isenabled(type:))*