# textViewDidBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when editing of the specified text view begins.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textViewDidBeginEditing(_ textView: UITextView)
```

```objc
- (void) textViewDidBeginEditing:(UITextView *) textView;
```

#### Discussion

Implementation of this method is optional. A text view sends this message to its delegate immediately after the user initiates editing in a text view and before any changes are actually made. You can use this method to set up any editing-related data structures and generally prepare your delegate to receive future editing messages.

## Parameters

- `textView`: The text view in which editing began.

## See Also

### Responding to editing notifications
- [func textViewShouldBeginEditing(UITextView) -> Bool](./textviewshouldbeginediting%28_%29.md)
  Asks the delegate whether to begin editing in the specified text view.
- [func textViewShouldEndEditing(UITextView) -> Bool](./textviewshouldendediting%28_%29.md)
  Asks the delegate whether to stop editing in the specified text view.
- [func textViewDidEndEditing(UITextView)](./textviewdidendediting%28_%29.md)
  Tells the delegate when editing of the specified text view ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidbeginediting(_:))*