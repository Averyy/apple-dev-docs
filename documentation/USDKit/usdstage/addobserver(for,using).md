# addObserver(for:using:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Registers an observer that runs when a notice of the given type is sent for this stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func addObserver<Notice>(for noticeType: Notice.Type, using observer: @escaping (Notice) -> Void) -> USDStage.ObservationToken where Notice : USDStage.Notice
```

#### Discussion

Observation continues while the returned token is retained, and ends when the token is released.

## See Also

### Observing changes
- [USDStage.Notice](./notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObjectsDidChange](./objectsdidchange.md)
  A notice sent when the objects on a stage change.
- [USDStage.ObservationToken](./observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/addobserver(for:using:))*