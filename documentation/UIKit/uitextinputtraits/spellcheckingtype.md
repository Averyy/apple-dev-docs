# spellCheckingType

**Framework**: UIKit  
**Kind**: property

The spell-checking style for the text object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var spellCheckingType: UITextSpellCheckingType { get set }
```

#### Discussion

This property determines whether spell-checking is enabled or disabled during typing. With spell-checking enabled, the text object generates red underlines for all misspelled words. If the user taps on a misspelled word, the text object presents the user with a list of possible corrections.

The default value for this property is [`UITextSpellCheckingType.default`](uitextspellcheckingtype/default.md), which enables spell-checking when autocorrection is also enabled. The value in this property overrides the spell-checking setting set by the user in Settings > General > Keyboard.

## See Also

- [var autocapitalizationType: UITextAutocapitalizationType](uitextinputtraits/autocapitalizationtype.md)
  The autocapitalization style for the text object.
- [enum UITextAutocapitalizationType](uitextautocapitalizationtype.md)
  The autocapitalization behavior of a text-based view.
- [var autocorrectionType: UITextAutocorrectionType](uitextinputtraits/autocorrectiontype.md)
  The autocorrection style for the text object.
- [enum UITextAutocorrectionType](uitextautocorrectiontype.md)
  The autocorrection behavior of a text-based view.
- [enum UITextSpellCheckingType](uitextspellcheckingtype.md)
  The spell-checking behavior of a text-based view.
- [var inlinePredictionType: UITextInlinePredictionType](uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.
- [enum UITextInlinePredictionType](uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/spellcheckingtype)*