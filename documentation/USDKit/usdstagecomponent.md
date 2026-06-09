# USDStageComponent

**Framework**: USDKit  
**Kind**: struct

A component that renders a USD stage as RealityKit entities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDStageComponent
```

#### Overview

Attach a `USDStageComponent` to an entity to render USD content as child entities. The component supports two modes of operation:

- **Manual mode**: Created with [`init(allowsHitTesting:)`](usdstagecomponent/init(allowshittesting:).md). You control when rendering occurs by calling [`render(_:to:at:)`](usdstagecomponent/render(_:to:at:).md).
- **Automatic mode**: Created with [`init(_:timeCode:allowsHitTesting:)`](usdstagecomponent/init(_:timecode:allowshittesting:).md). The component manages rendering internally and updates when the stage or time code changes.

## Topics

### Creating a stage component
- [init(USDStage, timeCode: USDStage.TimeCode, allowsHitTesting: Bool) async](usdstagecomponent/init(_:timecode:allowshittesting:).md)
  Creates a USDStageComponent in automatic mode and waits for the first render to complete.
- [init(allowsHitTesting: Bool)](usdstagecomponent/init(allowshittesting:).md)
  Creates a USDStageComponent in manual mode.
### Configuring the component
- [var stage: USDStage?](usdstagecomponent/stage.md)
  The stage currently being rendered by this component, or `nil` if the component is in manual mode and no render has been performed yet.
- [var timeCode: USDStage.TimeCode](usdstagecomponent/timecode.md)
  The time code to render at.
- [let allowsHitTesting: Bool](usdstagecomponent/allowshittesting.md)
  Whether the rendered entities support hit testing. Set at initialization and cannot be changed afterwards.
- [let rendersAutomatically: Bool](usdstagecomponent/rendersautomatically.md)
  Whether the component renders automatically in response to stage or time code changes. `false` indicates manual mode, in which rendering must be triggered explicitly via [`render(_:to:at:)`](usdstagecomponent/render(_:to:at:).md).
### Rendering the stage
- [static func render(USDStage, to: Entity, at: USDStage.TimeCode) async -> USDStageComponent.RenderResult](usdstagecomponent/render(_:to:at:).md)
  Renders a USD stage to an entity in manual mode.
- [static func waitForRenderComplete(on: Entity) async -> USDStageComponent.RenderResult](usdstagecomponent/waitforrendercomplete(on:).md)
  Waits for automatic rendering to complete.
- [USDStageComponent.RenderResult](usdstagecomponent/renderresult.md)
  The result of a render operation.

## Relationships

### Conforms To
- [Component](../RealityKit/Component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [class USDPlayer](usdplayer.md)
  An object that drives timeline playback of a USD stage in RealityKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent)*