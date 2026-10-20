# UITextDropProposal.ProgressMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The text drop progress styles for user-visible progress indication.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum ProgressMode
```

```c
enum UITextDropProgressMode : NSUInteger;
```

## Topics

### Progress modes
- [UITextDropProposal.ProgressMode.custom](./progressmode/custom.md)
  A text drop progress mode that indicates that you will provide custom progress indicator during the loading of dropped items.
- [UITextDropProposal.ProgressMode.system](./progressmode/system.md)
  A text drop progress mode indicating that the system will show the progress indicator.
### Initializers
- [init?(rawValue: UInt)](./progressmode/init%28rawvalue%29.md)

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
- [UITextDropProposal.Action](./action.md)
  The text drop action styles for text views.
- [UITextDropProposal.Performer](./performer.md)
  The performers that are responsible for handling the drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/progressmode)*