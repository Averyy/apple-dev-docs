# willDismissEditMenu(animator:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the object when the system is about to dismiss an edit menu with an animator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func willDismissEditMenu(animator: any UIEditMenuInteractionAnimating)
```

```objc
- (void) willDismissEditMenuWithAnimator:(id<UIEditMenuInteractionAnimating>) animator;
```

## Parameters

- `animator`: The dismissal animator to add animations to, so that the animations will run alongside the dismissal transition.

## See Also

### Managing the edit menu
- [func editMenu(for: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./editmenu%28for,suggestedactions%29.md)
  Asks for the menu to display for the given text range and actions the system provides.
- [func willPresentEditMenu(animator: any UIEditMenuInteractionAnimating)](./willpresenteditmenu%28animator%29.md)
  Tells the object when the system is about to present an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/willdismisseditmenu(animator:))*