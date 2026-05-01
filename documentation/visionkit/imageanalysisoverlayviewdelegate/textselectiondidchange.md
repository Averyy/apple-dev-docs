# textSelectionDidChange(_:)

**Framework**: VisionKit  
**Kind**: method  
**Required**: Yes

Notifies your app when the interaction’s text selection changes.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func textSelectionDidChange(_ overlayView: ImageAnalysisOverlayView)
```

## Parameters

- `overlayView`: The overlay view  in which the text selection changes.

## See Also

- [func overlayView(ImageAnalysisOverlayView, liveTextButtonDidChangeToVisible: Bool)](imageanalysisoverlayviewdelegate/overlayview(_:livetextbuttondidchangetovisible:).md)
  Notifies your app when the Live Text button’s visibility changes.
- [func overlayView(ImageAnalysisOverlayView, highlightSelectedItemsDidChange: Bool)](imageanalysisoverlayviewdelegate/overlayview(_:highlightselecteditemsdidchange:).md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/textselectiondidchange(_:))*