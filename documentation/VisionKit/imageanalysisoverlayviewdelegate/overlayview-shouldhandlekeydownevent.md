# overlayView(_:shouldHandleKeyDownEvent:)

**Framework**: Visionkit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the overlay view consumes the given key-down event.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, shouldHandleKeyDownEvent event: NSEvent) -> Bool
```

#### Return Value

`true` if the overlay view handles the event; otherwise, `false`.

#### Discussion

The default return value is `true`. Implement this callback if you don’t want the overlay view to consume the given event.

## Parameters

- `overlayView`: The overlay view that receives the key-down event.
- `event`: The key-down event that occurs.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldhandlekeydownevent:))*