# OS_TRACE_TYPE_INFO

**Framework**: os  
**Kind**: var  
**Role**: Global Variable

Trace messages that occur when a debugger is attached and additional info is requested.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use logging instead.

## Declaration

```swift
var OS_TRACE_TYPE_INFO: UInt32 { get }
```

```c
#define OS_TRACE_TYPE_INFO
```

## See Also

### Deprecated Macros
- [var OS_TRACE_TYPE_DEBUG: UInt32](./os_trace_type_debug.md)
  Trace messages that occur when a debugger is attached.
- [var OS_TRACE_TYPE_RELEASE: UInt32](./os_trace_type_release.md)
  Trace messages to be captured on your app when instealled on a user’s device.
- [os_activity_start](./os_activity_start.md)
- [os_activity_set_breadcrumb](./os_activity_set_breadcrumb.md)
  Flags the current activity as a breadcrumb, to signify an interesting event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_trace_type_info)*