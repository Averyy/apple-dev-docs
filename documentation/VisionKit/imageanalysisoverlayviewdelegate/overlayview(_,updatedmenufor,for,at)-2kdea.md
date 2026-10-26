# overlayView(_:updatedMenuFor:for:at:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default implementation that returns the menu without any changes.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, updatedMenuFor menu: NSMenu, for event: NSEvent, at point: CGPoint) -> NSMenu
```

## Parameters

- `overlayView`: The interaction object for the Live Text interface.
- `menu`: The menu to be presented.
- `event`: The event associated with this menu.
- `point`: The original location of the event for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:updatedmenufor:for:at:)-2kdea)*