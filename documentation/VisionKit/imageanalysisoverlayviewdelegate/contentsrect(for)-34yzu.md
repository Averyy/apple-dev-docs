# contentsRect(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default implementation that returns a rectangle that specifies the full width and height of the view.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func contentsRect(for overlayView: ImageAnalysisOverlayView) -> CGRect
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

#### Return Value

The unit rectangle `[0.0, 0.0, 1.0, 1.0]`.

## Parameters

- `overlayView`: The overlay view that implements the Live Text interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/contentsrect(for:)-34yzu)*