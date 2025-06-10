# textSelectionDidChange(_:)

**Framework**: VisionKit  
**Kind**: method  
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

## See Also

- [func interaction(ImageAnalysisInteraction, liveTextButtonDidChangeToVisible: Bool)](imageanalysisinteractiondelegate/interaction(_:livetextbuttondidchangetovisible:).md)
  Notifies your app when the Live Text button’s visibility changes.
- [func interaction(ImageAnalysisInteraction, highlightSelectedItemsDidChange: Bool)](imageanalysisinteractiondelegate/interaction(_:highlightselecteditemsdidchange:).md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/textselectiondidchange(_:))*