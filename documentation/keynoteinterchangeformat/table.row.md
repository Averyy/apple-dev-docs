# Table.Row

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A row in a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Row
```

## Overview

It holds the row’s cells, optional row-level defaults (`row_height`, `cell_properties`, and `text_properties`), and the stable `row_identifier` that formula references and merges use.

## Topics

### Objects
- [object Table.Row.GroupLabel](./table.row.grouplabel.md)
  The group that a category header row, or a pivot table’s row-axis group label, stands for.
### Enumerations
- [object Table.Row.Kind](./table.row.kind.md)
  The structural role of a row.
- [type Table.Row.VisibilityState](./table.row.visibilitystate.md)
  Whether a row is visible, and if not, whether it was hidden explicitly or excluded by the active filter.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.row`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `row_index` (integer): The zero-based position of the row in the table, from `0` through `Table.number_of_rows` minus 1. It’s required only in a sparse table, to mark the first non-blank row after a gap; the rows that follow are positioned sequentially.
- `row_identifier` (string): The row’s stable identifier. Formula references (`Table.Cell.Formula.CellReference.start_row_identifier` and `Table.Cell.Formula.CellReference.end_row_identifier`) and merge ranges use it, so references survive row insertions and deletions.
- `row_height` (number): The height of the row, in points, which must be greater than 0. If it’s present, it overrides `Table.default_row_height` for this row only.
- `cell_properties` (Table.CellProperties): The default cell styling for cells in the row. It overrides the table and column defaults, and `Table.Cell.cell_properties` overrides it for an individual cell.
- `text_properties` (ParagraphProperties): The default paragraph and text style for cells in the row. It overrides the table and column defaults, and `Table.Cell.text_properties` overrides it for an individual cell.
- `cells` ([Table.Cell]): The cells in the row, ordered from left to right. The list is sparse: trailing blank cells can be omitted, and a gap in the middle is marked by `Table.Cell.column_index` on the next non-blank cell.
- `visibility_state` (Table.Row.VisibilityState): Whether this row is visible, and if not, whether the user hid it or the active filter excluded it. Rows that aren’t visible remain in `content`.
- `kind` (Table.Row.Kind): The row’s structural role: `body` for an ordinary data row. The other roles (group label, subtotal, and grand total) are reserved for categorized and pivot tables, which version 1.0 doesn’t support.

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
- [object Table.Sort](./table.sort.md)
  The sort rules that the reader applies to the rows of a table’s content.
- [object Table.VisualProperties](./table.visualproperties.md)
  The default styling of a table, broken down by region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.row)*