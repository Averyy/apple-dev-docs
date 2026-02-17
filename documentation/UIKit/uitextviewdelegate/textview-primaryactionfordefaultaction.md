# textView(_:primaryActionFor:defaultAction:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func textView(_ textView: UITextView, primaryActionFor textItem: UITextItem, defaultAction: UIAction) -> UIAction?
```

#### Return Value

Return a UIAction to be performed when the text item is interacted with. Return @c nil to prevent the action from being performed.

## Parameters

- `textView`: The text view requesting the primary action.
- `textItem`: The text item for performing said action.
- `defaultAction`: The default action for the text item. Return this to perform the default action.

## See Also

- [func textView(UITextView, menuConfigurationFor: UITextItem, defaultMenu: UIMenu) -> UITextItem.MenuConfiguration?](uitextviewdelegate/textview(_:menuconfigurationfor:defaultmenu:).md)
  Asks the delegate for the menu configuration to be performed when interacting with a text item.
- [func textView(UITextView, textItemMenuWillDisplayFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](uitextviewdelegate/textview(_:textitemmenuwilldisplayfor:animator:).md)
  Informs the delegate that a text item menu is about to be presented with the specified animator.
- [func textView(UITextView, textItemMenuWillEndFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](uitextviewdelegate/textview(_:textitemmenuwillendfor:animator:).md)
  Informs the delegate that a text item menu is about to be dismissed with the specified animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:primaryactionfor:defaultaction:))*