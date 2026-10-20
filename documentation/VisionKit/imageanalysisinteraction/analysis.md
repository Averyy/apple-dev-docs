# analysis

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The results of analyzing an image for items that people can interact with.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var analysis: ImageAnalysis? { get set }
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

## See Also

### Configuring an image interaction
- [var delegate: (any ImageAnalysisInteractionDelegate)?](./delegate.md)
  The delegate that handles the interaction callbacks.
- [var view: UIView?](./view.md)
  The view that uses this interaction.
- [var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes](./preferredinteractiontypes.md)
  The types of interactions that people can perform with the image.
- [ImageAnalysisInteraction.InteractionTypes](./interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var activeInteractionTypes: ImageAnalysisInteraction.InteractionTypes](./activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/analysis)*