# dropPerformer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The performer that is responsible for handling the drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var dropPerformer: UITextDropProposal.Performer { get set }
```

```objc
@property (nonatomic) UITextDropPerformer dropPerformer;
```

## Discussion

The performer provides a preview for the drop activity, loads the data from the item providers, and inserts the data into the text view. It can be the [`UITextDropProposal.Performer.view`](./performer/view.md) performer (default) or the [`UITextDropProposal.Performer.delegate`](./performer/delegate.md) performer.

## See Also

### Configuring a text drop proposal
- [var dropAction: UITextDropProposal.Action](./dropaction.md)
  A text drop action style that specifies how the text view receives dropped items.
- [UITextDropProposal.Action](./action.md)
  The text drop action styles for text views.
- [UITextDropProposal.Performer](./performer.md)
  The performers that are responsible for handling the drop operation.
- [var dropProgressMode: UITextDropProposal.ProgressMode](./dropprogressmode.md)
  A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [UITextDropProposal.ProgressMode](./progressmode.md)
  The text drop progress styles for user-visible progress indication.
- [var useFastSameViewOperations: Bool](./usefastsameviewoperations.md)
  A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/dropperformer)*