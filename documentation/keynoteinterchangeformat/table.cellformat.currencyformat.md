# Table.CellFormat.CurrencyFormat

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Options for currency formatting.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellFormat.CurrencyFormat
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-format.currency-format`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `decimal_places` (integer): The number of decimal places to display, `0` through 30; a negative value is treated as zero rather than rejected. The value 253 means automatic (as many decimal places as the value needs) rather than a digit count.

  **Default**: `2`
- `negative_number_style` (Table.CellFormat.NegativeNumberStyle): The display style for negative amounts.
- `use_thousands_separator` (boolean): Whether to insert a thousands separator (for example, $1,234,567.00).

  **Default**: `true`
- `accounting_style` (boolean): Whether to use accounting style: currency symbol left-aligned and negative values in parentheses.

  **Default**: `false`
- `currency_code` (string): The ISO 4217 currency code (for example, `USD`, `EUR`, or `JPY`) that determines the symbol shown.

  **Default**: `USD`

## See Also

### Objects
- [object Table.CellFormat.BaseFormat](./table.cellformat.baseformat.md)
  Options for formatting a number in a numeral system such as binary, octal, or hexadecimal.
- [object Table.CellFormat.BoolFormat](./table.cellformat.boolformat.md)
  Options for Boolean formatting, including the strings shown in place of true and false.
- [object Table.CellFormat.DateTimeFormat](./table.cellformat.datetimeformat.md)
  Options for date and time formatting.
- [object Table.CellFormat.DurationFormat](./table.cellformat.durationformat.md)
  Options for duration formatting.
- [object Table.CellFormat.FractionFormat](./table.cellformat.fractionformat.md)
  Options for fraction formatting, such as showing a decimal as a fraction.
- [object Table.CellFormat.NumberFormat](./table.cellformat.numberformat.md)
  Options for plain numeric, percentage, and scientific formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.currencyformat)*