# Table.CellProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The styling of a table cell, other than its strokes.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellProperties
```

## Overview

Strokes are kept separately, in `Table.Cell.Strokes`, so individual edges can be overridden.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `text_wrap` (boolean): Whether text that exceeds the column width wraps to more lines (`true`) or clip (`false`).
- `vertical_alignment` (VerticalAlignmentType): The vertical alignment of content in the cell (top, middle, or bottom).
- `padding` (Insets): The inset of the cell’s content from the cell’s edges, in points (top, leading, bottom, and trailing).
- `fill` ((Fill | null)): The cell’s background fill (color, gradient, or image). If it’s absent, the fill is inherited; an explicit `null` gives the cell no fill, which isn’t the same as a fill at 0% opacity.

  **Allowed Types**: `Fill`, `null`

## See Also

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
- [object Table.Cell](./table.cell.md)
  A cell in a table.
- [object Table.CellFormat](./table.cellformat.md)
  The display format of a cell’s value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellproperties)*