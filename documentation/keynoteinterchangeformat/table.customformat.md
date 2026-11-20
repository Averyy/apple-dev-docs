# Table.CustomFormat

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A user-defined format for a cell.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CustomFormat
```

## Overview

A custom format has a format pattern string and optional conditional rules that switch the pattern based on the cell’s value. It’s used when `Table.CellFormat.format_type` is `custom`. Custom formats are stored in `Table.custom_formats`, and individual cells refer to one through `cell_format.custom_format_identifier`, so a single definition can be reused by many cells.

## Topics

### Objects
- [object Table.CustomFormat.CustomFormatCondition](./table.customformat.customformatcondition.md)
  A conditional rule on a custom number format.
- [object Table.CustomFormat.NumberFormatData](./table.customformat.numberformatdata.md)
  Details that the reader precomputes from a custom number format’s format string.
### Enumerations
- [type Table.CustomFormat.CustomFormatType](./table.customformat.customformattype.md)
  The kind of value the custom format applies to.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.custom-format`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string) *(required)*: The unique identifier of the custom format. Cells refer to it through `Table.CellFormat.custom_format_identifier`.
- `format_name` (string): The name of the custom format as shown in Keynote’s Data Format pop-up menu (for example, `My Sales Format`). It’s optional and purely cosmetic.
- `format_string` (string) *(required)*: The format pattern, whose syntax depends on `format_type`. Number formats use placeholder tokens such as `#,###.00` or `#,###K`, date and time formats use Unicode date patterns such as `MMM d, yyyy`, and text formats use `@` as the value placeholder.
- `format_type` (Table.CustomFormat.CustomFormatType): The kind of value the format applies to. It determines how `format_string` is interpreted and which other properties are used.
- `number_format_data` (Table.CustomFormat.NumberFormatData): The parsed details of `format_string`, such as placeholder counts and the scale factor, used to render numeric custom formats. It’s used only when `format_type` is `number`.
- `conditions` ([Table.CustomFormat.CustomFormatCondition]): The conditional rules that swap in a different format string when the cell value meets a threshold condition, for example, to format negative values differently from positive ones. They’re used only when `format_type` is `number`.

## See Also

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
- [object Table.Cell](./table.cell.md)
  A cell in a table.
- [object Table.CellFormat](./table.cellformat.md)
  The display format of a cell’s value.
- [object Table.CellProperties](./table.cellproperties.md)
  The styling of a table cell, other than its strokes.
- [object Table.ColumnHeader](./table.columnheader.md)
  The metadata for a column in a table.
- [object Table.ConditionalStyleSet](./table.conditionalstyleset.md)
  A shared set of conditional highlighting rules that multiple cells can reference.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.customformat)*