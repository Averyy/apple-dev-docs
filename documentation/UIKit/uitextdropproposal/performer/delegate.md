# UITextDropProposal.Performer.delegate

**Framework**: UIKit  
**Kind**: case

A performer type that indicates the delegate object is responsible for doing the drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case delegate
```

#### Discussion

If this performer is used, the delegate must implement the [`textDroppableView(_:willPerformDrop:)`](uitextdropdelegate/textdroppableview(_:willperformdrop:).md) method. Otherwise, the text view handles the drop operation, which is the same behavior as specifying [`UITextDropProposal.Performer.view`](uitextdropproposal/performer/view.md) as the performer.

## See Also

- [UITextDropProposal.Performer.view](uitextdropproposal/performer/view.md)
  A performer type that indicates that the text view is responsible for doing the drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/performer/delegate)*