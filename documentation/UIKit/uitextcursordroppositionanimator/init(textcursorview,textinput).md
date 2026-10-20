# init(textCursorView:textInput:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an animator for the given text cursor view implementation, and the document object that implements the UITextInput protocol.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
init!(textCursorView cursorView: (any UIView & UITextCursorView)!, textInput: (any UIView & UITextInput)!)
```

```objc
- (instancetype) initWithTextCursorView:(UIView<UITextCursorView> *) cursorView textInput:(UIView<UITextInput> *) textInput;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursordroppositionanimator/init(textcursorview:textinput:))*