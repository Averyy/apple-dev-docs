# useFastSameViewOperations

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var useFastSameViewOperations: Bool { get set }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), the drag item data isn’t used. Instead, the drop operation moves or copies the text from its original position to the dropped position within the text view. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/usefastsameviewoperations)*