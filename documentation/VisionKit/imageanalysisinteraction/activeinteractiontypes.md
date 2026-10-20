# activeInteractionTypes

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The types of interactions that a person actively performs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var activeInteractionTypes: ImageAnalysisInteraction.InteractionTypes { get }
```

#### Discussion

This property is always a concrete type that’s never set to [`automatic`](./interactiontypes/automatic.md).

## See Also

### Configuring an image interaction
- [var delegate: (any ImageAnalysisInteractionDelegate)?](./delegate.md)
  The delegate that handles the interaction callbacks.
- [var analysis: ImageAnalysis?](./analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var view: UIView?](./view.md)
  The view that uses this interaction.
- [var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes](./preferredinteractiontypes.md)
  The types of interactions that people can perform with the image.
- [ImageAnalysisInteraction.InteractionTypes](./interactiontypes.md)
  The types of interactions that people can perform with an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/activeinteractiontypes)*