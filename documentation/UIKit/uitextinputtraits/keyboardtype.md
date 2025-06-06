# keyboardType

**Framework**: UIKit  
**Kind**: property

The keyboard type for the text object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var keyboardType: UIKeyboardType { get set }
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Discussion

Text objects can be targeted for specific types of input, such as plain text, email, numeric entry, and so on. The keyboard style identifies what keys are available on the keyboard and which ones appear by default. The default value for this property is [`UIKeyboardType.default`](uikeyboardtype/default.md).

## See Also

- [enum UIKeyboardType](uikeyboardtype.md)
  Constants that specify the type of keyboard to display for a text-based view.
- [var keyboardAppearance: UIKeyboardAppearance](uitextinputtraits/keyboardappearance.md)
  The appearance style of the keyboard for the text object.
- [enum UIKeyboardAppearance](uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [var returnKeyType: UIReturnKeyType](uitextinputtraits/returnkeytype.md)
  The visible title of the Return key.
- [enum UIReturnKeyType](uireturnkeytype.md)
  Constants that specify the text string that displays in the Return key of a keyboard.
- [var textContentType: UITextContentType!](uitextinputtraits/textcontenttype.md)
  The semantic meaning for a text input area.
- [struct UITextContentType](uitextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/keyboardtype)*