# overlayView(_:shouldBeginAt:forAnalysisType:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether interaction begins at the given point for the specified interaction type.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, shouldBeginAt point: CGPoint, forAnalysisType analysisType: ImageAnalysisOverlayView.InteractionTypes) -> Bool
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

#### Return Value

This default implementation returns `true`.

#### Discussion

The overlay view invokes this method once for each type of interaction. The default return value is `true`, which starts the interface immediately upon presentation.

## Parameters

- `overlayView`: The overlay view that implements the Live Text interface.
- `point`: The point where the interface begins.
- `analysisType`: The type of interaction that starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldbeginat:foranalysistype:)-35czq)*