# ImageAnalysisInteraction

**Framework**: VisionKit  
**Kind**: class

An interface that enables people to interact with recognized text, barcodes, and other objects in an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc final class ImageAnalysisInteraction
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Overview

This class enables people to interact with specific content types ([`ImageAnalysisInteraction.InteractionTypes`](imageanalysisinteraction/interactiontypes.md)) that the framework identifies in an image. For example:

- The Live Text interface enables them to select any text present in the image ([`textSelection`](imageanalysisinteraction/interactiontypes/textselection.md)), or invoke a URL ([`dataDetectors`](imageanalysisinteraction/interactiontypes/datadetectors.md)). The text selection UI offers framework-standard buttons for copying selected text, or looking it up on the web for more information.
- The  feature identifies a wide variety of objects, or , in images with the [`imageSubject`](imageanalysisinteraction/interactiontypes/imagesubject.md) interaction type, and provides your app with an image of the objects with the background removed. The [`visualLookUp`](imageanalysisinteraction/interactiontypes/visuallookup.md) type supplements this feature by adding a button in the bottom corner of the view that people can click or tap for more information about the recognized subjects.

#### Configure the Interface and Begin Interaction

This class conforms to the [`UIInteraction`](https://developer.apple.com/documentation/UIKit/UIInteraction) protocol. To connect the interface with an image that your app displays, call [`addInteraction(_:)`](https://developer.apple.com/documentation/UIKit/UIView/addInteraction(_:)) on your app’s image view and pass in a new instance of this class.

Choose the items that the framework recognizes in an image by configuring the  [`preferredInteractionTypes`](imageanalysisinteraction/preferredinteractiontypes.md) property. To recognize all types of content, specify the [`automatic`](imageanalysisinteraction/interactiontypes/automatic.md) option, or choose a combination of types by assigning an array:

```swift
interaction.preferredInteractionTypes = [.textSelection, .imageSubject]
```

To begin interaction, call one of the [`ImageAnalyzer`](imageanalyzer.md) class’s `analyze` methods, such as [`analyze(_:configuration:)`](imageanalyzer/analyze(_:configuration:).md) and set the result onto this class’s [`analysis`](imageanalysisoverlayview/analysis.md) property.

You can take more control over the interaction or provide details about your app’s image view by implementing a delegate ([`ImageAnalysisInteractionDelegate`](imageanalysisinteractiondelegate.md)) and assigning it to the [`delegate`](imageanalysisinteraction/delegate.md) property. If your image view isn’t an instance of [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView), your app needs to define the interactive area within the image by implementing the [`contentsRect(for:)`](imageanalysisinteractiondelegate/contentsrect(for:).md) method.

## Topics

### Creating an image interaction
- [init()](imageanalysisinteraction/init.md)
  Creates an interaction for Live Text actions with items in an image.
- [convenience init(any ImageAnalysisInteractionDelegate)](imageanalysisinteraction/init(_:).md)
  Creates an interaction for Live Text actions with the specified delegate.
### Configuring an image interaction
- [var delegate: (any ImageAnalysisInteractionDelegate)?](imageanalysisinteraction/delegate.md)
  The delegate that handles the interaction callbacks.
- [var analysis: ImageAnalysis?](imageanalysisinteraction/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var view: UIView?](imageanalysisinteraction/view.md)
  The view that uses this interaction.
- [var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image.
- [ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var activeInteractionTypes: ImageAnalysisInteraction.InteractionTypes](imageanalysisinteraction/activeinteractiontypes.md)
  The types of interactions that a person actively performs.
### Responding to view events
- [func willMove(to: UIView?)](imageanalysisinteraction/willmove(to:).md)
  Performs an action before the view adds or removes the interaction from its interaction array.
- [func didMove(to: UIView?)](imageanalysisinteraction/didmove(to:).md)
  Performs an action after the view adds or removes the interaction from its interaction array.
### Accessing text information
- [var text: String](imageanalysisinteraction/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisinteraction/selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](imageanalysisinteraction/selectedattributedtext.md)
  The current selected attributed text.
- [func hasText(at: CGPoint) -> Bool](imageanalysisinteraction/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [var hasActiveTextSelection: Bool](imageanalysisinteraction/hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisinteraction/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisinteraction/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.
### Managing text selection
- [var selectedRanges: [Range<String.Index>]](imageanalysisinteraction/selectedranges.md)
  Sets selected text ranges.
- [func resetTextSelection()](imageanalysisinteraction/resettextselection.md)
  Removes a person’s text selection from the interface.
### Accessing image subjects
- [var subjects: Set<ImageAnalysisInteraction.Subject>](imageanalysisinteraction/subjects.md)
  The set of all subjects the framework identifies in an image.
- [ImageAnalysisInteraction.Subject](imageanalysisinteraction/subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisInteraction.Subject>) async throws -> UIImage](imageanalysisinteraction/image(for:).md)
  Provides an image asynchronously that contains the given subjects with the background removed.
- [func subject(at: CGPoint) async -> ImageAnalysisInteraction.Subject?](imageanalysisinteraction/subject(at:).md)
  Returns the subject at the given point within the interaction’s image, if one exists.
### Managing image subjects
- [var highlightedSubjects: Set<ImageAnalysisInteraction.Subject>](imageanalysisinteraction/highlightedsubjects.md)
  All highlighted subjects in the interaction image.
### Querying the interface state
- [var liveTextButtonVisible: Bool](imageanalysisinteraction/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](imageanalysisinteraction/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisinteraction/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisinteraction/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisinteraction/selectableitemshighlighted.md)
  A Boolean value that indicates whether the interaction highlights actionable text or data the analyzer detects in text.
### Customizing the interface
- [var allowLongPressForDataDetectorsInTextMode: Bool](imageanalysisinteraction/allowlongpressfordatadetectorsintextmode.md)
  A Boolean value that indicates whether people can press and hold text to activate data detectors.
- [func setSupplementaryInterfaceHidden(Bool, animated: Bool)](imageanalysisinteraction/setsupplementaryinterfacehidden(_:animated:).md)
  Hides or shows supplementary interface objects, such as the Live Action button and Quick Actions, depending on the item type.
- [var supplementaryInterfaceContentInsets: UIEdgeInsets](imageanalysisinteraction/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [var supplementaryInterfaceFont: UIFont?](imageanalysisinteraction/supplementaryinterfacefont.md)
  The font to use for the supplementary interface.
### Managing custom image views
- [var contentsRect: CGRect](imageanalysisinteraction/contentsrect.md)
  A rectangle, in unit coordinate space, that describes the content area of the interaction.
- [func setContentsRectNeedsUpdate()](imageanalysisinteraction/setcontentsrectneedsupdate.md)
  Informs the view that contains the image when the layout changes and the view needs to reload its content.
### Errors
- [ImageAnalysisInteraction.SubjectUnavailable](imageanalysisinteraction/subjectunavailable.md)
  Error conditions that can occur during subject analysis.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIInteraction](../UIKit/UIInteraction.md)

## See Also

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalyzer](imageanalyzer.md)
  An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [protocol ImageAnalysisInteractionDelegate](imageanalysisinteractiondelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- [class ImageAnalysisOverlayView](imageanalysisoverlayview.md)
  A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisOverlayViewDelegate](imageanalysisoverlayviewdelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an overlay view.
- [struct CameraRegionView](cameraregionview.md)
  This view displays a stabilized region of interest within a person’s view and provides passthrough camera feed for that selected region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction)*