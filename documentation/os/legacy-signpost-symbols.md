# Legacy Signpost Symbols

**Framework**: os

Migrate your code away from using these legacy symbols.

## Topics

### Measure Events
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
- [enum AnimationFormatString](animationformatstring.md)
  A namespace for utilities specific to animation-related signposts.
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.

## See Also

- [Recording Performance Data](recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [struct OSSignposter](ossignposter.md)
  An object for measuring task performance using the unified logging system.
- [struct OSSignpostType](ossignposttype.md)
  The different kinds of signpost.
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/legacy-signpost-symbols)*