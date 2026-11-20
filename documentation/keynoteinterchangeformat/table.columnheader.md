# Table.ColumnHeader

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The metadata for a column in a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.ColumnHeader
```

## Overview

Its default formatting and styling apply to the body cells in the column.

## Topics

### Objects
- [object Table.ColumnHeader.GroupLabel](./table.columnheader.grouplabel.md)
  The group that a pivot table’s group-label column stands for.
### Enumerations
- [object Table.ColumnHeader.Kind](./table.columnheader.kind.md)
  The structural role of a column.
- [type Table.ColumnHeader.VisibilityState](./table.columnheader.visibilitystate.md)
  A string that indicates whether a column is visible.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.column-header`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `column_identifier` (string): The column’s stable identifier. Formula references (`Table.Cell.Formula.CellReference.start_column_identifier` and `Table.Cell.Formula.CellReference.end_column_identifier`) and merge ranges use it, so inserting or removing columns doesn’t invalidate references.
- `title` (string): The column’s display title. By default, it mirrors the value of the column’s first header cell; for a column with no header or a blank header, a generic name (for example, `Column C`) may be used.
- `cell_format` (Table.CellFormat): The default data format (such as number, currency, or date) for body cells in the column. Header and footer rows aren’t affected. `Table.Cell.cell_format` overrides it for an individual cell.
- `column_width` (number): The width of the column, in points, which must be greater than 0. If it’s present, it overrides `Table.default_column_width` for this column only.
- `cell_properties` (Table.CellProperties): The default cell styling (fill, alignment, padding, and wrap) for body cells in the column. `Table.Cell.cell_properties` overrides it for an individual cell.
- `text_properties` (ParagraphProperties): The default paragraph and text style for body cells in the column. `Table.Cell.text_properties` overrides it for an individual cell.
- `visibility_state` (Table.ColumnHeader.VisibilityState): Whether this column is visible. Hidden columns are still counted by `number_of_columns`.
- `kind` (Table.ColumnHeader.Kind): The column’s structural role: `body` for an ordinary data column. The other roles (group label, subtotal, and grand total) are reserved for pivot tables, which version 1.0 doesn’t support.

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.columnheader)*