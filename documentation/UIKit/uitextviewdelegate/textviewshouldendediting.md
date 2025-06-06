# textViewShouldEndEditing(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to stop editing in the specified text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textViewShouldEndEditing(_ textView: UITextView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if editing should stop; otherwise, [`false`](https://developer.apple.com/documentation/swift/false) if the editing session should continue

#### Discussion

This method is called when the text view is asked to resign the first responder status. This might occur when the user tries to change the editing focus to another control. Before the focus actually changes, however, the text view calls this method to give your delegate a chance to decide whether it should.

Normally, you would return [`true`](https://developer.apple.com/documentation/swift/true) from this method to allow the text view to resign the first responder status. You might return [`false`](https://developer.apple.com/documentation/swift/false), however, in cases where your delegate wants to validate the contents of the text view. By returning [`false`](https://developer.apple.com/documentation/swift/false), you could prevent the user from switching to another control until the text view contained a valid value.

Be aware that this method provides only a recommendation about whether editing should end. Even if you return [`false`](https://developer.apple.com/documentation/swift/false) from this method, it is possible that editing might still end. For example, this might happen when the text view is forced to resign the first responder status by being removed from its parent view or window.

Implementation of this method by the delegate is optional. If it is not present, the first responder status is resigned as if this method had returned [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `textView`: The text view for which editing is about to end.

## See Also

- [func textViewShouldBeginEditing(UITextView) -> Bool](uitextviewdelegate/textviewshouldbeginediting(_:).md)
  Asks the delegate whether to begin editing in the specified text view.
- [func textViewDidBeginEditing(UITextView)](uitextviewdelegate/textviewdidbeginediting(_:).md)
  Tells the delegate when editing of the specified text view begins.
- [func textViewDidEndEditing(UITextView)](uitextviewdelegate/textviewdidendediting(_:).md)
  Tells the delegate when editing of the specified text view ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewshouldendediting(_:))*