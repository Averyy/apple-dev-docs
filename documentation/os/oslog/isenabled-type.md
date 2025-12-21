# isEnabled(type:)

**Framework**: os  
**Kind**: method

Returns a Boolean value that indicates whether the log can write messages with the specified log type.

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
func isEnabled(type: OSLogType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if logging at the specified level is in an enabled state; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `type`: A log type constant, such as  ,  ,  ,  , or  , that specifies the level of logging to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/isenabled(type:))*