# trackingImageView

**Framework**: Visionkit  
**Kind**: property

The image view that contains the image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
weak final var trackingImageView: NSImageView? { get set }
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

Optionally, set this property to the image view that contains the image, and the overlay view automatically calculates the [`contentsRect`](imageanalysisoverlayview/contentsrect.md) property value based on the image view properties.

## See Also

- [var delegate: (any ImageAnalysisOverlayViewDelegate)?](imageanalysisoverlayview/delegate.md)
  An object that handles image analysis interface callbacks.
- [var analysis: ImageAnalysis?](imageanalysisoverlayview/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/trackingimageview)*