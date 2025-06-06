# UITextDropProposal

**Framework**: UIKit  
**Kind**: class

A proposed configuration for the behavior of a text drop interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextDropProposal
```

## Topics

### Configuring a text drop proposal
- [var dropAction: UITextDropProposal.Action](uitextdropproposal/dropaction.md)
  A text drop action style that specifies how the text view receives dropped items.
- [UITextDropProposal.Action](uitextdropproposal/action.md)
  The text drop action styles for text views.
- [var dropPerformer: UITextDropProposal.Performer](uitextdropproposal/dropperformer.md)
  The performer that is responsible for handling the drop operation.
- [UITextDropProposal.Performer](uitextdropproposal/performer.md)
  The performers that are responsible for handling the drop operation.
- [var dropProgressMode: UITextDropProposal.ProgressMode](uitextdropproposal/dropprogressmode.md)
  A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [UITextDropProposal.ProgressMode](uitextdropproposal/progressmode.md)
  The text drop progress styles for user-visible progress indication.
- [var useFastSameViewOperations: Bool](uitextdropproposal/usefastsameviewoperations.md)
  A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.

## Relationships

### Inherits From
- [UIDropProposal](uidropproposal.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITextDropRequest](uitextdroprequest.md)
  The interface for specifying the attributes of a drop request for a text view.
- [UITextDropProposal.Action](uitextdropproposal/action.md)
  The text drop action styles for text views.
- [UITextDropProposal.Performer](uitextdropproposal/performer.md)
  The performers that are responsible for handling the drop operation.
- [UITextDropProposal.ProgressMode](uitextdropproposal/progressmode.md)
  The text drop progress styles for user-visible progress indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal)*