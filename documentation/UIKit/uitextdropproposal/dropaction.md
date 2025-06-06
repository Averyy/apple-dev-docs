# dropAction

**Framework**: UIKit  
**Kind**: property

A text drop action style that specifies how the text view receives dropped items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dropAction: UITextDropProposal.Action { get set }
```

#### Discussion

The property’s default value is [`UITextDropProposal.Action.insert`](uitextdropproposal/action/insert.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/dropaction)*