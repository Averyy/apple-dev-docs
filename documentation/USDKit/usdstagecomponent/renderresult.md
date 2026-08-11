# USDStageComponent.RenderResult

**Framework**: USDKit  
**Kind**: struct

The result of a render operation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderResult
```

## Topics

### Instance Properties
- [let errors: [USDRenderError]](usdstagecomponent/renderresult/errors.md)
  The errors encountered during the render, or an empty array if it succeeded.
- [let status: USDStageComponent.RenderResult.Status](usdstagecomponent/renderresult/status-swift.property.md)
  The status of the render operation.
### Enumerations
- [USDStageComponent.RenderResult.Status](usdstagecomponent/renderresult/status-swift.enum.md)
  The status of a render operation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func render(USDStage, to: Entity, at: USDStage.TimeCode) async -> USDStageComponent.RenderResult](usdstagecomponent/render(_:to:at:).md)
  Renders a USD stage to an entity in manual mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/renderresult)*