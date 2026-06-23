# USDStage.ObjectsDidChange

**Framework**: USDKit  
**Kind**: struct

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
- [var resyncedPaths: some Collection<USDLayer.Path>](usdstage/objectsdidchange/resyncedpaths.md)

## Relationships

### Conforms To
- [USDStage.Notice](usdstage/notice.md)

## See Also

- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](usdstage/addobserver(for:using:).md)
- [USDStage.Notice](usdstage/notice.md)
- [USDStage.ObservationToken](usdstage/observationtoken.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/objectsdidchange)*