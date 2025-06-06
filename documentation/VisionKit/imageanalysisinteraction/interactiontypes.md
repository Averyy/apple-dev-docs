# ImageAnalysisInteraction.InteractionTypes

**Framework**: Visionkit  
**Kind**: struct

The types of interactions that people can perform with an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct InteractionTypes
```

## Topics

### Specifying types of interactions
- [static let automatic: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let textSelection: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/textselection.md)
  An option that enables text selection, copying, and translating.
- [static let dataDetectors: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/datadetectors.md)
  An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.
- [static let imageSubject: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/imagesubject.md)
  An option that enables people to use a long-press gesture on a subject in an image to separate it from the background.
- [static let visualLookUp: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.
- [static let automaticTextOnly: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes/automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.
### Creating an interaction
- [init(rawValue: UInt)](imageanalysisinteraction/interactiontypes/init(rawvalue:).md)
  Creates an instance from a raw type.
- [var rawValue: UInt](imageanalysisinteraction/interactiontypes/rawvalue.md)
  The corresponding value of the raw type.
### Managing sets
- [Set properties and methods](interactiontypes-set-properties-and-methods.md)
  The properties and methods that conform to the option set protocol.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var delegate: (any ImageAnalysisInteractionDelegate)?](imageanalysisinteraction/delegate.md)
  The delegate that handles the interaction callbacks.
- [var analysis: ImageAnalysis?](imageanalysisinteraction/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var view: UIView?](imageanalysisinteraction/view.md)
  The view that uses this interaction.
- [var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image.
- [var activeInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes)*