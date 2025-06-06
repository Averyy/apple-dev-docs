# textField(_:willDismissEditMenuWith:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the system is about to dismiss an edit menu with an animator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textField(_ textField: UITextField, willDismissEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `textField`: The text field showing the menu.
- `animator`: The dismissal animator to add animations to, so that the animations will run alongside the dismissal transition.

## See Also

- [func textField(UITextField, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](uitextfielddelegate/textfield(_:willpresenteditmenuwith:).md)
  Tells the delegate that the system is about to present an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:willdismisseditmenuwith:))*