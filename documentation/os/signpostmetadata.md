# SignpostMetadata

**Framework**: os  
**Kind**: typealias

The type that represents a message you attach to a signpost.

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
typealias SignpostMetadata = OSLogMessage
```

## See Also

- [func beginInterval(StaticString, id: OSSignpostID) -> OSSignpostIntervalState](ossignposter/begininterval(_:id:).md)
  Begins a signposted interval.
- [func beginInterval(StaticString, id: OSSignpostID, SignpostMetadata) -> OSSignpostIntervalState](ossignposter/begininterval(_:id:_:).md)
  Begins a signposted interval and attaches the specified message.
- [func beginAnimationInterval(StaticString, id: OSSignpostID) -> OSSignpostIntervalState](ossignposter/beginanimationinterval(_:id:).md)
  Begins a signposted interval for measuring an animation.
- [func beginAnimationInterval(StaticString, id: OSSignpostID, SignpostMetadata) -> OSSignpostIntervalState](ossignposter/beginanimationinterval(_:id:_:).md)
  Begins a signposted interval for measuring an animation, and attaches a message.
- [class OSSignpostIntervalState](ossignpostintervalstate.md)
  An object that tracks the state of a signposted interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/signpostmetadata)*