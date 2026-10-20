# USDStage.Notice

**Framework**: USDKit  
**Kind**: protocol  
**Role**: Protocol

A change notification that can be observed on a stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol Notice
```

## Topics

### Instance Properties
- [var stage: USDStage](./notice/stage.md)
  The stage associated with this notice.

## Relationships

### Conforming Types
- [USDStage.ObjectsDidChange](./objectsdidchange.md)

## See Also

### Observing changes
- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](./addobserver%28for,using%29.md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.ObjectsDidChange](./objectsdidchange.md)
  A notice sent when the objects on a stage change.
- [USDStage.ObservationToken](./observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/notice)*