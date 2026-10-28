# textView(_:willDismissEditMenuWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func textView(_ textView: UITextView, willDismissEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

```objc
- (void) textView:(UITextView *) textView willDismissEditMenuWithAnimator:(id<UIEditMenuInteractionAnimating>) animator;
```

## Discussion

Called when the text view is about to dismiss the edit menu.

## Parameters

- `textView`: The text view displaying the menu.
- `animator`: Dismissal animator. Add animations to this object to run them alongside the dismissal transition.

## See Also

### Customizing an edit menu
- [func textView(UITextView, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](./textview%28_,willpresenteditmenuwith%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willdismisseditmenuwith:))*