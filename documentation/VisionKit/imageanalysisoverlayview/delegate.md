# delegate

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

An object that handles image analysis interface callbacks.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
weak final var delegate: (any ImageAnalysisOverlayViewDelegate)? { get set }
```

## See Also

### Configuring overlay views
- [var analysis: ImageAnalysis?](./analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [ImageAnalysisOverlayView.InteractionTypes](./interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var trackingImageView: NSImageView?](./trackingimageview.md)
  The image view that contains the image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/delegate)*