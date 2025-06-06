# UITextDropProposal.Performer

**Framework**: UIKit  
**Kind**: enum

The performers that are responsible for handling the drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Performer
```

#### Overview

A performer is responsible for:

- Proving a preview for the drop activity.
- Loading data from the item providers.
- Inserting the data into the text view.

## Topics

### Performers
- [UITextDropProposal.Performer.view](uitextdropproposal/performer/view.md)
  A performer type that indicates that the text view is responsible for doing the drop operation.
- [UITextDropProposal.Performer.delegate](uitextdropproposal/performer/delegate.md)
  A performer type that indicates the delegate object is responsible for doing the drop operation.
### Initializers
- [init?(rawValue: UInt)](uitextdropproposal/performer/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITextDropRequest](uitextdroprequest.md)
  The interface for specifying the attributes of a drop request for a text view.
- [class UITextDropProposal](uitextdropproposal.md)
  A proposed configuration for the behavior of a text drop interaction.
- [UITextDropProposal.Action](uitextdropproposal/action.md)
  The text drop action styles for text views.
- [UITextDropProposal.ProgressMode](uitextdropproposal/progressmode.md)
  The text drop progress styles for user-visible progress indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/performer)*