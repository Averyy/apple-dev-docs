# dataDetectors

**Framework**: Visionkit  
**Kind**: property

An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let dataDetectors: ImageAnalysisOverlayView.InteractionTypes
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

People interact with , or UI that highlights each instance of the recognized formats in text that’s on an image. The data detectors appear without a Live Text button, because people can’t interact with other text with this option.

## See Also

- [static let automatic: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let textSelection: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/textselection.md)
  An option that enables text selection, copying, and translating.
- [static let imageSubject: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/imagesubject.md)
  An option that enables people to click or tap a subject in an image to separate it from the background.
- [static let visualLookUp: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.
- [static let automaticTextOnly: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/interactiontypes/datadetectors)*