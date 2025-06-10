# keyboardAppearance

**Framework**: UIKit  
**Kind**: property

The appearance style of the keyboard for the text object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var keyboardAppearance: UIKeyboardAppearance { get set }
```

#### Discussion

This property lets you distinguish between the default text entry inside your application and text entry inside an alert panel. The default value for this property is [`UIKeyboardAppearance.default`](uikeyboardappearance/default.md).

## See Also

- [var keyboardType: UIKeyboardType](uitextinputtraits/keyboardtype.md)
  The keyboard type for the text object.
- [enum UIKeyboardType](uikeyboardtype.md)
  Constants that specify the type of keyboard to display for a text-based view.
- [enum UIKeyboardAppearance](uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [var returnKeyType: UIReturnKeyType](uitextinputtraits/returnkeytype.md)
  The visible indication of what the Return key does.
- [enum UIReturnKeyType](uireturnkeytype.md)
  Constants that specify the type of Return key the keyboard displays.
- [var textContentType: UITextContentType!](uitextinputtraits/textcontenttype.md)
  The semantic meaning for a text input area.
- [struct UITextContentType](uitextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/keyboardappearance)*