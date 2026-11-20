# Table.ConditionalStyleSet

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A shared set of conditional highlighting rules that multiple cells can reference.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.ConditionalStyleSet
```

## Topics

### Objects
- [object Table.ConditionalStyleSet.Rule](./table.conditionalstyleset.rule.md)
  A single conditional highlighting rule with a predicate and styling to apply when the predicate is true.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.conditional-style-set`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string) *(required)*: The unique identifier of the conditional style set.
- `rules` ([Table.ConditionalStyleSet.Rule]) *(required)*: The ordered list of conditional highlighting rules, with a maximum of 15. The first rule whose predicate is true for the cell is applied, and the rules after it aren’t.

## See Also

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
- [object Table.Cell](./table.cell.md)
  A cell in a table.
- [object Table.CellFormat](./table.cellformat.md)
  The display format of a cell’s value.
- [object Table.CellProperties](./table.cellproperties.md)
  The styling of a table cell, other than its strokes.
- [object Table.ColumnHeader](./table.columnheader.md)
  The metadata for a column in a table.
- [object Table.CustomFormat](./table.customformat.md)
  A user-defined format for a cell.
- [object Table.Date](./table.date.md)
  An absolute point in time.
- [object Table.FilterSet](./table.filterset.md)
  The complete filter configuration for a table.
- [object Table.PivotRules](./table.pivotrules.md)
  A placeholder for a pivot table’s rules, which version 1.0 doesn’t support.
- [object Table.Predicate](./table.predicate.md)
  A condition that’s evaluated against a single cell’s value.
- [object Table.Row](./table.row.md)
  A row in a table.
- [object Table.Sort](./table.sort.md)
  The sort rules that the reader applies to the rows of a table’s content.
- [object Table.VisualProperties](./table.visualproperties.md)
  The default styling of a table, broken down by region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.conditionalstyleset)*