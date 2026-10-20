# ImageAnalysisOverlayView.InteractionTypes

**Framework**: VisionKit  
**Kind**: struct  
**Role**: Structure

The types of interactions that people can perform with an image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct InteractionTypes
```

## Topics

### Specifying types of interactions
- [static let automatic: ImageAnalysisOverlayView.InteractionTypes](./interactiontypes/automatic.md)
  An option that enables interaction with any type of text, symbols, or subjects that the framework recognizes.
- [static let textSelection: ImageAnalysisOverlayView.InteractionTypes](./interactiontypes/textselection.md)
  An option that enables text selection, copying, and translating.
- [static let dataDetectors: ImageAnalysisOverlayView.InteractionTypes](./interactiontypes/datadetectors.md)
  An option that enables interaction with text of certain formats, such as URLs, email addresses, and physical addresses.
- [static let imageSubject: ImageAnalysisOverlayView.InteractionTypes](./interactiontypes/imagesubject.md)
  An option that enables people to click or tap a subject in an image to separate it from the background.
- [static let visualLookUp: ImageAnalysisOverlayView.InteractionTypes](./interactiontypes/visuallookup.md)
  An option that presents a button for more information on any subjects the framework recognizes in the image.
- [static let automaticTextOnly: ImageAnalysisOverlayView.InteractionTypes](./interactiontypes/automatictextonly.md)
  An option that enables all interaction types except image subjects and Visual Look Up.
### Creating an interaction
- [init(rawValue: UInt)](./interactiontypes/init%28rawvalue%29.md)
  Creates an instance from a raw type.
- [var rawValue: UInt](./interactiontypes/rawvalue.md)
  The corresponding value of the raw type.
### Managing sets
- [Set properties and methods](../interactiontypes-set-properties-and-methods.md)
  The properties and methods that conform to the option set protocol.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring overlay views
- [var delegate: (any ImageAnalysisOverlayViewDelegate)?](./delegate.md)
  An object that handles image analysis interface callbacks.
- [var analysis: ImageAnalysis?](./analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [var trackingImageView: NSImageView?](./trackingimageview.md)
  The image view that contains the image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](./activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/interactiontypes)*