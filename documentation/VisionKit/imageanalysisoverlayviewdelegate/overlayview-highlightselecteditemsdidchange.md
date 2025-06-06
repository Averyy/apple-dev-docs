# overlayView(_:highlightSelectedItemsDidChange:)

**Framework**: Visionkit  
**Kind**: method  
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

## See Also

- [func overlayView(ImageAnalysisOverlayView, liveTextButtonDidChangeToVisible: Bool)](imageanalysisoverlayviewdelegate/overlayview(_:livetextbuttondidchangetovisible:).md)
  Notifies your app when the Live Text button’s visibility changes.
- [func textSelectionDidChange(ImageAnalysisOverlayView)](imageanalysisoverlayviewdelegate/textselectiondidchange(_:).md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:highlightselecteditemsdidchange:))*