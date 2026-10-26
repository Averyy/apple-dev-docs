# os_trace_type_enabled(_:)

**Framework**: os  
**Kind**: func  
**Role**: Function

Returns whether the specified info level trace information is enabled.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0 (renamed: OSLog.isEnabled(self:type:))
- iPadOS 8.0+ - Deprecated in 11.0 (renamed: OSLog.isEnabled(self:type:))
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: OSLog.isEnabled(self:type:))
- macOS 10.10+ - Deprecated in 10.13 (renamed: OSLog.isEnabled(self:type:))
- tvOS 8.0+ - Deprecated in 11.0 (renamed: OSLog.isEnabled(self:type:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: OSLog.isEnabled(self:type:))
- watchOS 2.0+ - Deprecated in 4.0 (renamed: OSLog.isEnabled(self:type:))

> **Deprecated**: Use [`isEnabled(type:)`](./oslog/isenabled%28type%29.md) instead.

## Declaration

```swift
func os_trace_type_enabled(_ type: UInt8) -> Bool
```

```c
static bool os_trace_type_enabled(uint8_t type);
```

#### Discussion

Generally, trace points should not involve expensive operations, however some circumstances warrant it. Use this function to do expensive work only when a given level of trace messages are enabled.

## Parameters

- `type`: The type of trace to check. Possible values are [`OS_TRACE_TYPE_DEBUG`](./os_trace_type_debug.md) and [`OS_TRACE_TYPE_INFO`](./os_trace_type_info.md).

## See Also

### Deprecated Functions
- [func os_trace_debug_enabled() -> Bool](./os_trace_debug_enabled%28%29.md)
  Returns whether debug level trace information is enabled.
- [func os_trace_info_enabled() -> Bool](./os_trace_info_enabled%28%29.md)
  Returns whether info level trace information is enabled.
- [os_log_is_enabled](./os_log_is_enabled.md)
- [os_log_is_debug_enabled](./os_log_is_debug_enabled.md)
- [os_activity_get_active](./os_activity_get_active.md)
  Returns the stack of nested activities associated with the current thread.
- [os_activity_end](./os_activity_end.md)
  Ends the specified activity on the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_trace_type_enabled(_:))*