# UITextDropProposal.Performer.view

**Framework**: UIKit  
**Kind**: case

A performer type that indicates that the text view is responsible for doing the drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case view
```

#### Discussion

This performer is the default for a [`UITextDropProposal`](uitextdropproposal.md) object. If this performer is used, the [`textDroppableView(_:willPerformDrop:)`](uitextdropdelegate/textdroppableview(_:willperformdrop:).md) method is called (if implemented). However, implementing the delegate method isn’t required when using this performer.

## See Also

- [UITextDropProposal.Performer.delegate](uitextdropproposal/performer/delegate.md)
  A performer type that indicates the delegate object is responsible for doing the drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/performer/view)*