# textField(_:willDismissEditMenuWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system is about to dismiss an edit menu with an animator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func textField(_ textField: UITextField, willDismissEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

```objc
- (void) textField:(UITextField *) textField willDismissEditMenuWithAnimator:(id<UIEditMenuInteractionAnimating>) animator;
```

## Parameters

- `textField`: The text field showing the menu.
- `animator`: The dismissal animator to add animations to, so that the animations will run alongside the dismissal transition.

## See Also

### Customizing an edit menu
- [func textField(UITextField, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](./textfield%28_,willpresenteditmenuwith%29.md)
  Tells the delegate that the system is about to present an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:willdismisseditmenuwith:))*