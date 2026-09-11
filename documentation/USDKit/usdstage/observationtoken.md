# USDStage.ObservationToken

**Framework**: USDKit  
**Kind**: struct

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](usdstage/addobserver(for:using:).md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.Notice](usdstage/notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)
  A notice sent when the objects on a stage change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/observationtoken)*