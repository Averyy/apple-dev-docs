# Table.Cell.Formula.IdBasedFormula

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A formula whose cell references are stored separately, by row and column ID.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Cell.Formula.IdBasedFormula
```

## Overview

Because they’re stored by ID, the references survive insertions and deletions of rows or columns.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.cell.formula.id-based-formula`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `expression` (string) *(required)*: The formula expression, with placeholder tokens in place of cell references. Placeholders have the form `{refN}`, zero-indexed. For example, in `=SUM({ref0}) + {ref1}`, `{ref0}` resolves to the range carried by `references[0]` and `{ref1}` to `references[1]`.
- `references` ([Table.Cell.Formula.CellReference]): The cell references used by the expression, one entry for each placeholder. Their order must match the `{refN}` indices in `expression`.

## See Also

### Objects
- [object Table.Cell.Formula.CellReference](./table.cell.formula.cellreference.md)
  A reference to a single cell or a rectangular range of cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.formula.idbasedformula)*