# init(_:)

**Framework**: os  
**Kind**: init  
**Role**: Initializer

Creates a logger that writes to the specified log.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
init(_ logObj: OSLog)
```

## Parameters

- `logObj`: The log to write messages to.

## See Also

### Creating a Logger
- [init()](./init%28%29.md)
  Creates a logger that writes to the default subsystem.
- [init(subsystem: String, category: String)](./init%28subsystem,category%29.md)
  Creates a logger using the specified subsystem and category.
- [class OSLog](../oslog.md)
  A container of related log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/init(_:))*