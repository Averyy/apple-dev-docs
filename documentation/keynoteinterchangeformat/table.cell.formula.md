# Table.Cell.Formula

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The form in which a cell’s formula is carried.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Table.Cell.Formula.display_string | Table.Cell.Formula.id_based) Table.Cell.Formula
```



**Allowed Types**: `Table.Cell.Formula.display_string`, `Table.Cell.Formula.id_based`

## Discussion

The `display_string` form is the one to write: it’s the only one a reader resolves in version 1.0. An `id_based` formula is accepted, but its references aren’t substituted into the expression, so it reaches the reader with its placeholder tokens intact.

This value takes one of the following forms:

- `display_string`: Formula text in A1 notation. Keynote writes this text in A1 notation, for example, `=SUM(A1:A10)`, `=B$1*$C2`, where coordinates count from the table’s top-left cell, header rows and columns included, and `$` pins a row or column. A reference into another table is prefixed with that table’s name (`Table 2::A1`). Keynote writes function names and the argument and decimal separators, among other things, in the presentation’s language and region, and reads them in the language and region the presentation opens with, usually the device’s; English function names are also accepted. A formula that doesn’t parse is dropped without a warning and the cell keeps the value given for it, while one that names an unknown function is kept and the cell shows an error.
- `id_based`: A formula expression whose cell references are carried separately as row and column IDs. This expression means they survive insertions and deletions of rows or columns. A reader in version 1.0 leaves the expression’s placeholder tokens unsubstituted, so a formula written this way arrives with the tokens still in place.

## Topics

### Objects
- [object Table.Cell.Formula.CellReference](./table.cell.formula.cellreference.md)
  A reference to a single cell or a rectangular range of cells.
- [object Table.Cell.Formula.IdBasedFormula](./table.cell.formula.idbasedformula.md)
  A formula whose cell references are stored separately, by row and column ID.
### Dictionaries
- [object Table.Cell.Formula.display_string](./table.cell.formula/display_string.md)
  Formula text in A1 notation.
- [object Table.Cell.Formula.id_based](./table.cell.formula/id_based.md)
  A formula expression whose cell references are carried separately as row and column IDs.

## See Also

### Enumerations
- [type Table.Cell.UnformattedValue](./table.cell.unformattedvalue.md)
  The unformatted value of a cell, which can be one of several data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.formula)*