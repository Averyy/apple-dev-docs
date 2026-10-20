# init(logger:)

**Framework**: os  
**Kind**: init  
**Role**: Initializer

Creates a signposter that uses the subsystem and category of an existing logger.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
init(logger: Logger)
```

## Parameters

- `logger`: The logger that provides a subsystem and category for the signposter to use. For more information, see [`Logger`](../logger.md).

## See Also

### Creating a Signposter
- [init()](./init%28%29.md)
  Creates a signposter that uses the default subsystem.
- [init(subsystem: String, category: String)](./init%28subsystem,category%29-94xpb.md)
  Creates a signposter that uses the specified subsystem and category.
- [init(subsystem: String, category: OSLog.Category)](./init%28subsystem,category%29-4vdri.md)
  Creates a signposter that uses the specified subsystem and system-defined log category.
- [init(logHandle: OSLog)](./init%28loghandle%29.md)
  Creates a signposter that uses the subsystem and category of an existing log.
- [static var disabled: OSSignposter](./disabled.md)
  A shared signposter that doesn’t emit signposts at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/init(logger:))*