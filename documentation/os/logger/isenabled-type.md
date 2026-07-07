# isEnabled(type:)

**Framework**: os  
**Kind**: method

Checks if the Logger can emit log messages for a given log type. This allows for more granular control over logging based on the log level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func isEnabled(type: OSLogType) -> Bool
```

#### Return Value

True if logging is enabled for the specified log type, false otherwise

## Parameters

- `type`: The log type to check (e.g., .default, .info, .debug, .error, .fault)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/isenabled(type:))*