# UITextAutocapitalizationType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The autocapitalization behavior of a text-based view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum UITextAutocapitalizationType
```

```c
enum UITextAutocapitalizationType : NSInteger;
```

#### Overview

Use these constants with the [`autocapitalizationType`](./uitextinputtraits/autocapitalizationtype.md) property. If the script system doesn’t support capitalization, the keyboard input method ignores these constants.

Some keyboard types don’t support autocapitalization. Specifically, if the [`keyboardType`](./uitextinputtraits/keyboardtype.md) property is set to [`UIKeyboardType.numberPad`](./uikeyboardtype/numberpad.md), [`UIKeyboardType.phonePad`](./uikeyboardtype/phonepad.md), or [`UIKeyboardType.namePhonePad`](./uikeyboardtype/namephonepad.md), the system ignores these constants.

## Topics

### Constants
- [UITextAutocapitalizationType.none](./uitextautocapitalizationtype/none.md)
  Specifies that there is no automatic text capitalization.
- [UITextAutocapitalizationType.words](./uitextautocapitalizationtype/words.md)
  Specifies automatic capitalization of the first letter of each word.
- [UITextAutocapitalizationType.sentences](./uitextautocapitalizationtype/sentences.md)
  Specifies automatic capitalization of the first letter of each sentence.
- [UITextAutocapitalizationType.allCharacters](./uitextautocapitalizationtype/allcharacters.md)
  Specifies automatic capitalization of all characters, such as for entry of two-character state abbreviations for the United States.
### Initializers
- [init?(rawValue: Int)](./uitextautocapitalizationtype/init%28rawvalue%29.md)

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
- [enum UITextInlinePredictionType](./uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextautocapitalizationtype)*