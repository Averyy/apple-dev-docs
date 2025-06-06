# init(log:)

**Framework**: os  
**Kind**: init

Creates a signpost ID for the specified log.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+
- watchOS 5.0+

## Declaration

```swift
init(log: OSLog)
```

## Parameters

- `log`: The log that you’re writing signposted events to.

## See Also

- [init(UInt64)](ossignpostid/init(_:).md)
  Creates a signpost ID from an arbitrary 64-bit integer value.
- [init(log: OSLog, object: AnyObject)](ossignpostid/init(log:object:).md)
  Creates a signpost ID and associates it with the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostid/init(log:))*