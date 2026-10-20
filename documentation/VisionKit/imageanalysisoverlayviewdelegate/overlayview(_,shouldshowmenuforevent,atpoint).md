# overlayView(_:shouldShowMenuForEvent:atPoint:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
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

## Default Implementations

### ImageAnalysisOverlayViewDelegate Implementations
- [func overlayView(ImageAnalysisOverlayView, shouldShowMenuForEvent: NSEvent, atPoint: CGPoint) -> Bool](./overlayview%28_,shouldshowmenuforevent,atpoint%29-2irgq.md)
  A default implementation that indicates the overlay view shows its menu for the given event.

## See Also

### Responding to key and menu events
- [func overlayView(ImageAnalysisOverlayView, shouldHandleKeyDownEvent: NSEvent) -> Bool](./overlayview%28_,shouldhandlekeydownevent%29.md)
  Returns a Boolean value that indicates whether the overlay view consumes the given key-down event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldshowmenuforevent:atpoint:))*