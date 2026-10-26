# os_activity_set_breadcrumb

**Framework**: os  
**Kind**: macro  
**Role**: Macro

Flags the current activity as a breadcrumb, to signify an interesting event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`os_activity_label_useraction`](./os_activity_label_useraction.md) instead.

## Declaration

```c
#define os_activity_set_breadcrumb(name)
```

#### Discussion

Use breadcrumbs to track interactions that span across multiple activities. Keep in mind that not all activities are interesting events.

This function can only be called once per activity;  subsequent calls are ignored.

## Parameters

- `name`: A label that describes the breadcrumb.

## See Also

### Deprecated Macros
- [os_activity_start](./os_activity_start.md)
- [var OS_TRACE_TYPE_DEBUG: UInt32](./os_trace_type_debug.md)
  Trace messages that occur when a debugger is attached.
- [var OS_TRACE_TYPE_INFO: UInt32](./os_trace_type_info.md)
  Trace messages that occur when a debugger is attached and additional info is requested.
- [var OS_TRACE_TYPE_RELEASE: UInt32](./os_trace_type_release.md)
  Trace messages to be captured on your app when instealled on a user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_set_breadcrumb)*