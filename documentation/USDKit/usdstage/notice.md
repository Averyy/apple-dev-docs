# USDStage.Notice

**Framework**: USDKit  
**Kind**: protocol

A change notification that can be observed on a stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Notice
```

## Topics

### Instance Properties
- [var stage: USDStage](usdstage/notice/stage.md)
  The stage associated with this notice.

## Relationships

### Conforming Types
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)

## See Also

- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](usdstage/addobserver(for:using:).md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)
  A notice sent when the objects on a stage change.
- [USDStage.ObservationToken](usdstage/observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/notice)*