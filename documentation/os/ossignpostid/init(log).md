# init(log:)

**Framework**: os  
**Kind**: init  
**Role**: Initializer

Creates a signpost ID for the specified log.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS
- watchOS 5.0+

> **Deprecated**: Use [`makeSignpostID()`](../ossignposter/makesignpostid%28%29.md) instead.

## Declaration

```swift
init(log: OSLog)
```

## Parameters

- `log`: The log that you’re writing signposted events to.

## See Also

### Creating a Signpost Identifier
- [init(UInt64)](./init%28_%29.md)
  Creates a signpost ID from an arbitrary 64-bit integer value.
- [init(log: OSLog, object: AnyObject)](./init%28log,object%29.md)
  Creates a signpost ID and associates it with the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostid/init(log:))*