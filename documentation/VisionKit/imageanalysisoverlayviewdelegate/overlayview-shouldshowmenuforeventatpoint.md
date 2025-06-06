# overlayView(_:shouldShowMenuForEvent:atPoint:)

**Framework**: Visionkit  
**Kind**: method  
**Required**: Yes

Provides a Boolean value that indicates whether the overlay view shows a menu for the given event.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, shouldShowMenuForEvent event: NSEvent, atPoint point: CGPoint) -> Bool
```

#### Return Value

`true` if the menu appears in the overlay; otherwise, `false`.

#### Discussion

Implement this method if you don’t want the overlay view to show a menu for a specific event at a location. The default return value is `true`.

## Parameters

- `overlayView`: The overlay view in which the menu appears.
- `event`: The event that occurs.
- `point`: The location of the event.

## See Also

- [func overlayView(ImageAnalysisOverlayView, shouldHandleKeyDownEvent: NSEvent) -> Bool](imageanalysisoverlayviewdelegate/overlayview(_:shouldhandlekeydownevent:).md)
  Returns a Boolean value that indicates whether the overlay view consumes the given key-down event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldshowmenuforevent:atpoint:))*