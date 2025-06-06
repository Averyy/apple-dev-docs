# overlayView(_:shouldBeginAt:forAnalysisType:)

**Framework**: Visionkit  
**Kind**: method  
**Required**: Yes

Provides a Boolean value that indicates whether the interaction can begin at the given point.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, shouldBeginAt point: CGPoint, forAnalysisType analysisType: ImageAnalysisOverlayView.InteractionTypes) -> Bool
```

#### Return Value

`true` if the interaction can begin; otherwise, `false`.

#### Discussion

The system calls this method once for each type of interaction. The default value is `true`, which starts the interaction immediately after the image displays.

## Parameters

- `overlayView`: The overlay view for which interaction can begin.
- `point`: The point where the interaction can begin.
- `analysisType`: The type of interaction that can begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:shouldbeginat:foranalysistype:))*