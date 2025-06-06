# textInput

**Framework**: UIKit  
**Kind**: property

The object that interacts with the text input system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var textInput: (any UIResponder & UITextInput)? { get set }
```

#### Discussion

The object that you assign to [`textInput`](uitextinteraction/textinput.md) can be different than the view that contains the text interaction. For example, you may want the gestures for the text interaction to work on a container view, such as a scroll view, while managing the text selection behavior in a contained view, such as the one drawing the text.

## See Also

- [var delegate: (any UITextInteractionDelegate)?](uitextinteraction/delegate.md)
  The object that receives events from the text interaction.
- [protocol UITextInteractionDelegate](uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteraction/textinput)*