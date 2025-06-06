# OSSignpostID

**Framework**: os  
**Kind**: struct

An identifier that disambiguates signposted intervals.

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
struct OSSignpostID
```

## Mentions

- [Recording Performance Data](recording-performance-data.md)

#### Overview

Multiple intervals that have matching names, subsystems, and categories, and that exist in the same scope can be in-flight simultaneously. To match a pair of interval calls, you need to identify each interval with a unique signpost identifier. Use the first strategy in the list below that matches your use case:

- If identical intervals can never overlap, use the [`exclusive`](ossignpostid/exclusive.md) signpost ID.
- If you have data that uniquely identifies each instance of the measured task, create a signpost ID using the [`init(_:)`](ossignpostid/init(_:).md) method. The value you provide must not match that of any of the system-defined signpost IDs.
- If you have an object that uniquely identifies a pair of interval calls, such as the object you’re measuring, create a signpost ID using the [`makeSignpostID(from:)`](ossignposter/makesignpostid(from:).md) method. Don’t use this method for signposts that cross process boundaries.
- Otherwise, create a signpost ID using the [`makeSignpostID()`](ossignposter/makesignpostid().md) method.

## Topics

### Getting Signpost Identifiers
- [static let exclusive: OSSignpostID](ossignpostid/exclusive.md)
  A signpost identifier that indicates no overlap among different signpost time intervals.
- [static let invalid: OSSignpostID](ossignpostid/invalid.md)
  A signpost identifier that indicates an error.
- [static let null: OSSignpostID](ossignpostid/null.md)
  A signpost identifier that indicates a disabled signpost.
### Creating a Signpost Identifier
- [init(UInt64)](ossignpostid/init(_:).md)
  Creates a signpost ID from an arbitrary 64-bit integer value.
- [init(log: OSLog)](ossignpostid/init(log:).md)
  Creates a signpost ID for the specified log.
- [init(log: OSLog, object: AnyObject)](ossignpostid/init(log:object:).md)
  Creates a signpost ID and associates it with the specified object.
### Getting an Identifier’s Raw Value
- [let rawValue: os_signpost_id_t](ossignpostid/rawvalue.md)
  The signpost ID’s raw value.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func makeSignpostID() -> OSSignpostID](ossignposter/makesignpostid.md)
  Returns an identifier that’s unique within the scope of the signposter.
- [func makeSignpostID(from: AnyObject) -> OSSignpostID](ossignposter/makesignpostid(from:).md)
  Returns an identifier that the signposter derives from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostid)*