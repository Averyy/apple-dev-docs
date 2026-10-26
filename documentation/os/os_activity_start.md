# os_activity_start

**Framework**: os  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`os_activity_create`](./os_activity_create.md) and [`os_activity_apply`](./os_activity_apply.md) instead.

## Declaration

```c
#define os_activity_start(description, flags)
```

## See Also

### Deprecated Macros
- [os_activity_set_breadcrumb](./os_activity_set_breadcrumb.md)
  Flags the current activity as a breadcrumb, to signify an interesting event.
- [var OS_TRACE_TYPE_DEBUG: UInt32](./os_trace_type_debug.md)
  Trace messages that occur when a debugger is attached.
- [var OS_TRACE_TYPE_INFO: UInt32](./os_trace_type_info.md)
  Trace messages that occur when a debugger is attached and additional info is requested.
- [var OS_TRACE_TYPE_RELEASE: UInt32](./os_trace_type_release.md)
  Trace messages to be captured on your app when instealled on a user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_start)*