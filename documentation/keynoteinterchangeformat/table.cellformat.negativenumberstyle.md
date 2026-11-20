# Table.CellFormat.NegativeNumberStyle

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A style for displaying negative numbers.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.CellFormat.NegativeNumberStyle
```

## Discussion

This value takes one of the following forms:

- `minus`: Prefix with a minus sign (for example, -1,234.56).
- `none`: No special treatment for negative values.
- `parentheses`: Wrap in parentheses with no minus sign (for example, (1,234.56)).
- `red`: Display in red text with a minus sign.
- `red_and_parentheses`: Wrap in parentheses and display in red text.

## See Also

### Enumerations
- [type Table.CellFormat.FormatType](./table.cellformat.formattype.md)
  The kind of formatting to apply to a cell’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.negativenumberstyle)*