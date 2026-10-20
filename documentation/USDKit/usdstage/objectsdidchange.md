# USDStage.ObjectsDidChange

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A notice sent when the objects on a stage change.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ObjectsDidChange
```

## Topics

### Instance Properties
- [var changedPaths: some Collection<USDLayer.Path>](./objectsdidchange/changedpaths.md)
  The paths whose fields changed.
- [var resyncedPaths: some Collection<USDLayer.Path>](./objectsdidchange/resyncedpaths.md)
  The paths whose composed content was resynchronized.
- [var stage: USDStage](./objectsdidchange/stage.md)
  The stage associated with this notice.

## Relationships

### Conforms To
- [USDStage.Notice](./notice.md)

## See Also

### Observing changes
- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](./addobserver%28for,using%29.md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.Notice](./notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObservationToken](./observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/objectsdidchange)*