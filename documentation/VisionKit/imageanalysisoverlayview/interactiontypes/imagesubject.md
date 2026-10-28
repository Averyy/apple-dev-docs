# imageSubject

**Framework**: VisionKit  
**Kind**: property  
**Role**: Type Property

An option that enables people to click or tap a subject in an image to separate it from the background.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static let imageSubject: ImageAnalysisOverlayView.InteractionTypes
```

## Discussion

For more information about image subjects, see [`ImageAnalysisOverlayView.Subject`](../subject.md).

## See Also

### Specifying types of interactions
- [static let automatic: ImageAnalysisOverlayView.InteractionTypes](./automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let textSelection: ImageAnalysisOverlayView.InteractionTypes](./textselection.md)
  An option that enables text selection, copying, and translating.
- [static let dataDetectors: ImageAnalysisOverlayView.InteractionTypes](./datadetectors.md)
  An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.
- [static let visualLookUp: ImageAnalysisOverlayView.InteractionTypes](./visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.
- [static let automaticTextOnly: ImageAnalysisOverlayView.InteractionTypes](./automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/interactiontypes/imagesubject)*