# NumberFormatType.Kind

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A numbering system.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string NumberFormatType.Kind
```

## Discussion

This value takes one of the following forms:

- `alpha`: Latin letters; use `upper` to choose between A and a.
- `arabian`: Arabic-Indic digits.
- `arabian_abjad`: Abjad numerals, in which Arabic letters carry numeric values.
- `arabian_alpha`: Arabic letters in alphabetical order.
- `hebrew`: Hebrew letters in alphabetical order.
- `hebrew_biblical`: Traditional Hebrew numerals, in which letters carry numeric values.
- `hiragana`: Hiragana characters in aiueo order.
- `hiragana_iroha`: Hiragana characters in iroha order.
- `japanese`: Japanese ideographic numerals; set `formal` for the formal form.
- `katakana`: Katakana characters in aiueo order.
- `katakana_iroha`: Katakana characters in iroha order.
- `korean`: Korean syllables in ga, na, da order.
- `numeric`: Western digits: 1, 2, 3.
- `roman`: Roman numerals; use `upper` to choose between I and i.
- `simplified_chinese`: Simplified Chinese ideographic numerals; set `formal` for the formal form.
- `traditional_chinese`: Traditional Chinese ideographic numerals; set `formal` for the formal form.

## See Also

### Enumerations
- [type NumberFormatType.Format](./numberformattype.format.md)
  The decoration around a number, such as a trailing period or parentheses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/numberformattype.kind)*