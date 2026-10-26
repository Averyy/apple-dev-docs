# os_trace_info_enabled()

**Framework**: os  
**Kind**: func  
**Role**: Function

Returns whether info level trace information is enabled.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.13
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`os_log_info_enabled`](./os_log_info_enabled.md) instead.

## Declaration

```swift
func os_trace_info_enabled() -> Bool
```

```c
extern bool os_trace_info_enabled();
```

#### Discussion

Generally, trace points should not involve expensive operations, however some circumstances warrant it. Use this function to do expensive work only when info level trace messages are enabled.

## See Also

### Deprecated Functions
- [func os_trace_debug_enabled() -> Bool](./os_trace_debug_enabled%28%29.md)
  Returns whether debug level trace information is enabled.
- [func os_trace_type_enabled(UInt8) -> Bool](./os_trace_type_enabled%28_%29.md)
  Returns whether the specified info level trace information is enabled.
- [os_log_is_enabled](./os_log_is_enabled.md)
- [os_log_is_debug_enabled](./os_log_is_debug_enabled.md)
- [os_activity_get_active](./os_activity_get_active.md)
  Returns the stack of nested activities associated with the current thread.
- [os_activity_end](./os_activity_end.md)
  Ends the specified activity on the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_trace_info_enabled())*