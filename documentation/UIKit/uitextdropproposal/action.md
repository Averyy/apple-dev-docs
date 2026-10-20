# UITextDropProposal.Action

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The text drop action styles for text views.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Action
```

```c
enum UITextDropAction : NSUInteger;
```

## Topics

### Text drop actions
- [UITextDropProposal.Action.insert](./action/insert.md)
  A text drop action style specifying that text is inserted at the provided location, without altering the surrounding text.
- [UITextDropProposal.Action.replaceAll](./action/replaceall.md)
  A text drop action style specifying that the dropped text replaces all text in the target text view.
- [UITextDropProposal.Action.replaceSelection](./action/replaceselection.md)
  A text drop action style specifying that if the target text view contains a selection, dropped text replaces it.
### Initializers
- [init?(rawValue: UInt)](./action/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Drop management
- [protocol UITextDropRequest](../uitextdroprequest.md)
  The interface for specifying the attributes of a drop request for a text view.
- [class UITextDropProposal](../uitextdropproposal.md)
  A proposed configuration for the behavior of a text drop interaction.
- [UITextDropProposal.Performer](./performer.md)
  The performers that are responsible for handling the drop operation.
- [UITextDropProposal.ProgressMode](./progressmode.md)
  The text drop progress styles for user-visible progress indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/action)*