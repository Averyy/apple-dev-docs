# dropProgressMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A mode that specifies how the text view indicates progress to the user when loading dropped items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var dropProgressMode: UITextDropProposal.ProgressMode { get set }
```

```objc
@property (nonatomic) UITextDropProgressMode dropProgressMode;
```

#### Discussion

The default value is [`UITextDropProposal.ProgressMode.system`](./progressmode/system.md).

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
- [UITextDropProposal.ProgressMode](./progressmode.md)
  The text drop progress styles for user-visible progress indication.
- [var useFastSameViewOperations: Bool](./usefastsameviewoperations.md)
  A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/dropprogressmode)*