# textView(_:editMenuForTextIn:suggestedActions:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.2
- tvOS 16.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
optional func textView(_ textView: UITextView, editMenuForTextIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?
```

```objc
- (UIMenu *) textView:(UITextView *) textView editMenuForTextInRange:(NSRange) range suggestedActions:(NSArray<UIMenuElement *> *) suggestedActions;
```

#### Return Value

Returns a menu describing the desired menu hierarchy. Return `nil` to present the default system menu.

#### Discussion

The following example returns a menu that includes an “Add Bookmark” action and also a “Highlight” action, but only if the selected text range is greater than zero.

```swift
func textView(_ textView: UITextView, editMenuForTextIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu? {
    var additionalActions: [UIMenuElement] = []
    if range.length > 0 {
        let highlightAction = UIAction(title: "Highlight", image: UIImage(systemName: "highlighter")) { action in
            // The highlight action.
        }
        additionalActions.append(highlightAction)
    }
    let addBookmarkAction = UIAction(title: "Add Bookmark", image: UIImage(systemName: "bookmark")) { action in
        // The bookmark action.
    }
    additionalActions.append(addBookmarkAction)
    return UIMenu(children: suggestedActions + additionalActions)
}
```

## Parameters

- `textView`: The text view requesting the menu.
- `range`: The character range the menu is presenting for.
- `suggestedActions`: The actions and commands the system suggests.

## See Also

### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](../uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./textview%28_,shouldchangetextin,replacementtext%29.md)
  Asks the delegate whether to replace the specified text in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextin:suggestedactions:))*