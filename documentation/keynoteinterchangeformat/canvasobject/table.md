# CanvasObject.table

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A table of cells, nested two levels deep.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.table
```

## Overview

`content` holds the table’s rows, ordered top to bottom, and each row’s `cells` holds that row’s cells, ordered left to right. The first `number_of_header_rows` rows are header rows, and the last `number_of_footer_rows` are footer rows. Rows and cells that carry nothing may be omitted, so `Table.Row.row_index` and `Table.Cell.column_index` mark where a run resumes after a gap. On a slide, a table whose `title` is absent, has no text, or reads `Unnamed` or `Unnamed Table` gets a default name such as Table `1` as its built-in title, and Keynote renames tables there that share a name the same way until each has its own; which of them keeps the name isn’t defined, and Keynote reports no warning.

Written as `{"table": …}`: the `table` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `table` (Table) *(required)*: A table of cells, nested two levels deep. `content` holds the table’s rows, ordered top to bottom, and each row’s `cells` holds that row’s cells, ordered left to right. The first `number_of_header_rows` rows are header rows, and the last `number_of_footer_rows` are footer rows. Rows and cells that carry nothing may be omitted, so `Table.Row.row_index` and `Table.Cell.column_index` mark where a run resumes after a gap. On a slide, a table whose `title` is absent, has no text, or reads `Unnamed` or `Unnamed Table` gets a default name such as Table `1` as its built-in title, and Keynote renames tables there that share a name the same way until each has its own; which of them keeps the name isn’t defined, and Keynote reports no warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/table)*