# stage

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

The stage currently being rendered by this component, or `nil` if the component is in manual mode and no render has been performed yet.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var stage: USDStage? { get }
```

## See Also

### Configuring the component
- [var timeCode: USDStage.TimeCode](./timecode.md)
  The time code to render at.
- [let allowsHitTesting: Bool](./allowshittesting.md)
  Whether the rendered entities support hit testing. Set at initialization and cannot be changed afterwards.
- [let rendersAutomatically: Bool](./rendersautomatically.md)
  Whether the component renders automatically in response to stage or time code changes. `false` indicates manual mode, in which rendering must be triggered explicitly via [`render(_:to:at:)`](./render%28_,to,at%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/stage)*