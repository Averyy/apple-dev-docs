# textViewDidChange(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the user changes the text or attributes in the specified text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
optional func textViewDidChange(_ textView: UITextView)
```

#### Discussion

The text view calls this method in response to user-initiated changes to the text. This method is not called in response to programmatically initiated changes.

Implementation of this method is optional.

## Parameters

- `textView`: The text view containing the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidchange(_:))*