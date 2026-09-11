# init(allowsHitTesting:)

**Framework**: USDKit  
**Kind**: init

Creates a USDStageComponent in manual mode.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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