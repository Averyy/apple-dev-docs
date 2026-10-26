# Deprecated Symbols

**Framework**: os  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Deprecated Functions
- [func os_trace_debug_enabled() -> Bool](./os_trace_debug_enabled%28%29.md)
  Returns whether debug level trace information is enabled.
- [func os_trace_info_enabled() -> Bool](./os_trace_info_enabled%28%29.md)
  Returns whether info level trace information is enabled.
- [func os_trace_type_enabled(UInt8) -> Bool](./os_trace_type_enabled%28_%29.md)
  Returns whether the specified info level trace information is enabled.
- [os_log_is_enabled](./os_log_is_enabled.md)
- [os_log_is_debug_enabled](./os_log_is_debug_enabled.md)
- [os_activity_get_active](./os_activity_get_active.md)
  Returns the stack of nested activities associated with the current thread.
- [os_activity_end](./os_activity_end.md)
  Ends the specified activity on the current thread.
### Deprecated Macros
- [var OS_TRACE_TYPE_DEBUG: UInt32](./os_trace_type_debug.md)
  Trace messages that occur when a debugger is attached.
- [var OS_TRACE_TYPE_INFO: UInt32](./os_trace_type_info.md)
  Trace messages that occur when a debugger is attached and additional info is requested.
- [var OS_TRACE_TYPE_RELEASE: UInt32](./os_trace_type_release.md)
  Trace messages to be captured on your app when instealled on a user’s device.
- [os_activity_start](./os_activity_start.md)
- [os_activity_set_breadcrumb](./os_activity_set_breadcrumb.md)
  Flags the current activity as a breadcrumb, to signify an interesting event.
### Deprecated Type Aliases
- [typealias os_trace_payload_object_t](./os_trace_payload_object_t.md)
  A pointer to a trace payload object.
- [os_breadcrumb_t](./os_breadcrumb_t.md)
- [os_trace_payload_t](./os_trace_payload_t.md)
  A pointer to a trace payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/deprecated-symbols)*