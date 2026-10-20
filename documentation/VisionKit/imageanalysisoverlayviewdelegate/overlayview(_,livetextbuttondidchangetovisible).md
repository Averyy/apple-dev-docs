# overlayView(_:liveTextButtonDidChangeToVisible:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies your app when the Live Text button’s visibility changes.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, liveTextButtonDidChangeToVisible visible: Bool)
```

## Parameters

- `overlayView`: The associated overlay view for the Live Text button.
- `visible`: `true` if the Live Text button appears; otherwise, `false`.

## Default Implementations

### ImageAnalysisOverlayViewDelegate Implementations
- [func overlayView(ImageAnalysisOverlayView, liveTextButtonDidChangeToVisible: Bool)](./overlayview%28_,livetextbuttondidchangetovisible%29-7ln8u.md)
  A default, blank implementation for when the Live Text button appears or disappears.

## See Also

### Tracking interface changes
- [func overlayView(ImageAnalysisOverlayView, highlightSelectedItemsDidChange: Bool)](./overlayview%28_,highlightselecteditemsdidchange%29.md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.
- [func textSelectionDidChange(ImageAnalysisOverlayView)](./textselectiondidchange%28_%29.md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:livetextbuttondidchangetovisible:))*