# kUnicodeStringUnterminatedMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeStringUnterminatedMask = 1L << kUnicodeStringUnterminatedBit
```

## Discussion

A mask for setting the string-unterminated control flag. Determines how the Unicode Converter handles text-element boundaries and direction resolution at the end of an input buffer.

If you clear this bit, the converter treats the end of the buffer as the end of text. 

If you set this bit, the converter assumes that the next call you make using the current context will supply another buffer of text that should be treated as a continuation of the current text. For example, if the last character in the input buffer is `'A'`, `ConvertFromUnicodeToText` stops conversion at the `'A'` and returns `kTECIncompleteElementErr`, because the next buffer could begin with a combining diacritical mark that should be treated as part of the same text element. If the last character in the input buffer is a control character, `ConvertFromUnicodeToText` does not return `kTECIncompleteElementErr` because a control character could not be part of a multiple character text element. 

In attempting to analyze the text direction, when the Unicode Converter reaches the end of the current input buffer and the direction of the current text element is still unresolved, if you clear this flag, the converter treats the end of the buffer as a block separator for direction resolution. If you set this flag, it sets the direction as undetermined


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodestringunterminatedmask)*