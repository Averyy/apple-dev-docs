# textField(_:willPresentEditMenuWith:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the system is about to present an edit menu with an animator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textField(_ textField: UITextField, willPresentEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `textField`: The text field showing the menu.
- `animator`: The appearance animator to add animations to, so that the animations will run alongside the appearance transition.

## See Also

- [func textField(UITextField, willDismissEditMenuWith: any UIEditMenuInteractionAnimating)](uitextfielddelegate/textfield(_:willdismisseditmenuwith:).md)
  Tells the delegate that the system is about to dismiss an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:willpresenteditmenuwith:))*