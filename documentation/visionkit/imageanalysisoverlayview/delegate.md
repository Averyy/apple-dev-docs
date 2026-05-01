# delegate

**Framework**: VisionKit  
**Kind**: property

An object that handles image analysis interface callbacks.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
weak final var delegate: (any ImageAnalysisOverlayViewDelegate)? { get set }
```

## See Also

- [var analysis: ImageAnalysis?](imageanalysisoverlayview/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var trackingImageView: NSImageView?](imageanalysisoverlayview/trackingimageview.md)
  The image view that contains the image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/delegate)*