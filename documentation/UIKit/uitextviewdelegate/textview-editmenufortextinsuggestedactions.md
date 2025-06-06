# textView(_:editMenuForTextIn:suggestedActions:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, editMenuForTextIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextin:suggestedactions:))*