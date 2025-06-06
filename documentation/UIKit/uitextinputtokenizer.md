# UITextInputTokenizer

**Framework**: UIKit  
**Kind**: protocol

A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITextInputTokenizer : NSObjectProtocol
```

#### Overview

Granularities of text units are always evaluated with reference to a storage or reference direction.

Text-processing objects that conform to the [`UITextInput`](uitextinput.md) protocol must hold a reference to a tokenizer (through the [`tokenizer`](uitextinput/tokenizer.md) property). The [`UITextInputStringTokenizer`](uitextinputstringtokenizer.md) class provides a default base implementation of the [`UITextInputTokenizer`](uitextinputtokenizer.md) protocol. Tokenizers of this class are suitable for most western-language keyboards. Apps with different requirements may adopt the [`UITextInputTokenizer`](uitextinputtokenizer.md) protocol and create their own tokenizers.

## Topics

### Determining text positions relative to unit boundaries
- [func isPosition(UITextPosition, atBoundary: UITextGranularity, inDirection: UITextDirection) -> Bool](uitextinputtokenizer/isposition(_:atboundary:indirection:).md)
  Return whether a text position is at a boundary of a text unit of a specified granularity in a specified direction.
- [func isPosition(UITextPosition, withinTextUnit: UITextGranularity, inDirection: UITextDirection) -> Bool](uitextinputtokenizer/isposition(_:withintextunit:indirection:).md)
  Return whether a text position is within a text unit of a specified granularity in a specified direction.
### Computing text position by unit boundaries
- [func position(from: UITextPosition, toBoundary: UITextGranularity, inDirection: UITextDirection) -> UITextPosition?](uitextinputtokenizer/position(from:toboundary:indirection:).md)
  Return the next text position at a boundary of a text unit of the given granularity in a given direction.
### Getting ranges of specific text units
- [func rangeEnclosingPosition(UITextPosition, with: UITextGranularity, inDirection: UITextDirection) -> UITextRange?](uitextinputtokenizer/rangeenclosingposition(_:with:indirection:).md)
  Return the range for the text enclosing a text position in a text unit of a given granularity in a given direction.
### Constants
- [struct UITextDirection](uitextdirection.md)
  The direction of the text.
- [enum UITextGranularity](uitextgranularity.md)
  The granularity of a unit of text.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITextInputStringTokenizer](uitextinputstringtokenizer.md)

## See Also

- [class UITextInputStringTokenizer](uitextinputstringtokenizer.md)
  A base implementation of the text-input tokenizer protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer)*