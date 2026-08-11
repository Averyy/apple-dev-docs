# USDStage.ObjectsDidChange

**Framework**: USDKit  
**Kind**: struct

A notice sent when the objects on a stage change.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ObjectsDidChange
```

## Topics

### Instance Properties
- [var changedPaths: some Collection<USDLayer.Path>](usdstage/objectsdidchange/changedpaths.md)
  The paths whose fields changed.
- [var resyncedPaths: some Collection<USDLayer.Path>](usdstage/objectsdidchange/resyncedpaths.md)
  The paths whose composed content was resynchronized.
- [var stage: USDStage](usdstage/objectsdidchange/stage.md)
  The stage associated with this notice.

## Relationships

### Conforms To
- [USDStage.Notice](usdstage/notice.md)

## See Also

- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](usdstage/addobserver(for:using:).md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.Notice](usdstage/notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObservationToken](usdstage/observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/objectsdidchange)*