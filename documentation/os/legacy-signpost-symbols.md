# Legacy Signpost Symbols

**Framework**: os  
**Role**: API Collection

Migrate your code away from using these legacy symbols.

## Topics

### Measure Events
- [func os_signpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID)](./os_signpost%28_,dso,log,name,signpostid%29-2oz8u.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [func os_signpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, any CVarArg...)](./os_signpost%28_,dso,log,name,signpostid,_,_%29-2om9b.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message.
- [struct OSSignpostType](./ossignposttype.md)
  The different kinds of signpost.
- [func os_signpost(OSSignpostAnimationBegin, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID)](./os_signpost%28_,dso,log,name,signpostid%29-12m3v.md)
  Logs the beginning of an animation as a point-of-interest in your code, without a message.
- [func os_signpost(OSSignpostAnimationBegin, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, AnimationFormatString.OSLogMessage, any CVarArg...)](./os_signpost%28_,dso,log,name,signpostid,_,_%29-nez5.md)
  Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs.
- [enum OSSignpostAnimationBegin](./ossignpostanimationbegin.md)
  The signpost options to use when measuring animations.
- [enum AnimationFormatString](./animationformatstring.md)
  A namespace for utilities specific to animation-related signposts.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.

## See Also

### Measure Events
- [Recording Performance Data](./recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [struct OSSignposter](./ossignposter.md)
  An object for measuring task performance using the unified logging system.
- [struct OSSignpostType](./ossignposttype.md)
  The different kinds of signpost.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.
- [os_signpost_emit_with_type](./os_signpost_emit_with_type.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [os_signpost_interval_begin](./os_signpost_interval_begin.md)
  Marks the start of a time interval in your code using a signpost.
- [os_signpost_interval_end](./os_signpost_interval_end.md)
  Marks the end of a time interval in your code using a signpost.
- [os_signpost_event_emit](./os_signpost_event_emit.md)
  Marks a point of interest in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/legacy-signpost-symbols)*