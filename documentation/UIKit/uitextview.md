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
- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

#### Overview

[`UITextView`](uitextview.md) supports the display of text using custom style information and also supports text editing. You typically use a text view to display multiple lines of text, such as when displaying the body of a large text document.

This class supports multiple text styles through use of the [`attributedText`](uitextview/attributedtext.md) property. (Styled text isn’t supported in versions of iOS earlier than iOS 6.) Setting a value for this property causes the text view to use the style information provided in the attributed string. You can still use the [`font`](uitextview/font.md), [`textColor`](uitextview/textcolor.md), and [`textAlignment`](uitextview/textalignment.md) properties to set style attributes, but those properties apply to all of the text in the text view. It’s recommended that you use a text view—and not a [`UIWebView`](uiwebview.md) object—to display both plain and rich text in your app.

##### Manage the Keyboard

When the user taps in an editable text view, that text view becomes the first responder and automatically asks the system to display the associated keyboard. Because the appearance of the keyboard has the potential to obscure portions of your user interface, it’s up to you to make sure that doesn’t happen by repositioning any views that might be obscured. Some system views, like table views, help you by scrolling the first responder into view automatically. If the first responder is at the bottom of the scrolling region, however, you may still need to resize or reposition the scroll view itself to ensure the first responder is visible.

It’s your application’s responsibility to dismiss the keyboard at the time of your choosing. You might dismiss the keyboard in response to a specific user action, such as the user tapping a particular button in your user interface. To dismiss the keyboard, send the [`resignFirstResponder()`](uiresponder/resignfirstresponder().md) message to the text view that’s currently the first responder. Doing so causes the text view object to end the current editing session (with the delegate object’s consent) and hide the keyboard.

The appearance of the keyboard itself can be customized using the properties provided by the [`UITextInputTraits`](uitextinputtraits.md) protocol. Text view objects implement this protocol and support the properties it defines. You can use these properties to specify the type of keyboard (ASCII, Numbers, URL, Email, and others) to display. You can also configure the basic text entry behavior of the keyboard, such as whether it supports automatic capitalization and correction of the text.

##### Keyboard Notifications

When the system shows or hides the keyboard, it posts several keyboard notifications. These notifications contain information about the keyboard, including its size, which you can use for calculations that involve repositioning or resizing views. Registering for these notifications is the only way to get some types of information about the keyboard. The system delivers the following notifications for keyboard-related events:

- [`keyboardWillShowNotification`](uiresponder/keyboardwillshownotification.md)
- [`keyboardDidShowNotification`](uiresponder/keyboarddidshownotification.md)
- [`keyboardWillHideNotification`](uiresponder/keyboardwillhidenotification.md)
- [`keyboardDidHideNotification`](uiresponder/keyboarddidhidenotification.md)

For more information about these notifications, see their descriptions in [`UIWindow`](uiwindow.md).

##### State Preservation

In iOS 6 and later, if you assign a value to this view’s [`restorationIdentifier`](uiview/restorationidentifier.md) property, it preserves the following information:

- The selected range of text, as reported by the [`selectedRange`](uitextview/selectedrange.md) property.
- The editing state of the text view, as reported by the [`isEditable`](uitextview/iseditable.md) property.

During the next launch cycle, the view attempts to restore these properties to their saved values. If the selection range can’t be applied to the text in the restored view, no text is selected. For more information about how state preservation and restoration works, see [`App Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

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
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](uitextview/texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](uitextview/drawtexthighlightbackground(for:origin:).md)
- [UITextView.BorderStyle](uitextview/borderstyle-swift.enum.md)
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
### Getting the writing tools status
- [var isWritingToolsActive: Bool](uitextview/iswritingtoolsactive.md)
  A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
### Accessing TextKit Objects
- [var textLayoutManager: NSTextLayoutManager?](uitextview/textlayoutmanager.md)
  The text layout manager that lays out text for the text view’s text container.
- [var layoutManager: NSLayoutManager](uitextview/layoutmanager.md)
  The layout manager that lays out text for the text view’s text container.
- [var textContainer: NSTextContainer](uitextview/textcontainer.md)
  The text container object that defines the area where text displays in the text view.
- [var textStorage: NSTextStorage](uitextview/textstorage.md)
  The text storage object holding the text that displays in the text view.
### Supporting state restoration
- [var interactionState: Any](uitextview/interactionstate.md)
### Structures
- [UITextView.TextDidBeginEditingMessage](uitextview/textdidbegineditingmessage.md)
- [UITextView.TextDidChangeMessage](uitextview/textdidchangemessage.md)
- [UITextView.TextDidEndEditingMessage](uitextview/textdidendeditingmessage.md)
### Instance Properties
- [var allowedWritingToolsResultOptions: UIWritingToolsResultOptions](uitextview/allowedwritingtoolsresultoptions.md)
- [var selectedRanges: [NSRange]](uitextview/selectedranges-70g3h.md)
- [var subclassForWritingToolsCoordinator: AnyClass](uitextview/subclassforwritingtoolscoordinator.md)
- [var textFormattingConfiguration: UITextFormattingViewController.Configuration?](uitextview/textformattingconfiguration.md)
- [var writingToolsBehavior: UIWritingToolsBehavior](uitextview/writingtoolsbehavior.md)
- [var writingToolsCoordinator: UIWritingToolsCoordinator](uitextview/writingtoolscoordinator.md)

## Relationships

### Inherits From
- [UIScrollView](uiscrollview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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