# activeInteractionTypes

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The types of interactions that a person actively performs.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes { get }
```

## Discussion

This property is always a concrete type that’s never set to [`automatic`](./interactiontypes/automatic.md).

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
- [var trackingImageView: NSImageView?](./trackingimageview.md)
  The image view that contains the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/activeinteractiontypes)*