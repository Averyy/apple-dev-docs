# Table.CellRange.RowColumnIdRange

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A range addressed by the row and column IDs of its top-left and bottom-right cells.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CellRange.RowColumnIdRange
```

## Overview

Using IDs rather than indexes keeps the range stable across row and column insertions and deletions. Resolve each ID against the `row_identifier`s of the rows in `content` and the `column_identifier`s in `column_headers`; a range can name a row that `content` omits, and such a range can’t be located.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell-range.row-column-id-range`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `top_left_row_identifier` (string) *(required)*: The row ID of the top-left cell of the range.
- `top_left_column_identifier` (string) *(required)*: The column ID of the top-left cell of the range.
- `bottom_right_row_identifier` (string) *(required)*: The row ID of the bottom-right cell of the range.
- `bottom_right_column_identifier` (string) *(required)*: The column ID of the bottom-right cell of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellrange.rowcolumnidrange)*