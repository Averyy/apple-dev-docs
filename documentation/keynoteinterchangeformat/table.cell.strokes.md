# Table.Cell.Strokes

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The stroke overrides for the edges of a cell.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Cell.Strokes
```

## Overview

An omitted edge falls back to the table-level stroke for the cell’s region (body, header, or footer).

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell.strokes`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `top` (Stroke): The stroke along the top edge of the cell.
- `bottom` (Stroke): The stroke along the bottom edge of the cell.
- `left` (Stroke): The stroke along the left edge of the cell.
- `right` (Stroke): The stroke along the right edge of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.strokes)*