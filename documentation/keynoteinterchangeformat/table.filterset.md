# Table.FilterSet

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The complete filter configuration for a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.FilterSet
```

## Overview

It holds the per-column filters and how they combine. Rows that don’t pass the set stay in `content`, with `Table.Row.visibility_state` set to `filtered`.

## Topics

### Objects
- [object Table.FilterSet.Filter](./table.filterset.filter.md)
  The filter for a single column.
### Enumerations
- [type Table.FilterSet.CombineMode](./table.filterset.combinemode.md)
  The rule for combining the per-column filters in a filter set to decide whether a row passes.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.filter-set`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `is_enabled` (boolean): Whether the filter set is enabled. When it’s `false`, the filter set is preserved but every row passes, and no row has `Table.Row.visibility_state` set to `filtered`.

  **Default**: `true`
- `combine_mode` (Table.FilterSet.CombineMode): The way the per-column `filters` combine to decide whether a row passes the set. With `and`, the row must pass every column’s filter; with `or`, the row passes if it passes any one column’s filter. Within a single column’s filter, the rules are always combined with OR: a row passes that column’s filter when any of its rules match.
- `filters` ([Table.FilterSet.Filter]) *(required)*: The column filters, with at most one entry for each column. Each entry carries the rules that apply to its column. The order isn’t significant.

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
- [object Table.ConditionalStyleSet](./table.conditionalstyleset.md)
  A shared set of conditional highlighting rules that multiple cells can reference.
- [object Table.CustomFormat](./table.customformat.md)
  A user-defined format for a cell.
- [object Table.Date](./table.date.md)
  An absolute point in time.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.filterset)*