# isHardwareKeyboardInputExpected

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether someone is likely to enter text using a hardware keyboard.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
var isHardwareKeyboardInputExpected: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isHardwareKeyboardInputExpected) BOOL hardwareKeyboardInputExpected;
```

## Discussion

When hardware keyboard input is likely, adjust your UI or perform any actions you need to accommodate that input.

## See Also

### Getting the expected input type
- [var isDictationInputExpected: Bool](./isdictationinputexpected.md)
  Returns a Boolean value that indicates whether someone is likely to use dictation to input text to the app.
- [var isPencilInputExpected: Bool](./ispencilinputexpected.md)
  Returns a Boolean value that indicates whether someone is likely to use Apple Pencil for input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputcontext/ishardwarekeyboardinputexpected)*