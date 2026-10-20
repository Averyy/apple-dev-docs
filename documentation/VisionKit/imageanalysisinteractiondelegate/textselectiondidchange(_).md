# textSelectionDidChange(_:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies your app when the interaction’s text selection changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func textSelectionDidChange(_ interaction: ImageAnalysisInteraction)
```

## Parameters

- `interaction`: The interaction object in which the text selection changes.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func textSelectionDidChange(ImageAnalysisInteraction)](./textselectiondidchange%28_%29-4xwp.md)
  A default, blank implementation for when the text selection changes.

## See Also

### Tracking interface changes
- [func interaction(ImageAnalysisInteraction, liveTextButtonDidChangeToVisible: Bool)](./interaction%28_,livetextbuttondidchangetovisible%29.md)
  Notifies your app when the Live Text button’s visibility changes.
- [func interaction(ImageAnalysisInteraction, highlightSelectedItemsDidChange: Bool)](./interaction%28_,highlightselecteditemsdidchange%29.md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/textselectiondidchange(_:))*