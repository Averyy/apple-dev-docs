# textView(_:didEndFormattingWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 26.0+

## Declaration

```swift
optional func textView(_ textView: UITextView, didEndFormattingWith viewController: UITextFormattingViewController)
```

```objc
- (void) textView:(UITextView *) textView didEndFormattingWithViewController:(UITextFormattingViewController *) viewController;
```

## Discussion

Informs the delegate that text formatting controller has been dismissed.

## Parameters

- `viewController`: The text formatting controller that is being presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:didendformattingwith:))*