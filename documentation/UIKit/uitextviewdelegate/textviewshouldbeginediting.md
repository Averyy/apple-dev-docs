# textViewShouldBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to begin editing in the specified text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textViewShouldBeginEditing(_ textView: UITextView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if an editing session should be initiated; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) to disallow editing.

#### Discussion

When the user performs an action that would normally initiate an editing session, the text view calls this method first to see if editing should actually proceed. In most circumstances, you would simply return [`true`](https://developer.apple.com/documentation/Swift/true) from this method to allow editing to proceed.

Implementation of this method by the delegate is optional. If it is not present, editing proceeds as if this method had returned [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `textView`: The text view for which editing is about to begin.

## See Also

- [func textViewDidBeginEditing(UITextView)](uitextviewdelegate/textviewdidbeginediting(_:).md)
  Tells the delegate when editing of the specified text view begins.
- [func textViewShouldEndEditing(UITextView) -> Bool](uitextviewdelegate/textviewshouldendediting(_:).md)
  Asks the delegate whether to stop editing in the specified text view.
- [func textViewDidEndEditing(UITextView)](uitextviewdelegate/textviewdidendediting(_:).md)
  Tells the delegate when editing of the specified text view ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewshouldbeginediting(_:))*