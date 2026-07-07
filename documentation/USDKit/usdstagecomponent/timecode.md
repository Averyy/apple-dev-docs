# timeCode

**Framework**: USDKit  
**Kind**: property

The time code to render at.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var timeCode: USDStage.TimeCode { get set }
```

#### Discussion

In automatic mode, the system reads this value to determine what time to render at. Updating this value triggers a re-render. In manual mode, this value is unused. Pass the time code directly to [`render(_:to:at:)`](usdstagecomponent/render(_:to:at:).md) instead.

## See Also

- [var stage: USDStage?](usdstagecomponent/stage.md)
  The stage currently being rendered by this component, or `nil` if the component is in manual mode and no render has been performed yet.
- [let allowsHitTesting: Bool](usdstagecomponent/allowshittesting.md)
  Whether the rendered entities support hit testing. Set at initialization and cannot be changed afterwards.
- [let rendersAutomatically: Bool](usdstagecomponent/rendersautomatically.md)
  Whether the component renders automatically in response to stage or time code changes. `false` indicates manual mode, in which rendering must be triggered explicitly via [`render(_:to:at:)`](usdstagecomponent/render(_:to:at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/timecode)*