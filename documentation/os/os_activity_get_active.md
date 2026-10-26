# os_activity_get_active

**Framework**: os  
**Kind**: func  
**Role**: Function

Returns the stack of nested activities associated with the current thread.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.12
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: This function is no longer supported, and there is no replacement.

## Declaration

```c
extern unsigned int os_activity_get_active(os_activity_id_t *entries, unsigned int *count);
```

#### Return Value

The number of activities written to `entries`.

#### Discussion

Because activities can be nested, there can be more than one activity involved on the current thread.

This function should be used only by diagnostic tools for making additional determinations about a situation.

## Parameters

- `entries`: A buffer sized to hold the the number of activities being requested.
- `count`: The number of activities requested.

## See Also

### Deprecated Functions
- [os_log_is_enabled](./os_log_is_enabled.md)
- [os_log_is_debug_enabled](./os_log_is_debug_enabled.md)
- [os_activity_end](./os_activity_end.md)
  Ends the specified activity on the current thread.
- [func os_trace_debug_enabled() -> Bool](./os_trace_debug_enabled%28%29.md)
  Returns whether debug level trace information is enabled.
- [func os_trace_info_enabled() -> Bool](./os_trace_info_enabled%28%29.md)
  Returns whether info level trace information is enabled.
- [func os_trace_type_enabled(UInt8) -> Bool](./os_trace_type_enabled%28_%29.md)
  Returns whether the specified info level trace information is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_get_active)*