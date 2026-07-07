# waitForRenderComplete(on:)

**Framework**: USDKit  
**Kind**: method

Waits for automatic rendering to complete.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func waitForRenderComplete(on entity: Entity) async -> USDStageComponent.RenderResult
```

#### Return Value

The result of the render operation.

#### Discussion

If the entity does not have a `USDStageComponent` attached, or if the attached component is in manual mode, the result is `.failed`.

## Parameters

- `entity`: The entity with a `USDStageComponent`.

## See Also

- [static func render(USDStage, to: Entity, at: USDStage.TimeCode) async -> USDStageComponent.RenderResult](usdstagecomponent/render(_:to:at:).md)
  Renders a USD stage to an entity in manual mode.
- [USDStageComponent.RenderResult](usdstagecomponent/renderresult.md)
  The result of a render operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/waitforrendercomplete(on:))*