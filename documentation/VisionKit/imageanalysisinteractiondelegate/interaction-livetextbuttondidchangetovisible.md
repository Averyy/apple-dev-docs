# interaction(_:liveTextButtonDidChangeToVisible:)

**Framework**: VisionKit  
**Kind**: method  
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
- `visible`:   if the Live Text button appears; otherwise, .

## See Also

- [func interaction(ImageAnalysisInteraction, highlightSelectedItemsDidChange: Bool)](imageanalysisinteractiondelegate/interaction(_:highlightselecteditemsdidchange:).md)
  Notifies your app when recognized items in the image appear highlighted as a result of a person tapping the Live Text button.
- [func textSelectionDidChange(ImageAnalysisInteraction)](imageanalysisinteractiondelegate/textselectiondidchange(_:).md)
  Notifies your app when the interaction’s text selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/interaction(_:livetextbuttondidchangetovisible:))*