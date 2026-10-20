# overlayView(_:highlightSelectedItemsDidChange:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies your app when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, highlightSelectedItemsDidChange highlightSelectedItems: Bool)
```

## Parameters

- `overlayView`: The overlay view for which the selected item highlights change.
- `highlightSelectedItems`: A Boolean value that indicates whether highlights appear.

## Default Implementations

### ImageAnalysisOverlayViewDelegate Implementations
- [func overlayView(ImageAnalysisOverlayView, highlightSelectedItemsDidChange: Bool)](./overlayview%28_,highlightselecteditemsdidchange%29-68r8g.md)
  A default, blank implementation for when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.

## See Also

### Tracking interface changes
- [func overlayView(ImageAnalysisOverlayView, liveTextButtonDidChangeToVisible: Bool)](./overlayview%28_,livetextbuttondidchangetovisible%29.md)
  Notifies your app when the Live Text button’s visibility changes.
- [func textSelectionDidChange(ImageAnalysisOverlayView)](./textselectiondidchange%28_%29.md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:highlightselecteditemsdidchange:))*