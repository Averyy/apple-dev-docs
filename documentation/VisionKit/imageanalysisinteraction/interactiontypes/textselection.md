# textSelection

**Framework**: Visionkit  
**Kind**: property

An option that enables text selection, copying, and translating.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
static let textSelection: ImageAnalysisInteraction.InteractionTypes
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

People can select text to perform actions. In this mode, the framework disables data detectors ([`dataDetectors`](imageanalysisinteraction/interactiontypes/datadetectors.md)) by default. However, if you set the [`allowLongPressForDataDetectorsInTextMode`](imageanalysisinteraction/allowlongpressfordatadetectorsintextmode.md) property to `true`, a person can use a long-press gesture to enable them.

## See Also

- [static let automatic: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let dataDetectors: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/datadetectors.md)
  An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.
- [static let imageSubject: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/imagesubject.md)
  An option that enables people to use a long-press gesture on a subject in an image to separate it from the background.
- [static let visualLookUp: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.
- [static let automaticTextOnly: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes/textselection)*