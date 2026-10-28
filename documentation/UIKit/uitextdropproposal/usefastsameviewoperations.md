# useFastSameViewOperations

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var useFastSameViewOperations: Bool { get set }
```

```objc
@property (nonatomic) BOOL useFastSameViewOperations;
```

## Discussion

If this property is [`true`](../../Swift/true.md), the drag item data isn’t used. Instead, the drop operation moves or copies the text from its original position to the dropped position within the text view. The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring a text drop proposal
- [var dropAction: UITextDropProposal.Action](./dropaction.md)
  A text drop action style that specifies how the text view receives dropped items.
- [UITextDropProposal.Action](./action.md)
  The text drop action styles for text views.
- [var dropPerformer: UITextDropProposal.Performer](./dropperformer.md)
  The performer that is responsible for handling the drop operation.
- [UITextDropProposal.Performer](./performer.md)
  The performers that are responsible for handling the drop operation.
- [var dropProgressMode: UITextDropProposal.ProgressMode](./dropprogressmode.md)
  A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [UITextDropProposal.ProgressMode](./progressmode.md)
  The text drop progress styles for user-visible progress indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/usefastsameviewoperations)*