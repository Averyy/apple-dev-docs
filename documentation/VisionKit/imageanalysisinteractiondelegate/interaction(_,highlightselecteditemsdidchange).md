# interaction(_:highlightSelectedItemsDidChange:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies your app when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func interaction(_ interaction: ImageAnalysisInteraction, highlightSelectedItemsDidChange highlightSelectedItems: Bool)
```

## Parameters

- `interaction`: The interaction object for which the selected item highlights change.
- `highlightSelectedItems`: A Boolean value that indicates whether highlights appear.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func interaction(ImageAnalysisInteraction, highlightSelectedItemsDidChange: Bool)](./interaction%28_,highlightselecteditemsdidchange%29-qsjs.md)
  A default, blank implementation for when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.

## See Also

### Tracking interface changes
- [func interaction(ImageAnalysisInteraction, liveTextButtonDidChangeToVisible: Bool)](./interaction%28_,livetextbuttondidchangetovisible%29.md)
  Notifies your app when the Live Text button’s visibility changes.
- [func textSelectionDidChange(ImageAnalysisInteraction)](./textselectiondidchange%28_%29.md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/interaction(_:highlightselecteditemsdidchange:))*