# UITextInput

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods for interacting with the text input system and enabling features in documents.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UITextInput : UIKeyInput
```

```objc
@protocol UITextInput <UIKeyInput>
```

## Mentions

- [Adopting system selection UI in custom text views](./adopting-system-selection-ui-in-custom-text-views.md)
- [Adopting Smart Reply in your messaging or email app](./adopting-smart-reply-in-your-messaging-or-email-app.md)

#### Overview

Objects that adopt the [`UITextInput`](./uitextinput.md) protocol maintain information about text input and provide that information to the text input system on demand. A [`UITextInput`](./uitextinput.md) object interacts with the text input system by:

- Reporting text positions and text ranges
- Responding to queries layout and writing direction
- Performing hit-testing — returning text positions and ranges for a specific point
- Providing the system with rectangles for highlighting ranges of text and drawing the *caret*, a glyph that represents the insertion point during text entry

In addition, a [`UITextInput`](./uitextinput.md) object maintains ranges for selected text and marked text. Marked text, a part of multistage text input, represents provisionally inserted text that the user has yet to confirm. The range of marked text always contains a range of selected text, which might be a range of characters or the caret. Multistage text input is a requirement when the language is ideographic and the keyboard is phonetic.

##### Integrate with the text input system

The [`UITextInput`](./uitextinput.md) protocol works with other classes and protocols to integrate text-processing apps with the text input system:

- **[`UITextPosition`](./uitextposition.md) and [`UITextRange`](./uitextrange.md) classes**: All [`UITextInput`](./uitextinput.md)-conforming document classes must create custom subclasses of these classes. A [`UITextPosition`](./uitextposition.md) object represents a position in a text container. A [`UITextRange`](./uitextrange.md) object, which encapsulates beginning and ending [`UITextPosition`](./uitextposition.md) objects, represents a range of characters in the text container.
- **[`UITextInputTokenizer`](./uitextinputtokenizer.md) protocol and [`UITextInputStringTokenizer`](./uitextinputstringtokenizer.md) class**: The [`UITextInputTokenizer`](./uitextinputtokenizer.md) protocol defines an interface for tokenizing input text. The [`UITextInputStringTokenizer`](./uitextinputstringtokenizer.md) class is a default implementation of this protocol.
- **[`UITextInputDelegate`](./uitextinputdelegate.md) protocol**: The text input system automatically assigns its own text input delegate (which conforms to this protocol) to the [`UITextInput`](./uitextinput.md)-conforming document object. This text input delegate allows document objects to inform the input system of changes in text and selection.
- **[`UIKeyInput`](./uikeyinput.md) protocol**: Implement this protocol to allow text entry and deletion at an insertion point.

##### Customize keyboard behavior

The [`UITextInput`](./uitextinput.md) protocol also inherits the [`UITextInputTraits`](./uitextinputtraits.md) protocol, which provides customization of the keyboard and its behaviors.

When the user chooses dictation input on a supported device, the system automatically inserts recognized phrases into the current text view. Methods in the [`UITextInput`](./uitextinput.md) protocol allow your app to respond to the completion of dictation. You can use an object of the [`UIDictationPhrase`](./uidictationphrase.md) class to obtain a string that represents a phrase the user dictates. In the case of ambiguous dictation results, a dictation phrase object provides an array that contains alternative strings.

## Topics

### Handling text input
- [var inputDelegate: (any UITextInputDelegate)?](./uitextinput/inputdelegate.md)
  An input delegate that receives a notification when text changes or when the selection changes.
- [protocol UITextInputDelegate](./uitextinputdelegate.md)
  An intermediary between a document and the text input system.
### Replacing and returning text
- [func text(in: UITextRange) -> String?](./uitextinput/text%28in%29.md)
  Returns the text in the specified range.
- [func replace(UITextRange, withText: String)](./uitextinput/replace%28_,withtext%29.md)
  Replaces the text in a document that is in the specified range.
- [func shouldChangeText(in: UITextRange, replacementText: String) -> Bool](./uitextinput/shouldchangetext%28in,replacementtext%29.md)
  Asks whether to replace the text in the specified range.
### Working with marked and selected text
- [var selectedTextRange: UITextRange?](./uitextinput/selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextRange: UITextRange?](./uitextinput/markedtextrange.md)
  The range of currently marked text in a document.
- [var markedTextStyle: [NSAttributedString.Key : Any]?](./uitextinput/markedtextstyle.md)
  A dictionary of attributes that describes how to draw marked text.
- [func setMarkedText(String?, selectedRange: NSRange)](./uitextinput/setmarkedtext%28_,selectedrange%29.md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](./uitextinput/setattributedmarkedtext%28_,selectedrange%29.md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](./uitextinput/unmarktext%28%29.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](./uitextinput/selectionaffinity.md)
  The desired location for the insertion point.
### Computing text ranges and text positions
- [func textRange(from: UITextPosition, to: UITextPosition) -> UITextRange?](./uitextinput/textrange%28from,to%29.md)
  Returns the range between two text positions.
- [func position(from: UITextPosition, offset: Int) -> UITextPosition?](./uitextinput/position%28from,offset%29.md)
  Returns the text position at a specified offset from another text position.
- [func position(from: UITextPosition, in: UITextLayoutDirection, offset: Int) -> UITextPosition?](./uitextinput/position%28from,in,offset%29.md)
  Returns the text position at a specified offset in a specified direction from another text position.
- [var beginningOfDocument: UITextPosition](./uitextinput/beginningofdocument.md)
  The text position for the beginning of a document.
- [var endOfDocument: UITextPosition](./uitextinput/endofdocument.md)
  The text position for the end of a document.
### Evaluating text positions
- [func compare(UITextPosition, to: UITextPosition) -> ComparisonResult](./uitextinput/compare%28_,to%29.md)
  Returns how one text position compares to another text position.
- [func offset(from: UITextPosition, to: UITextPosition) -> Int](./uitextinput/offset%28from,to%29.md)
  Returns the number of UTF-16 characters between one text position and another text position.
### Making the view non-editable
- [var isEditable: Bool](./uitextinput/iseditable.md)
  A Boolean value that indicates whether the text view contains editable text.
### Determining layout and writing direction
- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](./uitextinput/position%28within,farthestin%29.md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](./uitextinput/characterrange%28byextending,in%29.md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](./uitextinput/basewritingdirection%28for,in%29.md)
  Returns the base writing direction for a position in the text going in a certain direction.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](./uitextinput/setbasewritingdirection%28_,for%29.md)
  Sets the base writing direction for a specified range of text in a document.
- [typealias UITextWritingDirection](./uitextwritingdirection.md)
  The writing direction of the text for the language.
### Working with geometry and hit-testing
- [func firstRect(for: UITextRange) -> CGRect](./uitextinput/firstrect%28for%29.md)
  Returns the first rectangle that encloses a range of text in a document.
- [func closestPosition(to: CGPoint) -> UITextPosition?](./uitextinput/closestposition%28to%29.md)
  Returns the position in a document that is closest to a specified point.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](./uitextinput/selectionrects%28for%29.md)
  Returns an array of selection rects corresponding to the range of text.
- [func closestPosition(to: CGPoint, within: UITextRange) -> UITextPosition?](./uitextinput/closestposition%28to,within%29.md)
  Returns the position in a document that is closest to a specified point in a specified range.
- [func characterRange(at: CGPoint) -> UITextRange?](./uitextinput/characterrange%28at%29.md)
  Returns the character or range of characters that is at a specified point in a document.
### Providing the caret layout information
- [func caretRect(for: UITextPosition) -> CGRect](./uitextinput/caretrect%28for%29.md)
  Returns a rectangle to draw the caret at a specified insertion point.
- [func caretTransform(for: UITextPosition) -> CGAffineTransform](./uitextinput/carettransform%28for%29.md)
  Returns the transform to apply to the caret prior to drawing.
### Tokenizing input text
- [var tokenizer: any UITextInputTokenizer](./uitextinput/tokenizer.md)
  An input tokenizer that provides information about the granularity of text units.
- [protocol UITextInputTokenizer](./uitextinputtokenizer.md)
  A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.
### Managing the floating cursor
- [func beginFloatingCursor(at: CGPoint)](./uitextinput/beginfloatingcursor%28at%29.md)
  Tells the object when the gesture that the system uses to manipulate the cursor begins.
- [func updateFloatingCursor(at: CGPoint)](./uitextinput/updatefloatingcursor%28at%29.md)
  Tells the object that the floating cursor moved to a new location.
- [func endFloatingCursor()](./uitextinput/endfloatingcursor%28%29.md)
  Tells the object when the gesture that the system uses to manipulate the cursor ends.
### Using dictation
- [func dictationRecordingDidEnd()](./uitextinput/dictationrecordingdidend%28%29.md)
  Tells the object when there is a pending dictation result.
- [func dictationRecognitionFailed()](./uitextinput/dictationrecognitionfailed%28%29.md)
  Tells the object when dictation ends, but recognition fails.
- [func insertDictationResult([UIDictationPhrase])](./uitextinput/insertdictationresult%28_%29.md)
  Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [var insertDictationResultPlaceholder: Any](./uitextinput/insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](./uitextinput/frame%28fordictationresultplaceholder%29.md)
  Asks for the rectangle for displaying the dictation placeholder animation.
- [func removeDictationResultPlaceholder(Any, willInsertResult: Bool)](./uitextinput/removedictationresultplaceholder%28_,willinsertresult%29.md)
  Tells the view that the specified placeholder object is unnecessary.
### Managing placeholders
- [func insertTextPlaceholder(with: CGSize) -> UITextPlaceholder](./uitextinput/inserttextplaceholder%28with%29.md)
  Inserts a placeholder object to reserve visual space during text input.
- [func remove(UITextPlaceholder)](./uitextinput/remove%28_%29.md)
  Removes a placeholder object from the text input view.
- [class UITextPlaceholder](./uitextplaceholder.md)
  A placeholder object that reserves visual space in a text input view.
### Managing the edit menu
- [func editMenu(for: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./uitextinput/editmenu%28for,suggestedactions%29.md)
  Asks for the menu to display for the given text range and actions the system provides.
- [func willPresentEditMenu(animator: any UIEditMenuInteractionAnimating)](./uitextinput/willpresenteditmenu%28animator%29.md)
  Tells the object when the system is about to present an edit menu with an animator.
- [func willDismissEditMenu(animator: any UIEditMenuInteractionAnimating)](./uitextinput/willdismisseditmenu%28animator%29.md)
  Tells the object when the system is about to dismiss an edit menu with an animator.
### Supporting text-phrase alternatives
- [func insertText(String, alternatives: [String], style: UITextAlternativeStyle)](./uitextinput/inserttext%28_,alternatives,style%29.md)
- [enum UITextAlternativeStyle](./uitextalternativestyle.md)
  A constant that determines if the system highlights alternative phrases during text input.
### Inserting a Smart Reply suggestion
- [func insert(UIInputSuggestion)](./uitextinput/insert%28_%29.md)
  Inserts the user or system’s input suggestion into the document.
### Supporting adaptive images
- [var supportsAdaptiveImageGlyph: Bool](./uitextinput/supportsadaptiveimageglyph.md)
  A Boolean value that indicates whether the document supports adaptive images in the input.
- [func insert(NSAdaptiveImageGlyph, replacementRange: UITextRange)](./uitextinput/insert%28_,replacementrange%29.md)
  Inserts an adaptive image into the text at the specifed location.
### Returning text-styling information
- [func textStyling(at: UITextPosition, in: UITextStorageDirection) -> [NSAttributedString.Key : Any]?](./uitextinput/textstyling%28at,in%29.md)
  Returns a dictionary with properties that specify how to style the text at a certain location in a document.
### Reconciling text position and character offset
- [func position(within: UITextRange, atCharacterOffset: Int) -> UITextPosition?](./uitextinput/position%28within,atcharacteroffset%29.md)
  Returns the position within a range of a document’s text that corresponds to the character offset from the start of that range.
- [func characterOffset(of: UITextPosition, within: UITextRange) -> Int](./uitextinput/characteroffset%28of,within%29.md)
  Returns the character offset of a position in a document’s text that falls within a specified range.
### Returning the text input view
- [var textInputView: UIView](./uitextinput/textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in the protocol.
### Constants
- [struct UITextDirection](./uitextdirection.md)
  The direction of the text.
- [enum UITextStorageDirection](./uitextstoragedirection.md)
  The direction of text storage.
- [enum UITextLayoutDirection](./uitextlayoutdirection.md)
  The direction of text layout.
### Deprecated
- [Style dictionary keys](./style-dictionary-keys.md)
  A dictionary that contains properties that define text style characteristics.
### Instance Properties
- [var unobscuredContentRect: CGRect](./uitextinput/unobscuredcontentrect.md)
  The visible content region, excluding parts covered by view-specific UI.
### Instance Methods
- [func attributedText(in: UITextRange) -> NSAttributedString](./uitextinput/attributedtext%28in%29.md)
- [func didDismissWritingTools()](./uitextinput/diddismisswritingtools%28%29.md)
- [func insertAttributedText(NSAttributedString)](./uitextinput/insertattributedtext%28_%29.md)
- [func replace(UITextRange, withAttributedText: NSAttributedString)](./uitextinput/replace%28_,withattributedtext%29.md)
- [func willPresentWritingTools()](./uitextinput/willpresentwritingtools%28%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIKeyInput](./uikeyinput.md)
- [UITextInputTraits](./uitextinputtraits.md)
### Inherited By
- [UITextDraggable](./uitextdraggable.md)
- [UITextDroppable](./uitextdroppable.md)
### Conforming Types
- [UISearchTextField](./uisearchtextfield.md)
- [UITextField](./uitextfield.md)
- [UITextView](./uitextview.md)

## See Also

### Text input
- [protocol UITextInputDelegate](./uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](./uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [protocol UITextInputTraits](./uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputContext](./uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputMode](./uitextinputmode.md)
  The current text input mode.
- [class UITextInputAssistantItem](./uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [class UIDictationPhrase](./uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput)*