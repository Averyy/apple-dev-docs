# textContentType

**Framework**: UIKit  
**Kind**: property

The semantic meaning for a text input area.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var textContentType: UITextContentType! { get set }
```

#### Discussion

Use this property to give the keyboard and the system information about the expected semantic meaning for the content that users enter. For example, you might specify [`emailAddress`](uitextcontenttype/emailaddress.md) for a text field that users fill in to receive an email confirmation. When you provide this information about the content you expect users to enter in a text input area, the system can in some cases automatically select an appropriate keyboard and improve keyboard corrections and proactive integration with other text input opportunities.

Because the expected semantic meaning for each text input area should be identified as specifically as possible, you can’t combine multiple values for one [`textContentType`](uitextinputtraits/textcontenttype.md) property. For possible values you can use, see [`UITextContentType`](uitextcontenttype.md); by default, the value of this property is `nil`.

## See Also

- [var keyboardType: UIKeyboardType](uitextinputtraits/keyboardtype.md)
  The keyboard type for the text object.
- [enum UIKeyboardType](uikeyboardtype.md)
  Constants that specify the type of keyboard to display for a text-based view.
- [var keyboardAppearance: UIKeyboardAppearance](uitextinputtraits/keyboardappearance.md)
  The appearance style of the keyboard for the text object.
- [enum UIKeyboardAppearance](uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [var returnKeyType: UIReturnKeyType](uitextinputtraits/returnkeytype.md)
  The visible indication of what the Return key does.
- [enum UIReturnKeyType](uireturnkeytype.md)
  Constants that specify the type of Return key the keyboard displays.
- [struct UITextContentType](uitextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/textcontenttype)*