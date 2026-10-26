# os_log_is_debug_enabled

**Framework**: os  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.12
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`os_log_debug_enabled`](./os_log_debug_enabled.md) instead.

## Declaration

```c
extern bool os_log_is_debug_enabled(os_log_t log);
```

## See Also

### Deprecated Functions
- [os_log_is_enabled](./os_log_is_enabled.md)
- [os_activity_get_active](./os_activity_get_active.md)
  Returns the stack of nested activities associated with the current thread.
- [os_activity_end](./os_activity_end.md)
  Ends the specified activity on the current thread.
- [func os_trace_debug_enabled() -> Bool](./os_trace_debug_enabled%28%29.md)
  Returns whether debug level trace information is enabled.
- [func os_trace_info_enabled() -> Bool](./os_trace_info_enabled%28%29.md)
  Returns whether info level trace information is enabled.
- [func os_trace_type_enabled(UInt8) -> Bool](./os_trace_type_enabled%28_%29.md)
  Returns whether the specified info level trace information is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_is_debug_enabled)*