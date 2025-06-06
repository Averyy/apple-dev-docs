# willDismissEditMenu(animator:)

**Framework**: UIKit  
**Kind**: method

Tells the object when the system is about to dismiss an edit menu with an animator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func willDismissEditMenu(animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `animator`: The dismissal animator to add animations to, so that the animations will run alongside the dismissal transition.

## See Also

- [func editMenu(for: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu?](uitextinput/editmenu(for:suggestedactions:).md)
  Asks for the menu to display for the given text range and actions the system provides.
- [func willPresentEditMenu(animator: any UIEditMenuInteractionAnimating)](uitextinput/willpresenteditmenu(animator:).md)
  Tells the object when the system is about to present an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/willdismisseditmenu(animator:))*