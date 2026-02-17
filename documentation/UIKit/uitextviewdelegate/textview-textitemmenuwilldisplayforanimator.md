# textView(_:textItemMenuWillDisplayFor:animator:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate that a text item menu is about to be presented with the specified animator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func textView(_ textView: UITextView, textItemMenuWillDisplayFor textItem: UITextItem, animator: any UIContextMenuInteractionAnimating)
```

## Parameters

- `textView`: The text view showing the menu.
- `textItem`: The text item for performing said action.
- `animator`: Appearance animator. Add animations to this object to run them alongside the appearance transition.

## See Also

- [func textView(UITextView, menuConfigurationFor: UITextItem, defaultMenu: UIMenu) -> UITextItem.MenuConfiguration?](uitextviewdelegate/textview(_:menuconfigurationfor:defaultmenu:).md)
  Asks the delegate for the menu configuration to be performed when interacting with a text item.
- [func textView(UITextView, primaryActionFor: UITextItem, defaultAction: UIAction) -> UIAction?](uitextviewdelegate/textview(_:primaryactionfor:defaultaction:).md)
  Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.
- [func textView(UITextView, textItemMenuWillEndFor: UITextItem, animator: any UIContextMenuInteractionAnimating)](uitextviewdelegate/textview(_:textitemmenuwillendfor:animator:).md)
  Informs the delegate that a text item menu is about to be dismissed with the specified animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:textitemmenuwilldisplayfor:animator:))*