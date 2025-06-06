# os_signpost(_:dso:log:name:signpostID:)

**Framework**: os  
**Kind**: func

Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.

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
func os_signpost(_ type: OSSignpostType, dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive)
```

## Parameters

- `type`: The type of signpost to create.
- `log`: A log object to write the signpost to.
- `name`: The name of the signpost.
- `signpostID`: A signpost identifier you use to disambiguate between signposts with the same name.

## See Also

- [func os_signpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, any CVarArg...)](os_signpost(_:dso:log:name:signpostid:_:_:)-2om9b.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message.
- [struct OSSignpostType](ossignposttype.md)
  The different kinds of signpost.
- [func os_signpost(OSSignpostAnimationBegin, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID)](os_signpost(_:dso:log:name:signpostid:)-12m3v.md)
  Logs the beginning of an animation as a point-of-interest in your code, without a message.
- [func os_signpost(OSSignpostAnimationBegin, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, AnimationFormatString.OSLogMessage, any CVarArg...)](os_signpost(_:dso:log:name:signpostid:_:_:)-nez5.md)
  Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs.
- [enum OSSignpostAnimationBegin](ossignpostanimationbegin.md)
  The signpost options to use when measuring animations.
- [enum AnimationFormatString](animationformatstring.md)
  A namespace for utilities specific to animation-related signposts.
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:)-2oz8u)*