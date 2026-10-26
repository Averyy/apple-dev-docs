# overlayView(_:shouldHandleKeyDownEvent:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default implementation that indicates the overlay view handles the given key-down event.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, shouldHandleKeyDownEvent event: NSEvent) -> Bool
```

#### Return Value

This default implementation returns `true`.

## Parameters

- `overlayView`: The overlay view that implements the Live Text interface.
- `event`: The event that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldhandlekeydownevent:)-6hhnu)*