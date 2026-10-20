# textInput

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that interacts with the text input system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var textInput: (any UIResponder & UITextInput)? { get set }
```

```objc
@property (nonatomic, weak) UIResponder<UITextInput> * textInput;
```

#### Discussion

The object that you assign to [`textInput`](./textinput.md) can be different than the view that contains the text interaction. For example, you may want the gestures for the text interaction to work on a container view, such as a scroll view, while managing the text selection behavior in a contained view, such as the one drawing the text.

## See Also

### Handling text input and interaction events
- [var delegate: (any UITextInteractionDelegate)?](./delegate.md)
  The object that receives events from the text interaction.
- [protocol UITextInteractionDelegate](../uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteraction/textinput)*