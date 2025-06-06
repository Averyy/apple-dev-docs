# onTextChange

**Framework**: TVMLKit JS  
**Kind**: instp

A function the system calls when the text in a search or text field changes.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function onTextChange;
```

#### Discussion

Provide a callback function for the `onTextChange` attribute to respond to changes in the `searchField` or `textField` elements. You can respond to user inputs as the changes happen. This attribute must be set to a function; for example, `Keyboard.onTextChange = function () {}`.

## See Also

- [text](keyboard/1627359-text.md)
  The text inside a search or text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/keyboard/1627355-ontextchange)*