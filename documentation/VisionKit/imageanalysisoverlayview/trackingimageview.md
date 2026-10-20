# trackingImageView

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The image view that contains the image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
weak final var trackingImageView: NSImageView? { get set }
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

#### Discussion

Optionally, set this property to the image view that contains the image, and the overlay view automatically calculates the [`contentsRect`](./contentsrect.md) property value based on the image view properties.

## See Also

### Configuring overlay views
- [var delegate: (any ImageAnalysisOverlayViewDelegate)?](./delegate.md)
  An object that handles image analysis interface callbacks.
- [var analysis: ImageAnalysis?](./analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [ImageAnalysisOverlayView.InteractionTypes](./interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/trackingimageview)*