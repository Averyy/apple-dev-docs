# render(_:to:at:)

**Framework**: USDKit  
**Kind**: method

Renders a USD stage to an entity in manual mode.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) static func render(_ stage: USDStage, to entity: Entity, at timeCode: USDStage.TimeCode = .default) async -> USDStageComponent.RenderResult
```

#### Return Value

The result of the render operation.

#### Discussion

If the entity does not have a `USDStageComponent` attached, or if the attached component is in automatic mode, the result is `.failed`.

## Parameters

- `stage`: The USD stage to render.
- `entity`: The entity to render into.
- `timeCode`: The time code to render at.

## See Also

- [static func waitForRenderComplete(on: Entity) async -> USDStageComponent.RenderResult](usdstagecomponent/waitforrendercomplete(on:).md)
  Waits for automatic rendering to complete.
- [USDStageComponent.RenderResult](usdstagecomponent/renderresult.md)
  The result of a render operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/render(_:to:at:))*