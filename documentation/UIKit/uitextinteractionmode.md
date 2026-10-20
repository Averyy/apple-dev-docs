# UITextInteractionMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Modes that determine the selection behaviors that a text interaction provides.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum UITextInteractionMode
```

```c
enum UITextInteractionMode : NSInteger;
```

## Topics

### Modes
- [UITextInteractionMode.editable](./uitextinteractionmode/editable.md)
  A mode indicating that the text interaction should provide selection behaviors for editable text.
- [UITextInteractionMode.nonEditable](./uitextinteractionmode/noneditable.md)
  A mode indicating that the text interaction should provide selection behaviors for non-editable, read-only text.
### Initializers
- [init?(rawValue: Int)](./uitextinteractionmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Text interactions
- [class UITextInteraction](./uitextinteraction.md)
  An interaction that provides text selection gestures and UI to custom text views.
- [protocol UITextInteractionDelegate](./uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractionmode)*