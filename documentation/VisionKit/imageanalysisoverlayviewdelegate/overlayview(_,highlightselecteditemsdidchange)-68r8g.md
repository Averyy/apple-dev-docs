# overlayView(_:highlightSelectedItemsDidChange:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default, blank implementation for when recognized items in the image appear highlighted as a result of a person clicking or tapping the Live Text button.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, highlightSelectedItemsDidChange highlightSelectedItems: Bool)
```

## Parameters

- `overlayView`: The interaction object for the Live Text interface.
- `highlightSelectedItems`: `true` if the interface highlights recognized items; otherwise, `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:highlightselecteditemsdidchange:)-68r8g)*