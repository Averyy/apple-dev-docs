# autocapitalizationType

**Framework**: UIKit  
**Kind**: property

The autocapitalization style for the text object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var autocapitalizationType: UITextAutocapitalizationType { get set }
```

#### Discussion

This property determines at what times the Shift key is automatically pressed, thereby making the typed character a capital letter. The default value for this property is [`UITextAutocapitalizationType.sentences`](uitextautocapitalizationtype/sentences.md).

Some keyboard types do not support autocapitalization. Specifically, this option is ignored if the value in the [`keyboardType`](uitextinputtraits/keyboardtype.md) property is set to [`UIKeyboardType.numberPad`](uikeyboardtype/numberpad.md), [`UIKeyboardType.phonePad`](uikeyboardtype/phonepad.md), or [`UIKeyboardType.namePhonePad`](uikeyboardtype/namephonepad.md).

## See Also

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
- [var inlinePredictionType: UITextInlinePredictionType](uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.
- [enum UITextInlinePredictionType](uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/autocapitalizationtype)*