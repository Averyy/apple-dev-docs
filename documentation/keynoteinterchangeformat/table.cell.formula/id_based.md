# Table.Cell.Formula.id_based

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A formula expression whose cell references are carried separately as row and column IDs.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Cell.Formula.id_based
```

## Overview

This expression means they survive insertions and deletions of rows or columns. A reader in version 1.0 leaves the expression’s placeholder tokens unsubstituted, so a formula written this way arrives with the tokens still in place.

Written as `{"id_based": …}`: the `id_based` form of `Table.Cell.Formula`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell.formula`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `id_based` (Table.Cell.Formula.IdBasedFormula) *(required)*: A formula expression whose cell references are carried separately as row and column IDs. This expression means they survive insertions and deletions of rows or columns. A reader in version 1.0 leaves the expression’s placeholder tokens unsubstituted, so a formula written this way arrives with the tokens still in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.formula/id_based)*