# init(_:timeCode:allowsHitTesting:)

**Framework**: USDKit  
**Kind**: init

Creates a USDStageComponent in automatic mode and waits for the first render to complete.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
init(_ stage: USDStage, timeCode: USDStage.TimeCode = .default, allowsHitTesting: Bool = true) async
```

#### Discussion

In automatic mode, the component manages rendering internally and updates when the stage or time code changes.

The initializer returns once the stage has been fully processed, including loading textures and compiling shaders.

## Parameters

- `stage`: The USD stage to render.
- `timeCode`: The time code to render at. Defaults to `.default`.
- `allowsHitTesting`: Whether to generate collision shapes for hit testing. Defaults to `true`.

## See Also

- [init(allowsHitTesting: Bool)](usdstagecomponent/init(allowshittesting:).md)
  Creates a USDStageComponent in manual mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/init(_:timecode:allowshittesting:))*