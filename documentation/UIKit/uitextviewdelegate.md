# UITextViewDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The methods for receiving editing-related messages for text view objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UITextViewDelegate : UIScrollViewDelegate
```

```objc
@protocol UITextViewDelegate <NSObject, UIScrollViewDelegate>
```

#### Overview

All of the methods in this protocol are optional. You can use them in situations where you might want to adjust the text a user is editing (such as in the case of a spell-checker program) or to modify the intended insertion point.

## Topics

### Responding to editing notifications
- [func textViewShouldBeginEditing(UITextView) -> Bool](./uitextviewdelegate/textviewshouldbeginediting%28_%29.md)
  Asks the delegate whether to begin editing in the specified text view.
- [func textViewDidBeginEditing(UITextView)](./uitextviewdelegate/textviewdidbeginediting%28_%29.md)
  Tells the delegate when editing of the specified text view begins.
- [func textViewShouldEndEditing(UITextView) -> Bool](./uitextviewdelegate/textviewshouldendediting%28_%29.md)
  Asks the delegate whether to stop editing in the specified text view.
- [func textViewDidEndEditing(UITextView)](./uitextviewdelegate/textviewdidendediting%28_%29.md)
  Tells the delegate when editing of the specified text view ends.
### Responding to text changes
- [func textViewDidChange(UITextView)](./uitextviewdelegate/textviewdidchange%28_%29.md)
  Tells the delegate when the user changes the text or attributes in the specified text view.
### Responding to selection changes
- [func textViewDidChangeSelection(UITextView)](./uitextviewdelegate/textviewdidchangeselection%28_%29.md)
  Tells the delegate when the text selection changes in the specified text view.
### Interacting with text data
- [func textView(UITextView, menuConfigurationFor: UITextItem, defaultMenu: UIMenu) -> UITextItem.MenuConfiguration?](./uitextviewdelegate/textview%28_,menuconfigurationfor,defaultmenu%29.md)
  Asks the delegate for the menu configuration to be performed when interacting with a text item.
- [func textView(UITextView, primaryActionFor: UITextItem, defaultAction: UIAction) -> UIAction?](./uitextviewdelegate/textview%28_,primaryactionfor,defaultaction%29.md)
  Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.
- [func textView(UITextView, textItemMenuWillDisplayFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](./uitextviewdelegate/textview%28_,textitemmenuwilldisplayfor,animator%29.md)
  Informs the delegate that a text item menu is about to be presented with the specified animator.
- [func textView(UITextView, textItemMenuWillEndFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](./uitextviewdelegate/textview%28_,textitemmenuwillendfor,animator%29.md)
  Informs the delegate that a text item menu is about to be dismissed with the specified animator.
### Customizing an edit menu
- [func textView(UITextView, willDismissEditMenuWith: any UIEditMenuInteractionAnimating)](./uitextviewdelegate/textview%28_,willdismisseditmenuwith%29.md)
- [func textView(UITextView, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](./uitextviewdelegate/textview%28_,willpresenteditmenuwith%29.md)
### Responding to writing tools interactions
- [func textViewWritingToolsWillBegin(UITextView)](./uitextviewdelegate/textviewwritingtoolswillbegin%28_%29.md)
  Tells the delegate that an interaction with the writing tools interface is about to begin.
- [func textViewWritingToolsDidEnd(UITextView)](./uitextviewdelegate/textviewwritingtoolsdidend%28_%29.md)
  Tells the delegate that the current writing tools session ended.
- [func textView(UITextView, writingToolsIgnoredRangesInEnclosingRange: NSRange) -> [NSValue]](./uitextviewdelegate/textview%28_,writingtoolsignoredrangesinenclosingrange%29.md)
  Asks the delegate to specify any ranges of text you want the writing tools to ignore.
### Inserting a Smart Reply suggestion
- [func textView(UITextView, insertInputSuggestion: UIInputSuggestion)](./uitextviewdelegate/textview%28_,insertinputsuggestion%29.md)
  Tells the delegate when the keyboard delivers an input suggestion.
### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in,interaction%29-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in%29-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in%29-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](./uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./uitextviewdelegate/textview%28_,shouldchangetextin,replacementtext%29.md)
  Asks the delegate whether to replace the specified text in the text view.
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./uitextviewdelegate/textview%28_,editmenufortextin,suggestedactions%29.md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.
### Instance Methods
- [func textView(UITextView, didBeginFormattingWith: UITextFormattingViewController)](./uitextviewdelegate/textview%28_,didbeginformattingwith%29.md)
- [func textView(UITextView, didEndFormattingWith: UITextFormattingViewController)](./uitextviewdelegate/textview%28_,didendformattingwith%29.md)
- [func textView(UITextView, editMenuForTextInRanges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?](./uitextviewdelegate/textview%28_,editmenufortextinranges,suggestedactions%29.md)
- [func textView(UITextView, shouldChangeTextInRanges: [NSValue], replacementText: String) -> Bool](./uitextviewdelegate/textview%28_,shouldchangetextinranges,replacementtext%29.md)
- [func textView(UITextView, willBeginFormattingWith: UITextFormattingViewController)](./uitextviewdelegate/textview%28_,willbeginformattingwith%29.md)
- [func textView(UITextView, willEndFormattingWith: UITextFormattingViewController)](./uitextviewdelegate/textview%28_,willendformattingwith%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIScrollViewDelegate](./uiscrollviewdelegate.md)

## See Also

### Text actions and menus
- [class UITextItem](./uitextitem.md)
  An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.
- [UITextItem.MenuConfiguration](./uitextitem/menuconfiguration.md)
  An object that describes what type of menu and preview to show for a text item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate)*