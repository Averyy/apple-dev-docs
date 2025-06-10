# view

**Framework**: VisionKit  
**Kind**: property

The view that uses this interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency weak final var view: UIView? { get }
```

## See Also

- [var delegate: (any ImageAnalysisInteractionDelegate)?](imageanalysisinteraction/delegate.md)
  The delegate that handles the interaction callbacks.
- [var analysis: ImageAnalysis?](imageanalysisinteraction/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image.
- [ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var activeInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/view)*