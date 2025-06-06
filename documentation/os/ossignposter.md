# OSSignposter

**Framework**: os  
**Kind**: struct

An object for measuring task performance using the unified logging system.

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
struct OSSignposter
```

## Mentions

- [Recording Performance Data](recording-performance-data.md)

#### Overview

Signposts allow you to record meaningful information about the duration of your app’s tasks using the same subsystems and categories that you use for logging. Use `OSSignposter` to create signposted intervals in your code, and then use Instruments’ `os_signposts` instrument to record those intervals as you run your app and perform the actions to measure. Instruments displays signpost data visually in a timeline.

![An image that shows several signposted intervals on a timeline in Instruments. The first interval has a highlight and displays the OS signpost icon at its start and end. The icons represent the calls in code that begin and end the signposted interval.](https://docs-assets.developer.apple.com/published/79b69e2516a36b5482a43e514c95a48b/media-3855979%402x.png)

To add a signposted interval, create a signpost ID — an identifier that disambiguates intervals that have the same name, subsystem, and category, and that exist within the same scope — and then add a call to one of the class’s `beginInterval` methods just before the code you want to measure. Retain the interval state it returns, and end the interval by passing that state to one of the class’s `endInterval` methods, which you call immediately after the measured code. A signposter uses interval state to enforce a number of runtime assertions, the behavior of which depends on your app’s build configuration. For more information, see [`OSSignpostIntervalState`](ossignpostintervalstate.md). A signposted interval consists of one begin call and one end call only.

`OSSignposter` also provides functionality to signpost a closure, and to emit individual signposts that don’t have a duration that you can use to highlight points of interest, such as when the user taps a button or performs a specific gesture.

## Topics

### Creating a Signposter
- [init()](ossignposter/init.md)
  Creates a signposter that uses the default subsystem.
- [init(subsystem: String, category: String)](ossignposter/init(subsystem:category:)-94xpb.md)
  Creates a signposter that uses the specified subsystem and category.
- [init(subsystem: String, category: OSLog.Category)](ossignposter/init(subsystem:category:)-4vdri.md)
  Creates a signposter that uses the specified subsystem and system-defined log category.
- [init(logger: Logger)](ossignposter/init(logger:).md)
  Creates a signposter that uses the subsystem and category of an existing logger.
- [init(logHandle: OSLog)](ossignposter/init(loghandle:).md)
  Creates a signposter that uses the subsystem and category of an existing log.
- [static var disabled: OSSignposter](ossignposter/disabled.md)
  A shared signposter that doesn’t emit signposts at runtime.
### Getting State
- [var isEnabled: Bool](ossignposter/isenabled.md)
  A Boolean value that indicates whether the signposter can emit signposts.
### Generating Signpost IDs
- [func makeSignpostID() -> OSSignpostID](ossignposter/makesignpostid.md)
  Returns an identifier that’s unique within the scope of the signposter.
- [func makeSignpostID(from: AnyObject) -> OSSignpostID](ossignposter/makesignpostid(from:).md)
  Returns an identifier that the signposter derives from the specified object.
- [struct OSSignpostID](ossignpostid.md)
  An identifier that disambiguates signposted intervals.
### Starting a Signposted Interval
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
- [typealias SignpostMetadata](signpostmetadata.md)
  The type that represents a message you attach to a signpost.
### Stopping a Signposted Interval
- [func endInterval(StaticString, OSSignpostIntervalState)](ossignposter/endinterval(_:_:).md)
  Ends the signposted interval that corresponds to the specified name and state.
- [func endInterval(StaticString, OSSignpostIntervalState, SignpostMetadata)](ossignposter/endinterval(_:_:_:).md)
  Ends a signposted interval and attaches the specified message.
### Measuring a Closure
- [func withIntervalSignpost<T>(StaticString, id: OSSignpostID, around: () throws -> T) rethrows -> T](ossignposter/withintervalsignpost(_:id:around:).md)
  Measures the execution of the specified closure.
- [func withIntervalSignpost<T>(StaticString, id: OSSignpostID, SignpostMetadata, around: () throws -> T) rethrows -> T](ossignposter/withintervalsignpost(_:id:_:around:).md)
  Measures the execution of a closure and attaches the specified message.
### Emitting Individual Signposts
- [func emitEvent(StaticString, id: OSSignpostID)](ossignposter/emitevent(_:id:).md)
  Marks a point of interest in time.
- [func emitEvent(StaticString, id: OSSignpostID, SignpostMetadata)](ossignposter/emitevent(_:id:_:).md)
  Marks a point of interest in time and attaches the specified message.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Recording Performance Data](recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [Legacy Signpost Symbols](legacy-signpost-symbols.md)
  Migrate your code away from using these legacy symbols.
- [struct OSSignpostType](ossignposttype.md)
  The different kinds of signpost.
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter)*