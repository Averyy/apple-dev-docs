# activeInteractionTypes

**Framework**: VisionKit  
**Kind**: property

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

This property is always a concrete type that’s never set to [`automatic`](imageanalysisinteraction/interactiontypes/automatic.md).

## See Also

- [var delegate: (any ImageAnalysisInteractionDelegate)?](imageanalysisinteraction/delegate.md)
  The delegate that handles the interaction callbacks.
- [var analysis: ImageAnalysis?](imageanalysisinteraction/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var view: UIView?](imageanalysisinteraction/view.md)
  The view that uses this interaction.
- [var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image.
- [ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes.md)
  The types of interactions that people can perform with an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/activeinteractiontypes)*