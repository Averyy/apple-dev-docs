# ImageAnalysisInteractionDelegate

**Framework**: VisionKit  
**Kind**: protocol

A delegate that handles image-analysis and user-interaction callbacks for an interaction object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol ImageAnalysisInteractionDelegate : AnyObject
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Overview

The delegate of an [`ImageAnalysisInteraction`](imageanalysisinteraction.md) object implements this protocol to provide interface details and to customize the response for a person’s interaction.

## Topics

### Providing interface details
- [func contentView(for: ImageAnalysisInteraction) -> UIView?](imageanalysisinteractiondelegate/contentview(for:).md)
  Provides the view that contains the image.
- [func contentsRect(for: ImageAnalysisInteraction) -> CGRect](imageanalysisinteractiondelegate/contentsrect(for:).md)
  Returns the rectangle, in unit coordinates, that contains the image within the view.
- [func presentingViewController(for: ImageAnalysisInteraction) -> UIViewController?](imageanalysisinteractiondelegate/presentingviewcontroller(for:).md)
  Provides the view controller that presents the interface objects.
### Starting the interaction
- [func interaction(ImageAnalysisInteraction, shouldBeginAt: CGPoint, for: ImageAnalysisInteraction.InteractionTypes) -> Bool](imageanalysisinteractiondelegate/interaction(_:shouldbeginat:for:).md)
  Provides a Boolean value that indicates whether the interaction can begin at the given point.
### Tracking interface changes
- [func interaction(ImageAnalysisInteraction, liveTextButtonDidChangeToVisible: Bool)](imageanalysisinteractiondelegate/interaction(_:livetextbuttondidchangetovisible:).md)
  Notifies your app when the Live Text button’s visibility changes.
- [func interaction(ImageAnalysisInteraction, highlightSelectedItemsDidChange: Bool)](imageanalysisinteractiondelegate/interaction(_:highlightselecteditemsdidchange:).md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.
- [func textSelectionDidChange(ImageAnalysisInteraction)](imageanalysisinteractiondelegate/textselectiondidchange(_:).md)
  Notifies your app when the interaction’s text selection changes.

## See Also

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalyzer](imageanalyzer.md)
  An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [class ImageAnalysisInteraction](imageanalysisinteraction.md)
  An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- [class ImageAnalysisOverlayView](imageanalysisoverlayview.md)
  A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisOverlayViewDelegate](imageanalysisoverlayviewdelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an overlay view.
- [struct CameraRegionView](cameraregionview.md)
  This view displays a stabilized region of interest within a person’s view and provides passthrough camera feed for that selected region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate)*