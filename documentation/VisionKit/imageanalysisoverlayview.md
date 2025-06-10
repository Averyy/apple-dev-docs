# ImageAnalysisOverlayView

**Framework**: VisionKit  
**Kind**: class

A view that enables people to interact with recognized text, barcodes, and other objects in an image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@objc final class ImageAnalysisOverlayView
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Overview

This class enables people to interact with specific content types ([`ImageAnalysisOverlayView.InteractionTypes`](imageanalysisoverlayview/interactiontypes.md)) that the framework identifies in an image. For example:

- The Live Text interface enables them to select any text present in the image ([`textSelection`](imageanalysisoverlayview/interactiontypes/textselection.md)), or invoke a URL ([`dataDetectors`](imageanalysisoverlayview/interactiontypes/datadetectors.md)). The text selection UI offers framework-standard buttons for copying selected text, or looking it up on the web for more information.
- The  feature identifies a wide variety of objects, or , in images with the [`imageSubject`](imageanalysisoverlayview/interactiontypes/imagesubject.md) interaction type, and provides your app with an image of the objects with the background removed. The [`visualLookUp`](imageanalysisoverlayview/interactiontypes/visuallookup.md) type supplements this feature by adding a button in the bottom corner of the view that people can click or tap for more information about the recognized subjects.

#### Configure the Interface and Begin Interaction

To connect the interface with an image that your app displays, add a new instance of this class as a subview to your app’s image view.

Choose the items that the framework recognizes in an image by configuring the  [`preferredInteractionTypes`](imageanalysisoverlayview/preferredinteractiontypes.md) property. To recognize all types of content, specify the [`automatic`](imageanalysisoverlayview/interactiontypes/automatic.md) option, or choose a combination of types by assigning an array:

```swift
overlayView.preferredInteractionTypes = [.textSelection, .imageSubject]
```

To begin interaction, call one of the [`ImageAnalyzer`](imageanalyzer.md) class’s `analyze` methods, such as [`analyze(_:configuration:)`](imageanalyzer/analyze(_:configuration:).md) and set the result onto this class’s [`analysis`](imageanalysisoverlayview/analysis.md) property.

You can take more control over the interaction or provide details about your app’s image view by implementing a delegate ([`ImageAnalysisInteractionDelegate`](imageanalysisinteractiondelegate.md)) and assigning it to the [`delegate`](imageanalysisinteraction/delegate.md) property. Your app needs to define the interactive area within the image either by setting the [`trackingImageView`](imageanalysisoverlayview/trackingimageview.md) property, or by implementing the delegate’s [`contentsRect(for:)`](imageanalysisoverlayviewdelegate/contentsrect(for:).md) method.

## Topics

### Creating overlay views
- [convenience init(any ImageAnalysisOverlayViewDelegate)](imageanalysisoverlayview/init(_:).md)
  Creates an overlay view with the specified delegate object.
- [init(frame: NSRect)](imageanalysisoverlayview/init(frame:).md)
  Creates an overlay view with the specified frame rectangle.
- [init?(coder: NSCoder)](imageanalysisoverlayview/init(coder:).md)
  Creates an overlay view from data in a coder object.
### Configuring overlay views
- [var delegate: (any ImageAnalysisOverlayViewDelegate)?](imageanalysisoverlayview/delegate.md)
  An object that handles image analysis interface callbacks.
- [var analysis: ImageAnalysis?](imageanalysisoverlayview/analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var preferredInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/preferredinteractiontypes.md)
  The types of interactions that people can perform with the image in this overlay view.
- [ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var trackingImageView: NSImageView?](imageanalysisoverlayview/trackingimageview.md)
  The image view that contains the image.
- [var activeInteractionTypes: ImageAnalysisOverlayView.InteractionTypes](imageanalysisoverlayview/activeinteractiontypes.md)
  The types of interactions that a person actively performs.
### Responding to view events
- [func viewDidMoveToSuperview()](imageanalysisoverlayview/viewdidmovetosuperview.md)
  Notifies your app when the view initially appears.
### Accessing text information
- [var text: String](imageanalysisoverlayview/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisoverlayview/selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](imageanalysisoverlayview/selectedattributedtext.md)
  The current selected attributed text.
- [var hasActiveTextSelection: Bool](imageanalysisoverlayview/hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisoverlayview/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasText(at: CGPoint) -> Bool](imageanalysisoverlayview/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisoverlayview/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.
### Managing text selection
- [var selectedRanges: [Range<String.Index>]](imageanalysisoverlayview/selectedranges.md)
  The current selected ranges.
- [func resetSelection()](imageanalysisoverlayview/resetselection.md)
  Removes a person’s text selection from the interface.
### Accessing image subjects
- [var subjects: Set<ImageAnalysisOverlayView.Subject>](imageanalysisoverlayview/subjects.md)
  The set of all subjects the framework identifies in an image.
- [ImageAnalysisOverlayView.Subject](imageanalysisoverlayview/subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisOverlayView.Subject>) async throws -> NSImage](imageanalysisoverlayview/image(for:).md)
  Provides an image asynchronously that contains the given subjects with the background removed.
- [func subject(at: CGPoint) async -> ImageAnalysisOverlayView.Subject?](imageanalysisoverlayview/subject(at:).md)
  Returns the subject at the given point within the overlay view’s image, if one exists.
### Managing image subjects
- [func beginSubjectAnalysisIfNecessary()](imageanalysisoverlayview/beginsubjectanalysisifnecessary.md)
  Begins subject analysis on the overlay view’s image.
- [var highlightedSubjects: Set<ImageAnalysisOverlayView.Subject>](imageanalysisoverlayview/highlightedsubjects.md)
  All highlighted subjects in the overlay view’s image.
### Querying the interface state
- [var liveTextButtonVisible: Bool](imageanalysisoverlayview/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](imageanalysisoverlayview/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisoverlayview/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisoverlayview/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisoverlayview/selectableitemshighlighted.md)
  A Boolean value that indicates whether the overlay view highlights actionable text or data that the analyzer detects in text.
### Customizing the interface
- [func setSupplementaryInterfaceHidden(Bool, animated: Bool)](imageanalysisoverlayview/setsupplementaryinterfacehidden(_:animated:).md)
  Hides or shows supplementary interface objects, such as the Live Text button and the interface for Quick Actions, depending on the item type.
- [var supplementaryInterfaceContentInsets: NSEdgeInsets](imageanalysisoverlayview/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [var supplementaryInterfaceFont: NSFont?](imageanalysisoverlayview/supplementaryinterfacefont.md)
  The font to use for the supplementary interface.
- [ImageAnalysisOverlayView.MenuTag](imageanalysisoverlayview/menutag.md)
  Tags that enable your app to manage image-analysis context menu items.
### Managing custom image views
- [var contentsRect: CGRect](imageanalysisoverlayview/contentsrect.md)
  Returns the rectangle, in unit coordinates, that contains the image within the superview.
- [func setContentsRectNeedsUpdate()](imageanalysisoverlayview/setcontentsrectneedsupdate.md)
  Informs the view that contains the image when the layout changes and the view needs to reload its content.
### Errors
- [ImageAnalysisOverlayView.SubjectUnavailable](imageanalysisoverlayview/subjectunavailable.md)
  Error conditions that can occur during subject analysis.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalyzer](imageanalyzer.md)
  An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [class ImageAnalysisInteraction](imageanalysisinteraction.md)
  An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisInteractionDelegate](imageanalysisinteractiondelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- [protocol ImageAnalysisOverlayViewDelegate](imageanalysisoverlayviewdelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an overlay view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview)*