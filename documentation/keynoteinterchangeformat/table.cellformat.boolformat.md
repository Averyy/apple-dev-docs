# Table.CellFormat.BoolFormat

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Options for Boolean formatting, including the strings shown in place of true and false.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellFormat.BoolFormat
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-format.bool-format`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `true_string` (string) *(required)*: The string displayed when the cell value is true (for example, `TRUE`, `Yes`, or `✓`). It’s only read when the cell’s `format_type` is `boolean`.
- `false_string` (string) *(required)*: The string displayed when the cell value is false (for example, `FALSE`, `No`, or `✗`). It’s only read when the cell’s `format_type` is `boolean`.

## See Also

### Objects
- [object Table.CellFormat.BaseFormat](./table.cellformat.baseformat.md)
  Options for formatting a number in a numeral system such as binary, octal, or hexadecimal.
- [object Table.CellFormat.CurrencyFormat](./table.cellformat.currencyformat.md)
  Options for currency formatting.
- [object Table.CellFormat.DateTimeFormat](./table.cellformat.datetimeformat.md)
  Options for date and time formatting.
- [object Table.CellFormat.DurationFormat](./table.cellformat.durationformat.md)
  Options for duration formatting.
- [object Table.CellFormat.FractionFormat](./table.cellformat.fractionformat.md)
  Options for fraction formatting, such as showing a decimal as a fraction.
- [object Table.CellFormat.NumberFormat](./table.cellformat.numberformat.md)
  Options for plain numeric, percentage, and scientific formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.boolformat)*