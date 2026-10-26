# overlayView(_:shouldShowMenuForEvent:atPoint:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default implementation that indicates the overlay view shows its menu for the given event.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, shouldShowMenuForEvent event: NSEvent, atPoint point: CGPoint) -> Bool
```

#### Return Value

This default implementation returns `true`.

## Parameters

- `overlayView`: The overlay view that implements the Live Text interface.
- `event`: The event that occurs.
- `point`: The location of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldshowmenuforevent:atpoint:)-2irgq)*