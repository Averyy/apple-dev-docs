# OSSignpostAnimationBegin

**Framework**: os  
**Kind**: enum  
**Role**: Enumeration

The signpost options to use when measuring animations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use [`OSSignposter`](./ossignposter.md) instead.

## Declaration

```swift
enum OSSignpostAnimationBegin
```

## Topics

### Getting the Animation Options
- [OSSignpostAnimationBegin.animationBegin](./ossignpostanimationbegin/animationbegin.md)
  A signpost that marks the start of an animation.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

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
- [enum AnimationFormatString](./animationformatstring.md)
  A namespace for utilities specific to animation-related signposts.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostanimationbegin)*