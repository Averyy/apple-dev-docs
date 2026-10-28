# UITextSpellCheckingType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The spell-checking behavior of a text-based view.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum UITextSpellCheckingType
```

```c
enum UITextSpellCheckingType : NSInteger;
```

## Overview

Use these constants with the [`spellCheckingType`](./uitextinputtraits/spellcheckingtype.md) property.

## Topics

### Constants
- [UITextSpellCheckingType.default](./uitextspellcheckingtype/default.md)
  Specifies the default spell-checking behavior.
- [UITextSpellCheckingType.no](./uitextspellcheckingtype/no.md)
  Disables spell-checking behavior.
- [UITextSpellCheckingType.yes](./uitextspellcheckingtype/yes.md)
  Enables spell-checking behavior.
### Initializers
- [init?(rawValue: Int)](./uitextspellcheckingtype/init%28rawvalue%29.md)

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
- [var inlinePredictionType: UITextInlinePredictionType](./uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.
- [enum UITextInlinePredictionType](./uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype)*