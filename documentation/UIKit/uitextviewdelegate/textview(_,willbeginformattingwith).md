# textView(_:willBeginFormattingWith:)

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
optional func textView(_ textView: UITextView, willBeginFormattingWith viewController: UITextFormattingViewController)
```

```objc
- (void) textView:(UITextView *) textView willBeginFormattingWithViewController:(UITextFormattingViewController *) viewController;
```

## Discussion

Informs the delegate that text formatting controller is about to be presented.

## Parameters

- `viewController`: The text formatting controller that is being presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willbeginformattingwith:))*