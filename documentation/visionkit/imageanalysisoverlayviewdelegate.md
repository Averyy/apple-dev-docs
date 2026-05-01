# ImageAnalysisOverlayViewDelegate

**Framework**: VisionKit  
**Kind**: protocol

A delegate that handles image-analysis and user-interaction callbacks for an overlay view.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
protocol ImageAnalysisOverlayViewDelegate : AnyObject
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Overview

The delegate of an [`ImageAnalysisOverlayView`](imageanalysisoverlayview.md) object implements this protocol to provide interface details and to customize the response for a person’s interaction.

## Topics

### Providing interface details
- [func contentView(for: ImageAnalysisOverlayView) -> NSView?](imageanalysisoverlayviewdelegate/contentview(for:).md)
  Provides the view that contains the image.
- [func contentsRect(for: ImageAnalysisOverlayView) -> CGRect](imageanalysisoverlayviewdelegate/contentsrect(for:).md)
  Returns the rectangle, in unit coordinate space, that contains the image within the view.
### Starting the interaction
- [func overlayView(ImageAnalysisOverlayView, shouldBeginAt: CGPoint, forAnalysisType: ImageAnalysisOverlayView.InteractionTypes) -> Bool](imageanalysisoverlayviewdelegate/overlayview(_:shouldbeginat:foranalysistype:).md)
  Provides a Boolean value that indicates whether the interaction can begin at the given point.
### Tracking interface changes
- [func overlayView(ImageAnalysisOverlayView, liveTextButtonDidChangeToVisible: Bool)](imageanalysisoverlayviewdelegate/overlayview(_:livetextbuttondidchangetovisible:).md)
  Notifies your app when the Live Text button’s visibility changes.
- [func overlayView(ImageAnalysisOverlayView, highlightSelectedItemsDidChange: Bool)](imageanalysisoverlayviewdelegate/overlayview(_:highlightselecteditemsdidchange:).md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.
- [func textSelectionDidChange(ImageAnalysisOverlayView)](imageanalysisoverlayviewdelegate/textselectiondidchange(_:).md)
  Notifies your app when the interaction’s text selection changes.
### Responding to key and menu events
- [func overlayView(ImageAnalysisOverlayView, shouldHandleKeyDownEvent: NSEvent) -> Bool](imageanalysisoverlayviewdelegate/overlayview(_:shouldhandlekeydownevent:).md)
  Returns a Boolean value that indicates whether the overlay view consumes the given key-down event.
- [func overlayView(ImageAnalysisOverlayView, shouldShowMenuForEvent: NSEvent, atPoint: CGPoint) -> Bool](imageanalysisoverlayviewdelegate/overlayview(_:shouldshowmenuforevent:atpoint:).md)
  Provides a Boolean value that indicates whether the overlay view shows a menu for the given event.
- [func overlayView(ImageAnalysisOverlayView, menu: NSMenu, willHighlight: NSMenuItem?)](imageanalysisoverlayviewdelegate/overlayview(_:menu:willhighlight:).md)
  Notifies your app that the given menu item is highlighted.
- [func overlayView(ImageAnalysisOverlayView, willOpen: NSMenu)](imageanalysisoverlayviewdelegate/overlayview(_:willopen:).md)
  Notifies your app that a given menu is opening imminently.
- [func overlayView(ImageAnalysisOverlayView, didClose: NSMenu)](imageanalysisoverlayviewdelegate/overlayview(_:didclose:).md)
  Notifies your app that the given menu closed.
- [func overlayView(ImageAnalysisOverlayView, needsUpdate: NSMenu)](imageanalysisoverlayviewdelegate/overlayview(_:needsupdate:).md)
  Notifies your app that the given menu needs updating.
- [func overlayView(ImageAnalysisOverlayView, updatedMenuFor: NSMenu, for: NSEvent, at: CGPoint) -> NSMenu](imageanalysisoverlayviewdelegate/overlayview(_:updatedmenufor:for:at:).md)
  Notifies your app before the framework presents a context menu.

## See Also

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalyzer](imageanalyzer.md)
  An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [class ImageAnalysisInteraction](imageanalysisinteraction.md)
  An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisInteractionDelegate](imageanalysisinteractiondelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- [class ImageAnalysisOverlayView](imageanalysisoverlayview.md)
  A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- [struct CameraRegionView](cameraregionview.md)
  This view displays a stabilized region of interest within a person’s view and provides passthrough camera feed for that selected region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate)*