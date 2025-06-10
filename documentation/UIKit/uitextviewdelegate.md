# UITextViewDelegate

**Framework**: UIKit  
**Kind**: protocol

The methods for receiving editing-related messages for text view objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITextViewDelegate : UIScrollViewDelegate
```

#### Overview

All of the methods in this protocol are optional. You can use them in situations where you might want to adjust the text a user is editing (such as in the case of a spell-checker program) or to modify the intended insertion point.

## Topics

### Responding to editing notifications
- [func textViewShouldBeginEditing(UITextView) -> Bool](uitextviewdelegate/textviewshouldbeginediting(_:).md)
  Asks the delegate whether to begin editing in the specified text view.
- [func textViewDidBeginEditing(UITextView)](uitextviewdelegate/textviewdidbeginediting(_:).md)
  Tells the delegate when editing of the specified text view begins.
- [func textViewShouldEndEditing(UITextView) -> Bool](uitextviewdelegate/textviewshouldendediting(_:).md)
  Asks the delegate whether to stop editing in the specified text view.
- [func textViewDidEndEditing(UITextView)](uitextviewdelegate/textviewdidendediting(_:).md)
  Tells the delegate when editing of the specified text view ends.
### Responding to text changes
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](uitextviewdelegate/textview(_:shouldchangetextin:replacementtext:).md)
  Asks the delegate whether to replace the specified text in the text view.
- [func textViewDidChange(UITextView)](uitextviewdelegate/textviewdidchange(_:).md)
  Tells the delegate when the user changes the text or attributes in the specified text view.
### Responding to selection changes
- [func textViewDidChangeSelection(UITextView)](uitextviewdelegate/textviewdidchangeselection(_:).md)
  Tells the delegate when the text selection changes in the specified text view.
### Interacting with text data
- [func textView(UITextView, menuConfigurationFor: UITextItem, defaultMenu: UIMenu) -> UITextItem.MenuConfiguration?](uitextviewdelegate/textview(_:menuconfigurationfor:defaultmenu:).md)
- [func textView(UITextView, primaryActionFor: UITextItem, defaultAction: UIAction) -> UIAction?](uitextviewdelegate/textview(_:primaryactionfor:defaultaction:).md)
- [func textView(UITextView, textItemMenuWillDisplayFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](uitextviewdelegate/textview(_:textitemmenuwilldisplayfor:animator:).md)
- [func textView(UITextView, textItemMenuWillEndFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](uitextviewdelegate/textview(_:textitemmenuwillendfor:animator:).md)
### Providing a context menu
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](uitextviewdelegate/textview(_:editmenufortextin:suggestedactions:).md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.
### Customizing an edit menu
- [func textView(UITextView, willDismissEditMenuWith: any UIEditMenuInteractionAnimating)](uitextviewdelegate/textview(_:willdismisseditmenuwith:).md)
- [func textView(UITextView, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](uitextviewdelegate/textview(_:willpresenteditmenuwith:).md)
### Responding to writing tools interactions
- [func textViewWritingToolsWillBegin(UITextView)](uitextviewdelegate/textviewwritingtoolswillbegin(_:).md)
  Tells the delegate that an interaction with the writing tools interface is about to begin.
- [func textViewWritingToolsDidEnd(UITextView)](uitextviewdelegate/textviewwritingtoolsdidend(_:).md)
  Tells the delegate that the current writing tools session ended.
- [func textView(UITextView, writingToolsIgnoredRangesInEnclosingRange: NSRange) -> [NSValue]](uitextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:).md)
  Asks the delegate to specify any ranges of text you want the writing tools to ignore.
### Inserting a Smart Reply suggestion
- [func textView(UITextView, insertInputSuggestion: UIInputSuggestion)](uitextviewdelegate/textview(_:insertinputsuggestion:).md)
  Tells the delegate when the keyboard delivers an input suggestion.
### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
### Instance Methods
- [func textView(UITextView, didBeginFormattingWith: UITextFormattingViewController)](uitextviewdelegate/textview(_:didbeginformattingwith:).md)
- [func textView(UITextView, didEndFormattingWith: UITextFormattingViewController)](uitextviewdelegate/textview(_:didendformattingwith:).md)
- [func textView(UITextView, editMenuForTextInRanges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?](uitextviewdelegate/textview(_:editmenufortextinranges:suggestedactions:).md)
- [func textView(UITextView, shouldChangeTextInRanges: [NSValue], replacementText: String) -> Bool](uitextviewdelegate/textview(_:shouldchangetextinranges:replacementtext:).md)
- [func textView(UITextView, willBeginFormattingWith: UITextFormattingViewController)](uitextviewdelegate/textview(_:willbeginformattingwith:).md)
- [func textView(UITextView, willEndFormattingWith: UITextFormattingViewController)](uitextviewdelegate/textview(_:willendformattingwith:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIScrollViewDelegate](uiscrollviewdelegate.md)

## See Also

- [class UITextItem](uitextitem.md)
  An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.
- [UITextItem.MenuConfiguration](uitextitem/menuconfiguration.md)
  An object that describes what type of menu and preview to show for a text item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate)*