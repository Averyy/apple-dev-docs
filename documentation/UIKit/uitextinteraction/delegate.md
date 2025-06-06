# delegate

**Framework**: UIKit  
**Kind**: property

The object that receives events from the text interaction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UITextInteractionDelegate)? { get set }
```

## See Also

- [var textInput: (any UIResponder & UITextInput)?](uitextinteraction/textinput.md)
  The object that interacts with the text input system.
- [protocol UITextInteractionDelegate](uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteraction/delegate)*