# FCPXTimeline

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

An interface that has methods and properties to communicate and interact with the Final Cut Pro timeline.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
class FCPXTimeline
```

```objc
@interface FCPXTimeline : NSObject
```

#### Overview

For certain workflows, you will want to observe changes to the Final Cut Pro timeline and reflect those changes in the extension interface. Workflow extensions can use methods in this class to observe for state changes in the Final Cut Pro timeline. See [`add(_:)`](./fcpxtimeline/add%28_%29.md)/[`remove(_:)`](./fcpxtimeline/remove%28_%29.md) for details.

You can use the properties of this object to access certain aspects of the Final Cut Pro timeline, such as an active sequence, playhead time, or current sequence range.

> **Note**:  Workflow extensions should register an observer that conforms to the [`FCPXTimelineObserver`](./fcpxtimelineobserver.md) protocol to find out when to fetch an up-to-date timeline property value. Doing so before Final Cut Pro invokes the observer may cause the property to return `nil`.

## Topics

### Fetching Details of an Active Sequence
- [var activeSequence: FCPXSequence?](./fcpxtimeline/activesequence.md)
  The sequence played in the Final Cut Pro timeline.
- [var sequenceTimeRange: CMTimeRange](./fcpxtimeline/sequencetimerange.md)
  The time range of an active sequence in the Final Cut Pro timeline.
### Observing the Final Cut Pro Timeline
- [func add(any FCPXTimelineObserver)](./fcpxtimeline/add%28_%29.md)
  Registers a workflow extension object as an observer for Final Cut Pro timeline changes.
- [func movePlayhead(to: CMTime) -> CMTime](./fcpxtimeline/moveplayhead%28to%29.md)
  Sets the Final Cut Pro timeline playhead to a specified time.
- [func playheadTime() -> CMTime](./fcpxtimeline/playheadtime%28%29.md)
  Returns the current playhead position in the Final Cut Pro timeline.
- [func remove(any FCPXTimelineObserver)](./fcpxtimeline/remove%28_%29.md)
  Stops an observer object from receiving notifications for changes in the Final Cut Pro timeline.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### FCPX Interactions
- [Interacting with the Final Cut Pro Timeline](../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)
  Extend your workflows beyond media exchange by enabling a workflow extension to interact with the Final Cut Pro timeline.
- [protocol FCPXHost](./fcpxhost.md)
  A protocol that provides an interface to retrieve the Final Cut Pro timeline proxy objects and details of the host app.
- [func ProExtensionHostSingleton() -> (any NSObjectProtocol)?](./proextensionhostsingleton%28%29.md)
  Returns the singleton proxy instance of the host object.
- [protocol FCPXTimelineObserver](./fcpxtimelineobserver.md)
  An interface with optional methods implemented by observers of [`FCPXTimeline`](./fcpxtimeline.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimeline)*