# imageSubject

**Framework**: VisionKit  
**Kind**: property

An option that enables people to use a long-press gesture on a subject in an image to separate it from the background.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
static let imageSubject: ImageAnalysisInteraction.InteractionTypes
```

#### Discussion

For more information about image subjects, see [`ImageAnalysisInteraction.Subject`](imageanalysisinteraction/subject.md).

## See Also

- [static let automatic: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let textSelection: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/textselection.md)
  An option that enables text selection, copying, and translating.
- [static let dataDetectors: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/datadetectors.md)
  An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.
- [static let visualLookUp: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.
- [static let automaticTextOnly: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes/imagesubject)*