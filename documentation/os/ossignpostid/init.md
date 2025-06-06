# init(_:)

**Framework**: os  
**Kind**: init

Creates a signpost ID from an arbitrary 64-bit integer value.

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
init(_ value: UInt64)
```

## Parameters

- `value`: The value to use when generating the signpost ID.

## See Also

- [init(log: OSLog)](ossignpostid/init(log:).md)
  Creates a signpost ID for the specified log.
- [init(log: OSLog, object: AnyObject)](ossignpostid/init(log:object:).md)
  Creates a signpost ID and associates it with the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostid/init(_:))*