# Table.Predicate.Reference

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A reference to a single cell, used as a predicate’s comparison operand.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Predicate.Reference
```

## Overview

It addresses the cell by row and column ID, so the reference stays stable across structural edits. Range references aren’t supported here; predicate operands are always single scalar values.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.predicate.reference`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `row_identifier` (string) *(required)*: The row ID of the referenced cell. It must match a `Table.Row.row_identifier` in this table or, for a cross-table reference, in the table identified by `table_identifier`.
- `column_identifier` (string) *(required)*: The column ID of the referenced cell. It must match a `Table.ColumnHeader.column_identifier` in the referenced table.
- `is_row_absolute` (boolean): Whether the row reference is absolute. It’s `true` if the original notation pinned the row (for example, `A$1`), and `false` if the row is relative (`A1`).

  **Default**: `false`
- `is_column_absolute` (boolean): Whether the column reference is absolute. It’s `true` if the original notation pinned the column (for example, `$A1`), and `false` if the column is relative (`A1`).

  **Default**: `false`
- `table_identifier` (string): The identifier of another table, for a cross-table reference. It matches the `Table.identifier` of that table. Omit it for a reference within the same table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.reference)*