# UITextInlinePredictionType

**Framework**: UIKit  
**Kind**: enum

Constants that identify the behavior of inline text predictions for a text-entry area.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum UITextInlinePredictionType
```

#### Overview

Use these constants with the [`inlinePredictionType`](uitextinputtraits/inlinepredictiontype.md) property.

## Topics

### Constants
- [UITextInlinePredictionType.default](uitextinlinepredictiontype/default.md)
  A constant that determines the behavior of inline text predictions according to the context.
- [UITextInlinePredictionType.no](uitextinlinepredictiontype/no.md)
  A constant that turns off inline text predictions.
- [UITextInlinePredictionType.yes](uitextinlinepredictiontype/yes.md)
  A constant that turns on inline text predictions.
### Initializers
- [init?(rawValue: Int)](uitextinlinepredictiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var inlinePredictionType: UITextInlinePredictionType](uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinlinepredictiontype)*