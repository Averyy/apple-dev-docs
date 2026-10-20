# overlayView(_:shouldHandleKeyDownEvent:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
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

## Default Implementations

### ImageAnalysisOverlayViewDelegate Implementations
- [func overlayView(ImageAnalysisOverlayView, shouldHandleKeyDownEvent: NSEvent) -> Bool](./overlayview%28_,shouldhandlekeydownevent%29-6hhnu.md)
  A default implementation that indicates the overlay view handles the given key-down event.

## See Also

### Responding to key and menu events
- [func overlayView(ImageAnalysisOverlayView, shouldShowMenuForEvent: NSEvent, atPoint: CGPoint) -> Bool](./overlayview%28_,shouldshowmenuforevent,atpoint%29.md)
  Provides a Boolean value that indicates whether the overlay view shows a menu for the given event.
- [func overlayView(ImageAnalysisOverlayView, menu: NSMenu, willHighlight: NSMenuItem?)](./overlayview%28_,menu,willhighlight%29.md)
  Notifies your app that the given menu item is highlighted.
- [func overlayView(ImageAnalysisOverlayView, willOpen: NSMenu)](./overlayview%28_,willopen%29.md)
  Notifies your app that a given menu is opening imminently.
- [func overlayView(ImageAnalysisOverlayView, didClose: NSMenu)](./overlayview%28_,didclose%29.md)
  Notifies your app that the given menu closed.
- [func overlayView(ImageAnalysisOverlayView, needsUpdate: NSMenu)](./overlayview%28_,needsupdate%29.md)
  Notifies your app that the given menu needs updating.
- [func overlayView(ImageAnalysisOverlayView, updatedMenuFor: NSMenu, for: NSEvent, at: CGPoint) -> NSMenu](./overlayview%28_,updatedmenufor,for,at%29.md)
  Notifies your app before the framework presents a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldhandlekeydownevent:))*