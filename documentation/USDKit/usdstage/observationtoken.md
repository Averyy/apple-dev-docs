# USDStage.ObservationToken

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A token that keeps an observer registered for as long as it is retained.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ObservationToken
```

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing changes
- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](./addobserver%28for,using%29.md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.Notice](./notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObjectsDidChange](./objectsdidchange.md)
  A notice sent when the objects on a stage change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/observationtoken)*