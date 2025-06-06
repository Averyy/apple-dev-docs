# init(subsystem:category:)

**Framework**: os  
**Kind**: init

Creates a signposter that uses the specified subsystem and system-defined log category.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
init(subsystem: String, category: OSLog.Category)
```

## Parameters

- `subsystem`: The string that identifies the subsystem that emits signposts. Typically, you use the same value as your app’s  . For more information, see  .
- `category`: The system-defined category, which the system uses to categorize emitted signposts. For possible values, see  .

## See Also

- [init()](ossignposter/init.md)
  Creates a signposter that uses the default subsystem.
- [init(subsystem: String, category: String)](ossignposter/init(subsystem:category:)-94xpb.md)
  Creates a signposter that uses the specified subsystem and category.
- [init(logger: Logger)](ossignposter/init(logger:).md)
  Creates a signposter that uses the subsystem and category of an existing logger.
- [init(logHandle: OSLog)](ossignposter/init(loghandle:).md)
  Creates a signposter that uses the subsystem and category of an existing log.
- [static var disabled: OSSignposter](ossignposter/disabled.md)
  A shared signposter that doesn’t emit signposts at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/init(subsystem:category:)-4vdri)*