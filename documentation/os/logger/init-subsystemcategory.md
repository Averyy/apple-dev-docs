# init(subsystem:category:)

**Framework**: os  
**Kind**: init

Creates a logger using the specified subsystem and category.

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
init(subsystem: String, category: String)
```

## Parameters

- `subsystem`: The string that identifies the subsystem that emits signposts. Typically, you use the same value as your app’s  . For more information, see  .
- `category`: The string that the system uses to categorize emitted signposts.

## See Also

- [init()](logger/init.md)
  Creates a logger that writes to the default subsystem.
- [init(OSLog)](logger/init(_:).md)
  Creates a logger that writes to the specified log.
- [class OSLog](oslog.md)
  A container of related log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/init(subsystem:category:))*