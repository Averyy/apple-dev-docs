# overlayView(_:liveTextButtonDidChangeToVisible:)

**Framework**: Visionkit  
**Kind**: method  
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
- `visible`:   if the Live Text button   appears; otherwise,  .

## See Also

- [func overlayView(ImageAnalysisOverlayView, highlightSelectedItemsDidChange: Bool)](imageanalysisoverlayviewdelegate/overlayview(_:highlightselecteditemsdidchange:).md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.
- [func textSelectionDidChange(ImageAnalysisOverlayView)](imageanalysisoverlayviewdelegate/textselectiondidchange(_:).md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:livetextbuttondidchangetovisible:))*