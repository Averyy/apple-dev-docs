# UITextDropRequest

**Framework**: UIKit  
**Kind**: protocol

The interface for specifying the attributes of a drop request for a text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextDropRequest : NSObjectProtocol
```

## Topics

### Getting information about the text drop request
- [var dropPosition: UITextPosition](uitextdroprequest/dropposition.md)
  The text position corresponding to the location of a drop session.
- [var isSameView: Bool](uitextdroprequest/issameview.md)
  A Boolean value indicating whether the drag and the drop are within the same text view.
- [var suggestedProposal: UITextDropProposal](uitextdroprequest/suggestedproposal.md)
  The text drop proposal offered by the text view.
### Getting the drop session
- [var dropSession: any UIDropSession](uitextdroprequest/dropsession.md)
  The drop session for the text view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UITextDropProposal](uitextdropproposal.md)
  A proposed configuration for the behavior of a text drop interaction.
- [UITextDropProposal.Action](uitextdropproposal/action.md)
  The text drop action styles for text views.
- [UITextDropProposal.Performer](uitextdropproposal/performer.md)
  The performers that are responsible for handling the drop operation.
- [UITextDropProposal.ProgressMode](uitextdropproposal/progressmode.md)
  The text drop progress styles for user-visible progress indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdroprequest)*