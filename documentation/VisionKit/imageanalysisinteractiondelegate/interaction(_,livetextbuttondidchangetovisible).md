# interaction(_:liveTextButtonDidChangeToVisible:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies your app when the Live Text button’s visibility changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func interaction(_ interaction: ImageAnalysisInteraction, liveTextButtonDidChangeToVisible visible: Bool)
```

## Parameters

- `interaction`: The interaction object for which the Live Text button appears.
- `visible`: `true` if the Live Text button appears; otherwise,`false`.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func interaction(ImageAnalysisInteraction, liveTextButtonDidChangeToVisible: Bool)](./interaction%28_,livetextbuttondidchangetovisible%29-51zmv.md)
  A default, blank implementation for when the Live Text button appears or disappears.

## See Also

### Tracking interface changes
- [func interaction(ImageAnalysisInteraction, highlightSelectedItemsDidChange: Bool)](./interaction%28_,highlightselecteditemsdidchange%29.md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.
- [func textSelectionDidChange(ImageAnalysisInteraction)](./textselectiondidchange%28_%29.md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/interaction(_:livetextbuttondidchangetovisible:))*