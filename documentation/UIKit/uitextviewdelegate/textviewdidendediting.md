# textViewDidEndEditing(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when editing of the specified text view ends.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textViewDidEndEditing(_ textView: UITextView)
```

#### Discussion

Implementation of this method is optional. A text view sends this message to its delegate after it closes out any pending edits and resigns its first responder status. You can use this method to tear down any data structures or change any state information that you set when editing began.

## Parameters

- `textView`: The text view in which editing ended.

## See Also

- [func textViewShouldBeginEditing(UITextView) -> Bool](uitextviewdelegate/textviewshouldbeginediting(_:).md)
  Asks the delegate whether to begin editing in the specified text view.
- [func textViewDidBeginEditing(UITextView)](uitextviewdelegate/textviewdidbeginediting(_:).md)
  Tells the delegate when editing of the specified text view begins.
- [func textViewShouldEndEditing(UITextView) -> Bool](uitextviewdelegate/textviewshouldendediting(_:).md)
  Asks the delegate whether to stop editing in the specified text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidendediting(_:))*