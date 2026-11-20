# Table.CellRange

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A rectangular range of cells in a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellRange
```

## Overview

It’s addressed by row and column IDs, so it stays stable across structural edits. It’s defined so that future versions can add other ways to address a range. Fields that use it include `Table.merges` (visually combined cells) and `Table.Cell.spill_range` (the range a spilling formula populates).

A range addressed by the row ID and column ID of its top-left and bottom-right cells.

## Topics

### Objects
- [object Table.CellRange.RowColumnIdRange](./table.cellrange.rowcolumnidrange.md)
  A range addressed by the row and column IDs of its top-left and bottom-right cells.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-range`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `row_column_id_range` (Table.CellRange.RowColumnIdRange) *(required)*: A range addressed by the row ID and column ID of its top-left and bottom-right cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellrange)*