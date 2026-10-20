# preferredInteractionTypes

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The types of interactions that people can perform with the image in this overlay view.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes { get set }
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

#### Discussion

You need to set this property to enable the Live Text interface with the image. If this property contains [`automatic`](./interactiontypes/automatic.md), the overlay view ignores the other interaction types in the set. The default value for this property is an empty array that disables any interactions.

## See Also

### Configuring overlay views
- [var delegate: (any ImageAnalysisOverlayViewDelegate)?](./delegate.md)
  An object that handles image analysis interface callbacks.
- [var analysis: ImageAnalysis?](./analysis.md)
  The results of analyzing an image for items that people can interact with.
- [ImageAnalysisOverlayView.InteractionTypes](./interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var trackingImageView: NSImageView?](./trackingimageview.md)
  The image view that contains the image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/preferredinteractiontypes)*