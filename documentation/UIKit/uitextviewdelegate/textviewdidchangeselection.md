# textViewDidChangeSelection(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the text selection changes in the specified text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textViewDidChangeSelection(_ textView: UITextView)
```

#### Discussion

Implementation of this method is optional. You can use the [`selectedRange`](uitextview/selectedrange.md) property of the text view to get the new selection.

## Parameters

- `textView`: The text view whose selection changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidchangeselection(_:))*