# textView(_:willDismissEditMenuWith:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func textView(_ textView: UITextView, willDismissEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

#### Discussion

Called when the text view is about to dismiss the edit menu.

## Parameters

- `textView`: The text view displaying the menu.
- `animator`: Dismissal animator. Add animations to this object to run them alongside the dismissal transition.

## See Also

- [func textView(UITextView, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](uitextviewdelegate/textview(_:willpresenteditmenuwith:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willdismisseditmenuwith:))*