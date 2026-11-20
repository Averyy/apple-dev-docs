# Table.CellFormat

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The display format of a cell’s value.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellFormat
```

## Overview

`format_type` selects the kind of format, and the matching sub-format property (`number_format`, `currency_format`, and so on) holds the options for that kind. Sub-formats for a different kind are ignored.

## Topics

### Objects
- [object Table.CellFormat.BaseFormat](./table.cellformat.baseformat.md)
  Options for formatting a number in a numeral system such as binary, octal, or hexadecimal.
- [object Table.CellFormat.BoolFormat](./table.cellformat.boolformat.md)
  Options for Boolean formatting, including the strings shown in place of true and false.
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
### Enumerations
- [type Table.CellFormat.FormatType](./table.cellformat.formattype.md)
  The kind of formatting to apply to a cell’s value.
- [type Table.CellFormat.NegativeNumberStyle](./table.cellformat.negativenumberstyle.md)
  A style for displaying negative numbers.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-format`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `format_type` (Table.CellFormat.FormatType): The kind of formatting to apply (such as number, currency, or date). It determines which sub-format property is read. Keynote doesn’t write `automatic`: a cell set to Automatic is written with the format its value is displayed in, such as `number` or `date_time`, and opens set to that format rather than to Automatic, unless that format is `text`.
- `number_format` (Table.CellFormat.NumberFormat): The options for the `number`, `percentage`, and `scientific` format types.
- `currency_format` (Table.CellFormat.CurrencyFormat): The options for the `currency` format type (such as the currency code and accounting style).
- `fraction_format` (Table.CellFormat.FractionFormat): The options for the `fraction` format type (for example, display as halves, as eighths, or with an up-to-three-digit numerator).
- `base_format` (Table.CellFormat.BaseFormat): The options for the `base` format type (numeric base 2 through 36; for example, binary, octal, or hexadecimal).
- `bool_format` (Table.CellFormat.BoolFormat): The options for the `boolean` format type (the strings to display for true and false).
- `duration_format` (Table.CellFormat.DurationFormat): The options for the `duration` format type (its unit range and style).
- `date_time_format` (Table.CellFormat.DateTimeFormat): The options for the `date_time` format type (its format string).
- `custom_format_identifier` (string): The identifier of a shared custom format, declared in `Table.custom_formats`, that applies to this cell. It’s used only when `format_type` is `custom` and is ignored for built-in format types.

## See Also

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
- [object Table.Cell](./table.cell.md)
  A cell in a table.
- [object Table.CellProperties](./table.cellproperties.md)
  The styling of a table cell, other than its strokes.
- [object Table.ColumnHeader](./table.columnheader.md)
  The metadata for a column in a table.
- [object Table.ConditionalStyleSet](./table.conditionalstyleset.md)
  A shared set of conditional highlighting rules that multiple cells can reference.
- [object Table.CustomFormat](./table.customformat.md)
  A user-defined format for a cell.
- [object Table.Date](./table.date.md)
  An absolute point in time.
- [object Table.FilterSet](./table.filterset.md)
  The complete filter configuration for a table.
- [object Table.PivotRules](./table.pivotrules.md)
  A placeholder for a pivot table’s rules, which version 1.0 doesn’t support.
- [object Table.Predicate](./table.predicate.md)
  A condition that’s evaluated against a single cell’s value.
- [object Table.Row](./table.row.md)
  A row in a table.
- [object Table.Sort](./table.sort.md)
  The sort rules that the reader applies to the rows of a table’s content.
- [object Table.VisualProperties](./table.visualproperties.md)
  The default styling of a table, broken down by region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat)*