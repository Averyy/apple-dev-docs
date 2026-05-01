# overlayView(_:needsUpdate:)

**Framework**: VisionKit  
**Kind**: method  
**Required**: Yes

Notifies your app that the given menu needs updating.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, needsUpdate menu: NSMenu)
```

## Parameters

- `overlayView`: The associated overlay view for the menu.
- `menu`: The menu that updates.

## See Also

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
- [func overlayView(ImageAnalysisOverlayView, updatedMenuFor: NSMenu, for: NSEvent, at: CGPoint) -> NSMenu](imageanalysisoverlayviewdelegate/overlayview(_:updatedmenufor:for:at:).md)
  Notifies your app before the framework presents a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:needsupdate:))*