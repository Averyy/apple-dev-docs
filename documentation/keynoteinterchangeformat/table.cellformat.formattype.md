# Table.CellFormat.FormatType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The kind of formatting to apply to a cell’s value.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.CellFormat.FormatType
```

## Discussion

Each case selects which sub-format property of the cell format is read.

This value takes one of the following forms:

- `automatic`: Inferred from the value’s data type: numbers display as numbers, dates as dates, and so on.
- `base`: Display in a chosen numeric base (for example, binary, octal, hexadecimal). Shown in Keynote as Numeral System.
- `boolean`: Display as TRUE or FALSE (or as user-specified strings set in the Boolean format options).
- `currency`: Currency formatting with a currency symbol or code and optional accounting style.
- `custom`: User-defined format string with optional conditional rules (see the table’s custom formats).
- `date_time`: A date, a time, or both, formatted with a date and time format string.
- `duration`: Duration in chosen units (weeks, days, hours, and so on).
- `fraction`: Display as a fraction at a chosen accuracy (such as halves, eighths, or up to a number of digits).
- `number`: Plain numeric formatting (decimal places, thousands separator, negative number style).
- `percentage`: Numeric formatting where the displayed value is the underlying value multiplied by 100, suffixed with “%.”
- `scientific`: Scientific notation (for example, 1.23E+04).
- `text`: Treat the value as raw text (no numeric or date interpretation). A reader in version 1.0 doesn’t apply this format, so a cell written with it opens with the `automatic` format instead.

## See Also

### Enumerations
- [type Table.CellFormat.NegativeNumberStyle](./table.cellformat.negativenumberstyle.md)
  A style for displaying negative numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.formattype)*