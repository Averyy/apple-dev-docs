# FCPXTimelineObserver

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An interface with optional methods implemented by observers of [`FCPXTimeline`](./fcpxtimeline.md) objects.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
protocol FCPXTimelineObserver : NSObjectProtocol
```

```objc
@protocol FCPXTimelineObserver <NSObject>
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)

#### Overview

Observers of [`FCPXTimeline`](./fcpxtimeline.md) objects implement methods of this protocol to get notified of changes in the Final Cut Pro timeline. Based on the methods implemented in this protocol, Final Cut Pro invokes an observer for changes in an active sequence, playhead time, or sequence time range.

## Topics

### Handling Final Cut Pro Timeline Changes
- [func activeSequenceChanged()](./fcpxtimelineobserver/activesequencechanged%28%29.md)
  A callback method that gets invoked when there is a change in the current timeline sequence.
- [func playheadTimeChanged()](./fcpxtimelineobserver/playheadtimechanged%28%29.md)
  A callback method that gets invoked when the playhead position changes in the Final Cut Pro timeline.
- [func sequenceTimeRangeChanged()](./fcpxtimelineobserver/sequencetimerangechanged%28%29.md)
  A callback method that gets invoked when the time range of an active sequence changes in the Final Cut Pro timeline.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### FCPX Interactions
- [Interacting with the Final Cut Pro Timeline](../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)
  Extend your workflows beyond media exchange by enabling a workflow extension to interact with the Final Cut Pro timeline.
- [protocol FCPXHost](./fcpxhost.md)
  A protocol that provides an interface to retrieve the Final Cut Pro timeline proxy objects and details of the host app.
- [func ProExtensionHostSingleton() -> (any NSObjectProtocol)?](./proextensionhostsingleton%28%29.md)
  Returns the singleton proxy instance of the host object.
- [class FCPXTimeline](./fcpxtimeline.md)
  An interface that has methods and properties to communicate and interact with the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimelineobserver)*