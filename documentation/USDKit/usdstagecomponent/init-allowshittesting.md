# init(allowsHitTesting:)

**Framework**: USDKit  
**Kind**: init

Creates a USDStageComponent in manual mode.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
init(allowsHitTesting: Bool = true)
```

#### Discussion

In manual mode, you control when rendering occurs by calling [`render(_:to:at:)`](usdstagecomponent/render(_:to:at:).md).

## Parameters

- `allowsHitTesting`: Whether to generate collision shapes for hit testing. Defaults to `true`.

## See Also

- [init(USDStage, timeCode: USDStage.TimeCode, allowsHitTesting: Bool) async](usdstagecomponent/init(_:timecode:allowshittesting:).md)
  Creates a USDStageComponent in automatic mode and waits for the first render to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/init(allowshittesting:))*