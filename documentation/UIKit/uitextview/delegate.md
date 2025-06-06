# delegate

**Framework**: UIKit  
**Kind**: property

The text view’s delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UITextViewDelegate)? { get set }
```

#### Discussion

A text view delegate responds to editing-related messages from the text view. You can use the delegate to track changes to the text itself and to the current selection.

For information about the methods implemented by the delegate, see [`UITextViewDelegate`](uitextviewdelegate.md).

## See Also

- [protocol UITextViewDelegate](uitextviewdelegate.md)
  The methods for receiving editing-related messages for text view objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/delegate)*