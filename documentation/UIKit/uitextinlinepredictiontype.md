# UITextInlinePredictionType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UITextInlinePredictionType : NSInteger;
```

#### Overview

Use these constants with the [`inlinePredictionType`](./uitextinputtraits/inlinepredictiontype.md) property.

## Topics

### Constants
- [UITextInlinePredictionType.default](./uitextinlinepredictiontype/default.md)
  A constant that determines the behavior of inline text predictions according to the context.
- [UITextInlinePredictionType.no](./uitextinlinepredictiontype/no.md)
  A constant that turns off inline text predictions.
- [UITextInlinePredictionType.yes](./uitextinlinepredictiontype/yes.md)
  A constant that turns on inline text predictions.
### Initializers
- [init?(rawValue: Int)](./uitextinlinepredictiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing spelling and autocorrection
- [var autocapitalizationType: UITextAutocapitalizationType](./uitextinputtraits/autocapitalizationtype.md)
  The autocapitalization style for the text object.
- [enum UITextAutocapitalizationType](./uitextautocapitalizationtype.md)
  The autocapitalization behavior of a text-based view.
- [var autocorrectionType: UITextAutocorrectionType](./uitextinputtraits/autocorrectiontype.md)
  The autocorrection style for the text object.
- [enum UITextAutocorrectionType](./uitextautocorrectiontype.md)
  The autocorrection behavior of a text-based view.
- [var spellCheckingType: UITextSpellCheckingType](./uitextinputtraits/spellcheckingtype.md)
  The spell-checking style for the text object.
- [enum UITextSpellCheckingType](./uitextspellcheckingtype.md)
  The spell-checking behavior of a text-based view.
- [var inlinePredictionType: UITextInlinePredictionType](./uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinlinepredictiontype)*