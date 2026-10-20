# textView(_:willPresentEditMenuWith:)

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
optional func textView(_ textView: UITextView, willPresentEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

```objc
- (void) textView:(UITextView *) textView willPresentEditMenuWithAnimator:(id<UIEditMenuInteractionAnimating>) animator;
```

#### Discussion

Called when the text view is about to present the edit menu.

## Parameters

- `textView`: The text view displaying the menu.
- `animator`: Appearance animator. Add animations to this object to run them alongside the appearance transition.

## See Also

### Customizing an edit menu
- [func textView(UITextView, willDismissEditMenuWith: any UIEditMenuInteractionAnimating)](./textview%28_,willdismisseditmenuwith%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willpresenteditmenuwith:))*