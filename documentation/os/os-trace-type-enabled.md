# os_trace_type_enabled(_:)

**Framework**: os  
**Kind**: func

Returns whether the specified info level trace information is enabled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func os_trace_type_enabled(_ type: UInt8) -> Bool
```

#### Discussion

Generally, trace points should not involve expensive operations, however some circumstances warrant it. Use this function to do expensive work only when a given level of trace messages are enabled.

## Parameters

- `type`: The type of trace to check. Possible values are   and  .

## See Also

- [func os_trace_debug_enabled() -> Bool](os_trace_debug_enabled().md)
  Returns whether debug level trace information is enabled.
- [func os_trace_info_enabled() -> Bool](os_trace_info_enabled().md)
  Returns whether info level trace information is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_trace_type_enabled(_:))*