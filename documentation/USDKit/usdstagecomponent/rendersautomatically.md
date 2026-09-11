# rendersAutomatically

**Framework**: USDKit  
**Kind**: property

Whether the component renders automatically in response to stage or time code changes. `false` indicates manual mode, in which rendering must be triggered explicitly via [`render(_:to:at:)`](usdstagecomponent/render(_:to:at:).md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let rendersAutomatically: Bool
```

## See Also

- [var stage: USDStage?](usdstagecomponent/stage.md)
  The stage currently being rendered by this component, or `nil` if the component is in manual mode and no render has been performed yet.
- [var timeCode: USDStage.TimeCode](usdstagecomponent/timecode.md)
  The time code to render at.
- [let allowsHitTesting: Bool](usdstagecomponent/allowshittesting.md)
  Whether the rendered entities support hit testing. Set at initialization and cannot be changed afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/rendersautomatically)*