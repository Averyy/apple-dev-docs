# Table.Cell

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A cell in a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Cell
```

## Overview

Its value is carried as a formatted display string in `value`, a typed underlying value in `unformatted_value`, or both. It can also have a formula and per-cell style and format overrides.

## Topics

### Objects
- [object Table.Cell.Strokes](./table.cell.strokes.md)
  The stroke overrides for the edges of a cell.
### Enumerations
- [type Table.Cell.Formula](./table.cell.formula.md)
  The form in which a cell’s formula is carried.
- [type Table.Cell.UnformattedValue](./table.cell.unformattedvalue.md)
  The unformatted value of a cell, which can be one of several data types.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `value` (string): The cell’s content as a pre-formatted string (for example, `$1,234.56`, `12/25/2024`, or `42%`). It’s the simplest representation, intended for readers that render the cell as plain text. For the typed value, use `unformatted_value`.
- `unformatted_value` (Table.Cell.UnformattedValue): The cell’s typed underlying value (`number`, `text`, `date`, `boolean`, or `rich_text`), which lets a reader recover the value’s type when `value` is only the formatted string. It’s absent when the value has no typed form: a formula that evaluated to an error arrives with `formula` set and an empty `value`, so an absent typed value doesn’t mean the cell is empty.
- `cell_format` (Table.CellFormat): The cell’s value-formatting override. If it’s set, it overrides the column-level default in `Table.ColumnHeader.cell_format` for this cell only.
- `cell_properties` (Table.CellProperties): The cell’s styling override (fill, alignment, padding, and wrap). If it’s set, it overrides the table-, column-, and row-level defaults for this cell only.
- `text_properties` (ParagraphProperties): The cell’s paragraph and text style override (font, size, color, and alignment). If it’s set, it overrides the table-, column-, and row-level defaults for this cell only.
- `strokes` (Table.Cell.Strokes): The cell’s stroke overrides for each edge (top, bottom, left, and right). An omitted edge falls back to the table-level stroke for the cell’s region.
- `anchored_objects` ([string]): The IDs of the objects, such as shapes and images, that are anchored to the cell. Keynote ignores them.
- `column_index` (integer): The zero-based column position of the cell in its row, from `0` through `Table.number_of_columns` minus 1. It’s only required in a sparse row, to mark the first non-blank cell after a gap; the cells that follow are positioned sequentially.
- `formula` (Table.Cell.Formula): The formula that produces the cell’s value. If it’s present, `value` and `unformatted_value` contain the most recently computed result of evaluating the formula.
- `spill_range` (Table.CellRange.RowColumnIdRange): The range that the cell’s `formula` populates when it spills, with this cell at its top left. It’s only meaningful for a cell whose formula spills, and it’s absent when the spill is blocked. The other cells in the range hold the last spilled result and are replaced on re-evaluation. A corner ID matching no row or column of this table is ignored without a warning, and the cells it would have covered keep the values written for them.
- `conditional_style_set_identifier` (string): The ID of a shared conditional style set, declared in `Table.conditional_style_sets`, that applies to the cell. The first rule in the set whose condition is true for this cell determines its conditional styling. An identifier matching no set is ignored without a warning, and the cell keeps its regular styling.

## See Also

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
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
- [object Table.Row](./table.row.md)
  A row in a table.
- [object Table.Sort](./table.sort.md)
  The sort rules that the reader applies to the rows of a table’s content.
- [object Table.VisualProperties](./table.visualproperties.md)
  The default styling of a table, broken down by region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell)*