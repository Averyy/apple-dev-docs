# autocorrectionType

**Framework**: UIKit  
**Kind**: property

The autocorrection style for the text object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var autocorrectionType: UITextAutocorrectionType { get set }
```

#### Discussion

This property determines whether autocorrection is enabled or disabled during typing. With autocorrection enabled, the text object tracks unknown words and suggests a more suitable replacement candidate to the user, replacing the typed text automatically unless the user explicitly overrides the action.

The default value for this property is [`UITextAutocorrectionType.default`](uitextautocorrectiontype/default.md), which for most input methods results in autocorrection being enabled.

## See Also

- [var autocapitalizationType: UITextAutocapitalizationType](uitextinputtraits/autocapitalizationtype.md)
  The autocapitalization style for the text object.
- [enum UITextAutocapitalizationType](uitextautocapitalizationtype.md)
  The autocapitalization behavior of a text-based view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/autocorrectiontype)*