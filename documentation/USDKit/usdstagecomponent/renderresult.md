# USDStageComponent.RenderResult

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

The result of a render operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct RenderResult
```

## Topics

### Instance Properties
- [let errors: [USDRenderError]](./renderresult/errors.md)
  The errors encountered during the render, or an empty array if it succeeded.
- [let status: USDStageComponent.RenderResult.Status](./renderresult/status-swift.property.md)
  The status of the render operation.
### Enumerations
- [USDStageComponent.RenderResult.Status](./renderresult/status-swift.enum.md)
  The status of a render operation.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Rendering the stage
- [static func render(USDStage, to: Entity, at: USDStage.TimeCode) async -> USDStageComponent.RenderResult](./render%28_,to,at%29.md)
  Renders a USD stage to an entity in manual mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/renderresult)*