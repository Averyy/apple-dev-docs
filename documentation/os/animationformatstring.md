# AnimationFormatString

**Framework**: os  
**Kind**: enum

A namespace for utilities specific to animation-related signposts.

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
enum AnimationFormatString
```

## Topics

### Getting an Animation-Related Log Message
- [AnimationFormatString.OSLogMessage](animationformatstring/oslogmessage.md)
  A log message that includes an animation tag.

## See Also

- [func os_signpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID)](os_signpost(_:dso:log:name:signpostid:)-2oz8u.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
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
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/animationformatstring)*