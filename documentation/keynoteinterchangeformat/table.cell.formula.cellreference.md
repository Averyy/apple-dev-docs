# Table.Cell.Formula.CellReference

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A reference to a single cell or a rectangular range of cells.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Cell.Formula.CellReference
```

## Overview

It’s addressed by row and column ID rather than by index, so it stays stable across structural edits.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell.formula.cell-reference`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `placeholder` (string) *(required)*: The placeholder token in the expression that this reference fills in, of the form `{refN}` (for example, `{ref0}` or `{ref1}`).
- `display_notation` (string): The original A1-style notation, preserved for display only (for example, `A1`, `B2:D5`, or `$A$1`). It isn’t used during evaluation.
- `start_row_identifier` (string) *(required)*: The row ID of a single cell, or of the top-left cell of a range. It must match a `Table.Row.row_identifier` in this table or, for a cross-table reference, in the table identified by `table_identifier`.
- `start_column_identifier` (string) *(required)*: The column ID of a single cell, or of the top-left cell of a range. It must match a `Table.ColumnHeader.column_identifier` in the referenced table.
- `end_row_identifier` (string): The row ID of the bottom-right cell of a range. Omit it for a single-cell reference.
- `end_column_identifier` (string): The column ID of the bottom-right cell of a range. Omit it for a single-cell reference.
- `is_row_absolute` (boolean): Whether the start row reference is absolute. It’s `true` if the original notation pinned the row (for example, `A$1`) and `false` for a relative reference (`A1`).

  **Default**: `false`
- `is_column_absolute` (boolean): Whether the start column reference is absolute. It’s `true` if the original notation pinned the column (for example, `$A1`) and `false` for a relative reference (`A1`).

  **Default**: `false`
- `is_end_row_absolute` (boolean): Whether the end row reference of a range is absolute. It’s only meaningful when `end_row_identifier` is set.

  **Default**: `false`
- `is_end_column_absolute` (boolean): Whether the end column reference of a range is absolute. It’s only meaningful when `end_column_identifier` is set.

  **Default**: `false`
- `table_identifier` (string): The identifier of another table, for a cross-table reference. It matches the `Table.identifier` of that table. Omit it for a reference within the same table. An example in A1 notation is `Table 2::A1`.

## See Also

### Objects
- [object Table.Cell.Formula.IdBasedFormula](./table.cell.formula.idbasedformula.md)
  A formula whose cell references are stored separately, by row and column ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.formula.cellreference)*