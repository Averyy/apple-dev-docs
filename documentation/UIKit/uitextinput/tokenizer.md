# tokenizer

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

An input tokenizer that provides information about the granularity of text units.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var tokenizer: any UITextInputTokenizer { get }
```

#### Discussion

Standard units of granularity include characters, words, lines, and paragraphs. In most cases, you may lazily create and assign an instance of a subclass of [`UITextInputStringTokenizer`](uitextinputstringtokenizer.md) for this purpose. If you require different behavior than this system-provided tokenizer, you can create a custom tokenizer that adopts the [`UITextInputTokenizer`](uitextinputtokenizer.md) protocol.

## See Also

- [protocol UITextInputTokenizer](uitextinputtokenizer.md)
  A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/tokenizer)*