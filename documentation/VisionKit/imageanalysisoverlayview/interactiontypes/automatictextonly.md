# automaticTextOnly

**Framework**: Visionkit  
**Kind**: property

An option that enables all interaction types except image subjects and Visual Look Up.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let automaticTextOnly: ImageAnalysisOverlayView.InteractionTypes
```

#### Discussion

This option represents the [`automatic`](imageanalysisoverlayview/interactiontypes/automatic.md) type, but excludes the [`imageSubject`](imageanalysisoverlayview/interactiontypes/imagesubject.md) and [`visualLookUp`](imageanalysisoverlayview/interactiontypes/visuallookup.md) types.

## See Also

- [static let automatic: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let textSelection: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/textselection.md)
  An option that enables text selection, copying, and translating.
- [static let dataDetectors: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/datadetectors.md)
  An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.
- [static let imageSubject: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/imagesubject.md)
  An option that enables people to click or tap a subject in an image to separate it from the background.
- [static let visualLookUp: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/interactiontypes/automatictextonly)*