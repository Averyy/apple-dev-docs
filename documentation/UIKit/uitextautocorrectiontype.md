# UITextAutocorrectionType

**Framework**: UIKit  
**Kind**: enum

The autocorrection behavior of a text-based view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum UITextAutocorrectionType
```

#### Overview

Use these constants with the [`autocorrectionType`](uitextinputtraits/autocorrectiontype.md) property. If the script system doesn’t support inline autocorrection, the keyboard input method ignores these constants.

## Topics

### Constants
- [UITextAutocorrectionType.default](uitextautocorrectiontype/default.md)
  Specifies an appropriate autocorrection behavior for the current script system.
- [UITextAutocorrectionType.no](uitextautocorrectiontype/no.md)
  Disables autocorrection behavior.
- [UITextAutocorrectionType.yes](uitextautocorrectiontype/yes.md)
  Enables autocorrection behavior.
### Initializers
- [init?(rawValue: Int)](uitextautocorrectiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var autocapitalizationType: UITextAutocapitalizationType](uitextinputtraits/autocapitalizationtype.md)
  The autocapitalization style for the text object.
- [enum UITextAutocapitalizationType](uitextautocapitalizationtype.md)
  The autocapitalization behavior of a text-based view.
- [var autocorrectionType: UITextAutocorrectionType](uitextinputtraits/autocorrectiontype.md)
  The autocorrection style for the text object.
- [var spellCheckingType: UITextSpellCheckingType](uitextinputtraits/spellcheckingtype.md)
  The spell-checking style for the text object.
- [enum UITextSpellCheckingType](uitextspellcheckingtype.md)
  The spell-checking behavior of a text-based view.
- [var inlinePredictionType: UITextInlinePredictionType](uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.
- [enum UITextInlinePredictionType](uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextautocorrectiontype)*