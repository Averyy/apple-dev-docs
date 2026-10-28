# textViewShouldBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to begin editing in the specified text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textViewShouldBeginEditing(_ textView: UITextView) -> Bool
```

```objc
- (BOOL) textViewShouldBeginEditing:(UITextView *) textView;
```

## Return Value

[`true`](../../Swift/true.md) if an editing session should be initiated; otherwise, [`false`](../../Swift/false.md) to disallow editing.

## Discussion

When the user performs an action that would normally initiate an editing session, the text view calls this method first to see if editing should actually proceed. In most circumstances, you would simply return [`true`](../../Swift/true.md) from this method to allow editing to proceed.

Implementation of this method by the delegate is optional. If it is not present, editing proceeds as if this method had returned [`true`](../../Swift/true.md).

## Parameters

- `textView`: The text view for which editing is about to begin.

## See Also

### Responding to editing notifications
- [func textViewDidBeginEditing(UITextView)](./textviewdidbeginediting%28_%29.md)
  Tells the delegate when editing of the specified text view begins.
- [func textViewShouldEndEditing(UITextView) -> Bool](./textviewshouldendediting%28_%29.md)
  Asks the delegate whether to stop editing in the specified text view.
- [func textViewDidEndEditing(UITextView)](./textviewdidendediting%28_%29.md)
  Tells the delegate when editing of the specified text view ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewshouldbeginediting(_:))*