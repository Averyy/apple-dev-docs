# UITextView

**Framework**: UIKit  
**Kind**: class

A scrollable, multiline text region.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextView
```

## Mentions

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md)
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)
- [About app development with UIKit](about-app-development-with-uikit.md)
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md)
- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)
- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Overview

A text view displays multiple lines of text and supports editing, custom styles, and rich formatting. Use it when you need to display or edit a body of text, such as the contents of a document.

For rich text, set the [`attributedText`](uitextview/attributedtext.md) property to provide per-range style information. You can also use [`font`](uitextview/font.md), [`textColor`](uitextview/textcolor.md), and [`textAlignment`](uitextview/textalignment.md) to apply a single style across all text in the view.

##### Manage the Keyboard

When someone taps in an editable text view, it becomes the first responder and the system displays the keyboard. Because the keyboard can obscure parts of your interface, reposition any views that would otherwise be hidden. Some system views, like table views, scroll the first responder into view automatically. If the first responder is at the bottom of the scrolling region, you may still need to resize or reposition the scroll view to keep it visible.

Your app is responsible for dismissing the keyboard. Dismiss it in response to a user action, such as tapping a Done button. To dismiss the keyboard, call [`resignFirstResponder()`](uiresponder/resignfirstresponder().md) on the text view that’s currently the first responder. This ends the editing session and hides the keyboard, with your delegate’s consent.

To customize the keyboard, use the properties from the [`UITextInputTraits`](uitextinputtraits.md) protocol, which text views implement. You can set the keyboard type (ASCII, Numbers, URL, Email, and others) and configure text entry behavior like autocapitalization and autocorrection.

##### Keyboard Notifications

When the system shows or hides the keyboard, it posts notifications that include the keyboard’s size and position. Register for these notifications to reposition or resize views as needed:

- [`keyboardWillShowNotification`](uiresponder/keyboardwillshownotification.md)
- [`keyboardDidShowNotification`](uiresponder/keyboarddidshownotification.md)
- [`keyboardWillHideNotification`](uiresponder/keyboardwillhidenotification.md)
- [`keyboardDidHideNotification`](uiresponder/keyboarddidhidenotification.md)

For more information about these notifications, see [`UIWindow`](uiwindow.md).

##### State Preservation

If you assign a value to this view’s [`restorationIdentifier`](uiview/restorationidentifier.md) property, the view preserves the following information:

- The selected range of text.
- The editing state of the text view, as reported by the [`isEditable`](uitextview/iseditable.md) property.

On the next launch, the view restores these properties. If the saved selection range doesn’t apply to the current text, no text is selected.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/content/text-views/).

## Topics

### Initializing the text view
- [init(frame: CGRect, textContainer: NSTextContainer?)](uitextview/init(frame:textcontainer:).md)
  Creates a new text view with the specified text container.
- [convenience init(usingTextLayoutManager: Bool)](uitextview/init(usingtextlayoutmanager:).md)
  Creates a new text view, with or without a text layout manager depending on the Boolean value you specify.
- [init?(coder: NSCoder)](uitextview/init(coder:).md)
  Creates a text view from data in an unarchiver.
### Specifying the text content
- [var text: String!](uitextview/text.md)
  The text that the text view displays.
- [var attributedText: NSAttributedString!](uitextview/attributedtext.md)
  The styled text that the text view displays.
### Responding to text view changes
- [var delegate: (any UITextViewDelegate)?](uitextview/delegate.md)
  The text view’s delegate.
- [protocol UITextViewDelegate](uitextviewdelegate.md)
  The methods for receiving editing-related messages for text view objects.
### Configuring appearance attributes
- [var font: UIFont?](uitextview/font.md)
  The font of the text.
- [var textColor: UIColor?](uitextview/textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](uitextview/textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]](uitextview/typingattributes.md)
  The attributes to apply to new text that the user enters.
- [var linkTextAttributes: [NSAttributedString.Key : Any]!](uitextview/linktextattributes.md)
  The attributes to apply to links.
- [var borderStyle: UITextView.BorderStyle](uitextview/borderstyle-swift.property.md)
  The border style for the text field.
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](uitextview/texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](uitextview/drawtexthighlightbackground(for:origin:).md)
- [UITextView.BorderStyle](uitextview/borderstyle-swift.enum.md)
  The type of border around the text view.
### Configuring layout attributes
- [var textContainerInset: UIEdgeInsets](uitextview/textcontainerinset.md)
  The inset of the text container’s layout area within the text view’s content area.
- [var usesStandardTextScaling: Bool](uitextview/usesstandardtextscaling.md)
  A Boolean value that determines the rendering scale of the text.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
### Formatting special data in text
- [var dataDetectorTypes: UIDataDetectorTypes](uitextview/datadetectortypes.md)
  The types of data that convert to tappable URLs in the text view.
- [struct UIDataDetectorTypes](uidatadetectortypes.md)
  Constants that define the types of information to detect in text-based content.
### Managing the editing behavior
- [var isEditable: Bool](uitextview/iseditable.md)
  A Boolean value that indicates whether the text view is editable.
- [var allowsEditingTextAttributes: Bool](uitextview/allowseditingtextattributes.md)
  A Boolean value that indicates whether the text view allows the user to edit style information.
- [class let textDidBeginEditingNotification: NSNotification.Name](uitextview/textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text view.
- [class let textDidChangeNotification: NSNotification.Name](uitextview/textdidchangenotification.md)
  A notification that alerts observers when the text in a text view changes.
- [class let textDidEndEditingNotification: NSNotification.Name](uitextview/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text view.
### Working with the selection
- [var selectedRange: NSRange](uitextview/selectedrange.md)
  The current selection range of the text view.
- [func scrollRangeToVisible(NSRange)](uitextview/scrollrangetovisible(_:).md)
  Scrolls the text view until the text in the specified range is visible.
- [var clearsOnInsertion: Bool](uitextview/clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.
- [var isSelectable: Bool](uitextview/isselectable.md)
  A Boolean value that indicates whether the text view is selectable.
### Replacing the system input views
- [var inputView: UIView?](uitextview/inputview.md)
  The custom input view to display when the text view becomes the first responder.
- [var inputAccessoryView: UIView?](uitextview/inputaccessoryview.md)
  The custom accessory view to display when the text view becomes the first responder.
### Supporting Find and Replace
- [var isFindInteractionEnabled: Bool](uitextview/isfindinteractionenabled.md)
  A Boolean value that enables a text view’s built-in find interaction.
- [var findInteraction: UIFindInteraction?](uitextview/findinteraction.md)
  The text view’s built-in find interaction.
### Getting the Writing Tools configuration
- [var writingToolsBehavior: UIWritingToolsBehavior](uitextview/writingtoolsbehavior.md)
  The level of Writing Tools support to use in the text view.
- [var allowedWritingToolsResultOptions: UIWritingToolsResultOptions](uitextview/allowedwritingtoolsresultoptions.md)
  The type of content Writing Tools generates for your text view.
- [var isWritingToolsActive: Bool](uitextview/iswritingtoolsactive.md)
  A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [var writingToolsCoordinator: UIWritingToolsCoordinator](uitextview/writingtoolscoordinator.md)
  The object that coordinates interactions between Writing Tools and the text view.
- [var subclassForWritingToolsCoordinator: AnyClass](uitextview/subclassforwritingtoolscoordinator.md)
### Accessing TextKit Objects
- [var textLayoutManager: NSTextLayoutManager?](uitextview/textlayoutmanager.md)
  The text layout manager that lays out text for the text view’s text container.
- [var layoutManager: NSLayoutManager](uitextview/layoutmanager.md)
  The layout manager that lays out text for the text view’s text container.
- [var textContainer: NSTextContainer](uitextview/textcontainer.md)
  The text container object that defines the area where text displays in the text view.
- [var textStorage: NSTextStorage](uitextview/textstorage.md)
  The text storage object holding the text that displays in the text view.
### Customizing viewport layout
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](uitextview/viewportbounds(for:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls to request the current viewport, which is the view visible bounds plus the overdraw area. Requires a call to super.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](uitextview/textviewportlayoutcontrollerwilllayout(_:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller starts its layout process. Requires a call to super.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](uitextview/textviewportlayoutcontrollerdidlayout(_:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller finishes its layout process. Requires a call to super.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](uitextview/textviewportlayoutcontrollerreceivedsetneedslayout(_:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller receives a `setNeedsLayout` call. Requires a call to super.
### Managing attachment view reuse
- [func register(UITextAttachmentViewProviderReusePolicy, forTextAttachmentViewProviderType: AnyClass)](uitextview/register(_:fortextattachmentviewprovidertype:).md)
  Register the UITextAttachmentViewProviderReusePolicy for all instances of a particular subclass of NSTextAttachmentViewProvider.
- [struct UITextAttachmentViewProviderReusePolicy](uitextattachmentviewproviderreusepolicy.md)
  An option set that controls whether a text view reuses attachment view providers when scrolling or editing.
### Supporting state restoration
- [var interactionState: Any](uitextview/interactionstate.md)
### Structures
- [UITextView.TextDidBeginEditingMessage](uitextview/textdidbegineditingmessage.md)
- [UITextView.TextDidChangeMessage](uitextview/textdidchangemessage.md)
- [UITextView.TextDidEndEditingMessage](uitextview/textdidendeditingmessage.md)
### Instance Properties
- [var selectedRanges: [NSRange]](uitextview/selectedranges-70g3h.md)
- [var textFormattingConfiguration: UITextFormattingViewController.Configuration?](uitextview/textformattingconfiguration.md)
  For text views that have flag `allowsEditingTextAttributes` set, this configuration will be used for `UITextFormattingViewController` when its presentation is requested.
### Instance Methods
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](uitextview/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the layout controller lays out a text layout fragment in the UI. Requires a call to super.

## Relationships

### Inherits From
- [UIScrollView](uiscrollview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTextViewportLayoutControllerDelegate](nstextviewportlayoutcontrollerdelegate.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFindInteractionDelegate](uifindinteractiondelegate.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
- [UIKeyInput](uikeyinput.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UILetterformAwareAdjusting](uiletterformawareadjusting.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITextDraggable](uitextdraggable.md)
- [UITextDroppable](uitextdroppable.md)
- [UITextInput](uitextinput.md)
- [UITextInputTraits](uitextinputtraits.md)
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
- [UITextSearching](uitextsearching-3wkjv.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UILabel](uilabel.md)
  A view that displays one or more lines of informational text.
- [class UITextField](uitextfield.md)
  An object that displays an editable text area in your interface.
- [Drag and drop customization](drag-and-drop-customization.md)
  Extend the standard drag and drop support for text views to include custom types of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview)*