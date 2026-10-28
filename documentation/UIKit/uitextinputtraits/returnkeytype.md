# returnKeyType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visible indication of what the Return key does.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional var returnKeyType: UIReturnKeyType { get set }
```

```objc
@property (nonatomic) UIReturnKeyType returnKeyType;
```

## Discussion

Setting this property to a different key type changes the visible title of the Return key and typically results in the system dismissing the keyboard when it is pressed. The default value for this property is [`UIReturnKeyType.default`](../uireturnkeytype/default.md).

## See Also

### Configuring the keyboard appearance
- [var keyboardType: UIKeyboardType](./keyboardtype.md)
  The keyboard type for the text object.
- [enum UIKeyboardType](../uikeyboardtype.md)
  Constants that specify the type of keyboard to display for a text-based view.
- [var keyboardAppearance: UIKeyboardAppearance](./keyboardappearance.md)
  The appearance style of the keyboard for the text object.
- [enum UIKeyboardAppearance](../uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [enum UIReturnKeyType](../uireturnkeytype.md)
  Constants that specify the type of Return key the keyboard displays.
- [var textContentType: UITextContentType!](./textcontenttype.md)
  The semantic meaning for a text input area.
- [struct UITextContentType](../uitextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/returnkeytype)*