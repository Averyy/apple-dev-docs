# init(_:)

**Framework**: os  
**Kind**: init

Creates a logger that writes to the specified log.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
init(_ logObj: OSLog)
```

## Parameters

- `logObj`: The log to write messages to.

## See Also

- [init()](logger/init.md)
  Creates a logger that writes to the default subsystem.
- [init(subsystem: String, category: String)](logger/init(subsystem:category:).md)
  Creates a logger using the specified subsystem and category.
- [class OSLog](oslog.md)
  A container of related log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/init(_:))*