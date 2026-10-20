# overlayView(_:willOpen:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies your app that a given menu is opening imminently.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, willOpen menu: NSMenu)
```

## Parameters

- `overlayView`: The associated overlay view for the menu.
- `menu`: The menu that will open.

## Default Implementations

### ImageAnalysisOverlayViewDelegate Implementations
- [func overlayView(ImageAnalysisOverlayView, willOpen: NSMenu)](./overlayview%28_,willopen%29-5t8cy.md)
  A default, blank implementation for when an overlay view menu opens.

## See Also

### Responding to key and menu events
- [func overlayView(ImageAnalysisOverlayView, shouldHandleKeyDownEvent: NSEvent) -> Bool](./overlayview%28_,shouldhandlekeydownevent%29.md)
  Returns a Boolean value that indicates whether the overlay view consumes the given key-down event.
- [func overlayView(ImageAnalysisOverlayView, shouldShowMenuForEvent: NSEvent, atPoint: CGPoint) -> Bool](./overlayview%28_,shouldshowmenuforevent,atpoint%29.md)
  Provides a Boolean value that indicates whether the overlay view shows a menu for the given event.
- [func overlayView(ImageAnalysisOverlayView, menu: NSMenu, willHighlight: NSMenuItem?)](./overlayview%28_,menu,willhighlight%29.md)
  Notifies your app that the given menu item is highlighted.
- [func overlayView(ImageAnalysisOverlayView, didClose: NSMenu)](./overlayview%28_,didclose%29.md)
  Notifies your app that the given menu closed.
- [func overlayView(ImageAnalysisOverlayView, needsUpdate: NSMenu)](./overlayview%28_,needsupdate%29.md)
  Notifies your app that the given menu needs updating.
- [func overlayView(ImageAnalysisOverlayView, updatedMenuFor: NSMenu, for: NSEvent, at: CGPoint) -> NSMenu](./overlayview%28_,updatedmenufor,for,at%29.md)
  Notifies your app before the framework presents a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:willopen:))*