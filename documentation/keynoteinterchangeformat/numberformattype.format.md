# NumberFormatType.Format

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The decoration around a number, such as a trailing period or parentheses.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string NumberFormatType.Format
```

## Discussion

This value takes one of the following forms:

- `circled`: The number enclosed in a circle. Valid only with the `numeric` kind.
- `decimal`: The number followed by a period, as in `1.`.
- `double_paren`: The number enclosed in parentheses, as in `(1)`.
- `paren`: The number followed by a closing parenthesis, as in `1)`.
- `standard`: The standard form of the number for its kind, with no added decoration. Valid only with the `hebrew_biblical` kind.

## See Also

### Enumerations
- [type NumberFormatType.Kind](./numberformattype.kind.md)
  A numbering system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/numberformattype.format)*