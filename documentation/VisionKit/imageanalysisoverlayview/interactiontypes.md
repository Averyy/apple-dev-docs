# ImageAnalysisOverlayView.InteractionTypes

**Framework**: VisionKit  
**Kind**: struct

The types of interactions that people can perform with an image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct InteractionTypes
```

## Topics

### Specifying types of interactions
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
- [static let automaticTextOnly: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes/automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.
### Creating an interaction
- [init(rawValue: UInt)](imageanalysisoverlayview/interactiontypes/init(rawvalue:).md)
  Creates an instance from a raw type.
- [var rawValue: UInt](imageanalysisoverlayview/interactiontypes/rawvalue.md)
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

- [var delegate: (any ImageAnalysisOverlayViewDelegate)?](imageanalysisoverlayview/delegate.md)
  An object that handles image analysis interface callbacks.
- [var analysis: ImageAnalysis?](imageanalysisoverlayview/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [var trackingImageView: NSImageView?](imageanalysisoverlayview/trackingimageview.md)
  The image view that contains the image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/interactiontypes)*