# os_signpost(_:dso:log:name:signpostID:_:_:)

**Framework**: os  
**Kind**: func

Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs.

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
func os_signpost(_ animationBegin: OSSignpostAnimationBegin, dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive, _ format: AnimationFormatString.OSLogMessage, _ arguments: any CVarArg...)
```

## Parameters

- `animationBegin`: The type of animation signpost to create.
- `log`: The log object to write the signpost to.
- `name`: The name of the signpost.
- `signpostID`: A signpost identifier you use to disambiguate between signposts with the same name. If you specify   or   for this parameter, this method does nothing.
- `format`: A constant string or format string that produces a human-readable log message.
- `arguments`: Additional arguments to substitute into the   string parameter. Pass the expected number of arguments in the order that they appear in the string. If   is a constant string, don’t include any additional arguments.

## See Also

- [func os_signpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID)](os_signpost(_:dso:log:name:signpostid:)-2oz8u.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [func os_signpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, any CVarArg...)](os_signpost(_:dso:log:name:signpostid:_:_:)-2om9b.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message.
- [struct OSSignpostType](ossignposttype.md)
  The different kinds of signpost.
- [func os_signpost(OSSignpostAnimationBegin, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID)](os_signpost(_:dso:log:name:signpostid:)-12m3v.md)
  Logs the beginning of an animation as a point-of-interest in your code, without a message.
- [enum OSSignpostAnimationBegin](ossignpostanimationbegin.md)
  The signpost options to use when measuring animations.
- [enum AnimationFormatString](animationformatstring.md)
  A namespace for utilities specific to animation-related signposts.
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:_:_:)-nez5)*