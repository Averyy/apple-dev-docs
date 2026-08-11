# addObserver(for:using:)

**Framework**: USDKit  
**Kind**: method

Registers an observer that runs when a notice of the given type is sent for this stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func addObserver<Notice>(for noticeType: Notice.Type, using observer: @escaping (Notice) -> Void) -> USDStage.ObservationToken where Notice : USDStage.Notice
```

#### Discussion

Observation continues while the returned token is retained, and ends when the token is released.

## See Also

- [USDStage.Notice](usdstage/notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)
  A notice sent when the objects on a stage change.
- [USDStage.ObservationToken](usdstage/observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/addobserver(for:using:))*