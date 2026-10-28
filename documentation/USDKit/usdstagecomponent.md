# USDStageComponent

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A component that renders a USD stage as RealityKit entities.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct USDStageComponent
```

## Overview

Attach a `USDStageComponent` to an entity to render USD content as child entities. The component supports two modes of operation:

- **Manual mode**: Created with [`init(allowsHitTesting:)`](./usdstagecomponent/init%28allowshittesting%29.md). You control when rendering occurs by calling [`render(_:to:at:)`](./usdstagecomponent/render%28_,to,at%29.md).
- **Automatic mode**: Created with [`init(_:timeCode:allowsHitTesting:)`](./usdstagecomponent/init%28_,timecode,allowshittesting%29.md). The component manages rendering internally and updates when the stage or time code changes.

## Topics

### Creating a stage component
- [init(USDStage, timeCode: USDStage.TimeCode, allowsHitTesting: Bool) async](./usdstagecomponent/init%28_,timecode,allowshittesting%29.md)
  Creates a USDStageComponent in automatic mode and waits for the first render to complete.
- [init(allowsHitTesting: Bool)](./usdstagecomponent/init%28allowshittesting%29.md)
  Creates a USDStageComponent in manual mode.
### Configuring the component
- [var stage: USDStage?](./usdstagecomponent/stage.md)
  The stage currently being rendered by this component, or `nil` if the component is in manual mode and no render has been performed yet.
- [var timeCode: USDStage.TimeCode](./usdstagecomponent/timecode.md)
  The time code to render at.
- [let allowsHitTesting: Bool](./usdstagecomponent/allowshittesting.md)
  Whether the rendered entities support hit testing. Set at initialization and cannot be changed afterwards.
- [let rendersAutomatically: Bool](./usdstagecomponent/rendersautomatically.md)
  Whether the component renders automatically in response to stage or time code changes. `false` indicates manual mode, in which rendering must be triggered explicitly via [`render(_:to:at:)`](./usdstagecomponent/render%28_,to,at%29.md).
### Rendering the stage
- [static func render(USDStage, to: Entity, at: USDStage.TimeCode) async -> USDStageComponent.RenderResult](./usdstagecomponent/render%28_,to,at%29.md)
  Renders a USD stage to an entity in manual mode.
- [USDStageComponent.RenderResult](./usdstagecomponent/renderresult.md)
  The result of a render operation.
### Type Methods
- [static func coordinateSpace(on: Entity, at: USDLayer.Path, timeCode: USDStage.TimeCode?) -> some CoordinateSpace3DFloat](./usdstagecomponent/coordinatespace%28on,at,timecode%29.md)
  Returns a coordinate space anchored to the closest rendered ancestor of `path`.
- [static func waitForRenderCompletion(on: Entity) async -> USDStageComponent.RenderResult](./usdstagecomponent/waitforrendercompletion%28on%29.md)
  Waits for automatic rendering to complete.

## Relationships

### Conforms To
- [Component](../RealityKit/component.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)

## See Also

### RealityKit rendering and playback
- [class USDPlayer](./usdplayer.md)
  Drives timeline playback of a USD stage and produces per-frame render data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent)*