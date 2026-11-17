# isEnabled(type:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Checks if the Logger can emit log messages for a given log type. This allows for more granular control over logging based on the log level.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
func isEnabled(type: OSLogType) -> Bool
```

## Return Value

True if logging is enabled for the specified log type, false otherwise

## Parameters

- `type`: The log type to check (e.g., .default, .info, .debug, .error, .fault)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/isenabled(type:))*