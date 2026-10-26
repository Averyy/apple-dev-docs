# FCPXHost

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that provides an interface to retrieve the Final Cut Pro timeline proxy objects and details of the host app.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
protocol FCPXHost : NSObjectProtocol
```

```objc
@protocol FCPXHost <NSObject>
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](https://developer.apple.com/documentation/professional-video-applications/interacting-with-the-final-cut-pro-timeline)

#### Overview

Workflow extensions can use the [`timeline`](./fcpxhost/timeline.md) property of this protocol as a starting point for communicating with the Final Cut Pro timeline.

## Topics

### Getting the Host Object Details
- [var bundleIdentifier: String](./fcpxhost/bundleidentifier.md)
  A unique string that identifies a host app to the system.
- [var name: String](./fcpxhost/name.md)
  The name of the host app.
- [var timeline: FCPXTimeline?](./fcpxhost/timeline.md)
  A pointer to the Final Cut Pro timeline proxy object.
- [var versionString: String](./fcpxhost/versionstring.md)
  The version number of the host app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### FCPX Interactions
- [Interacting with the Final Cut Pro Timeline](https://developer.apple.com/documentation/professional-video-applications/interacting-with-the-final-cut-pro-timeline)
  Extend your workflows beyond media exchange by enabling a workflow extension to interact with the Final Cut Pro timeline.
- [func ProExtensionHostSingleton() -> (any NSObjectProtocol)?](./proextensionhostsingleton%28%29.md)
  Returns the singleton proxy instance of the host object.
- [class FCPXTimeline](./fcpxtimeline.md)
  An interface that has methods and properties to communicate and interact with the Final Cut Pro timeline.
- [protocol FCPXTimelineObserver](./fcpxtimelineobserver.md)
  An interface with optional methods implemented by observers of [`FCPXTimeline`](./fcpxtimeline.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxhost)*