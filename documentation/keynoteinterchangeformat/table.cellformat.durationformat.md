# Table.CellFormat.DurationFormat

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Options for duration formatting.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellFormat.DurationFormat
```

## Overview

They set how a span of time is broken into units and displayed.

## Topics

### Enumerations
- [type Table.CellFormat.DurationFormat.Style](./table.cellformat.durationformat.style.md)
  The length of the unit labels in a displayed duration.
- [type Table.CellFormat.DurationFormat.Unit](./table.cellformat.durationformat.unit.md)
  A duration unit.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-format.duration-format`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `use_automatic_units` (boolean): Whether units are chosen automatically based on the duration’s magnitude. If it’s `false`, `smallest_unit` and `largest_unit` are used.

  **Default**: `true`
- `smallest_unit` (Table.CellFormat.DurationFormat.Unit): The smallest unit to include in the displayed duration. It’s used only when `use_automatic_units` is `false`.
- `largest_unit` (Table.CellFormat.DurationFormat.Unit): The largest unit to include in the displayed duration. It’s used only when `use_automatic_units` is `false`.
- `style` (Table.CellFormat.DurationFormat.Style): The formatting style, which can be compact (“1h”), short (“1 hr”), or long (“1 hour”).

## See Also

### Objects
- [object Table.CellFormat.BaseFormat](./table.cellformat.baseformat.md)
  Options for formatting a number in a numeral system such as binary, octal, or hexadecimal.
- [object Table.CellFormat.BoolFormat](./table.cellformat.boolformat.md)
  Options for Boolean formatting, including the strings shown in place of true and false.
- [object Table.CellFormat.CurrencyFormat](./table.cellformat.currencyformat.md)
  Options for currency formatting.
- [object Table.CellFormat.DateTimeFormat](./table.cellformat.datetimeformat.md)
  Options for date and time formatting.
- [object Table.CellFormat.FractionFormat](./table.cellformat.fractionformat.md)
  Options for fraction formatting, such as showing a decimal as a fraction.
- [object Table.CellFormat.NumberFormat](./table.cellformat.numberformat.md)
  Options for plain numeric, percentage, and scientific formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.durationformat)*