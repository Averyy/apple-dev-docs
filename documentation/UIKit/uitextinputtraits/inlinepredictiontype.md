# inlinePredictionType

**Framework**: UIKit  
**Kind**: property

The behavior of inline text predictions for a text-entry area.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var inlinePredictionType: UITextInlinePredictionType { get set }
```

#### Discussion

This property controls whether system-provided text suggestions appear inline during typing. The default value is [`UITextInlinePredictionType.default`](uitextinlinepredictiontype/default.md).

If you use a [`UITextView`](uitextview.md) or [`UITextField`](uitextfield.md), set this property if you want to change the inline text prediction behavior. For example, you might want to turn off inline text predictions if your app provides its own text suggestions.

The following code turns off inline text predictions in a text view:

```swift
let textView = UITextView(frame: frame)
textView.inlinePredictionType = .no
```

## See Also

- [var autocapitalizationType: UITextAutocapitalizationType](uitextinputtraits/autocapitalizationtype.md)
  The autocapitalization style for the text object.
- [enum UITextAutocapitalizationType](uitextautocapitalizationtype.md)
  The autocapitalization behavior of a text-based view.
- [var autocorrectionType: UITextAutocorrectionType](uitextinputtraits/autocorrectiontype.md)
  The autocorrection style for the text object.
- [enum UITextAutocorrectionType](uitextautocorrectiontype.md)
  The autocorrection behavior of a text-based view.
- [var spellCheckingType: UITextSpellCheckingType](uitextinputtraits/spellcheckingtype.md)
  The spell-checking style for the text object.
- [enum UITextSpellCheckingType](uitextspellcheckingtype.md)
  The spell-checking behavior of a text-based view.
- [enum UITextInlinePredictionType](uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/inlinepredictiontype)*