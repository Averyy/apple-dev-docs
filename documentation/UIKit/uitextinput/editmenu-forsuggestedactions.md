# editMenu(for:suggestedActions:)

**Framework**: UIKit  
**Kind**: method

Asks for the menu to display for the given text range and actions the system provides.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func editMenu(for textRange: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu?
```

#### Return Value

Returns a menu describing the desired menu hierarchy. Return `nil` to present the default system menu.

#### Discussion

The following example returns a menu with additional actions in a submenu.

```swift
func editMenu(for textRange: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu? {
    let indentationMenu = UIMenu(title: "Indentation", image: UIImage(systemName: "list.bullet.indent"), children: [
        UIAction(title: "Increase", image: UIImage(systemName: "increase.indent")) { (action) in
            // Increase indentation action.
        },
        UIAction(title: "Decrease", image: UIImage(systemName: "decrease.indent")) { (action) in
            // Decrease indentation action.
        }
    ])

    var actions = suggestedActions
    actions.append(indentationMenu)
    return UIMenu(children: actions)
}
```

## Parameters

- `textRange`: The text range the menu is presenting for.
- `suggestedActions`: The actions and commands the system suggests.

## See Also

- [func willPresentEditMenu(animator: any UIEditMenuInteractionAnimating)](uitextinput/willpresenteditmenu(animator:).md)
  Tells the object when the system is about to present an edit menu with an animator.
- [func willDismissEditMenu(animator: any UIEditMenuInteractionAnimating)](uitextinput/willdismisseditmenu(animator:).md)
  Tells the object when the system is about to dismiss an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/editmenu(for:suggestedactions:))*