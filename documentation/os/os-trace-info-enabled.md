# os_trace_info_enabled()

**Framework**: os  
**Kind**: func

Returns whether info level trace information is enabled.

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
func os_trace_info_enabled() -> Bool
```

#### Discussion

Generally, trace points should not involve expensive operations, however some circumstances warrant it. Use this function to do expensive work only when info level trace messages are enabled.

## See Also

- [func os_trace_debug_enabled() -> Bool](os_trace_debug_enabled().md)
  Returns whether debug level trace information is enabled.
- [func os_trace_type_enabled(UInt8) -> Bool](os_trace_type_enabled(_:).md)
  Returns whether the specified info level trace information is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_trace_info_enabled())*