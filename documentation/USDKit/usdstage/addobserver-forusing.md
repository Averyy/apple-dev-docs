# addObserver(for:using:)

**Framework**: USDKit  
**Kind**: method

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

## See Also

- [USDStage.Notice](usdstage/notice.md)
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)
- [USDStage.ObservationToken](usdstage/observationtoken.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/addobserver(for:using:))*