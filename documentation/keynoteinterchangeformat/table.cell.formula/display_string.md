# Table.Cell.Formula.display_string

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Formula text in A1 notation.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Cell.Formula.display_string
```

## Overview

Keynote writes this text in A1 notation, for example, `=SUM(A1:A10)`, `=B$1*$C2`, where coordinates count from the table’s top-left cell, header rows and columns included, and `$` pins a row or column. A reference into another table is prefixed with that table’s name (`Table 2::A1`). Keynote writes function names and the argument and decimal separators, among other things, in the presentation’s language and region, and reads them in the language and region the presentation opens with, usually the device’s; English function names are also accepted. A formula that doesn’t parse is dropped without a warning and the cell keeps the value given for it, while one that names an unknown function is kept and the cell shows an error.

Written as `{"display_string": …}`: the `display_string` form of `Table.Cell.Formula`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell.formula`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `display_string` (string) *(required)*: Formula text in A1 notation. Keynote writes this text in A1 notation, for example, `=SUM(A1:A10)`, `=B$1*$C2`, where coordinates count from the table’s top-left cell, header rows and columns included, and `$` pins a row or column. A reference into another table is prefixed with that table’s name (`Table 2::A1`). Keynote writes function names and the argument and decimal separators, among other things, in the presentation’s language and region, and reads them in the language and region the presentation opens with, usually the device’s; English function names are also accepted. A formula that doesn’t parse is dropped without a warning and the cell keeps the value given for it, while one that names an unknown function is kept and the cell shows an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.formula/display_string)*