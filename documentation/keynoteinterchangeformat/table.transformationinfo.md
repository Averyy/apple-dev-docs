# Table.TransformationInfo

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Information about how the reader derives a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.TransformationInfo
```

## Overview

In version 1.0, it holds the filter and sort rules applied to the table, in `filter_set` and `sort`, and the table’s `content` holds the result. `base_table` and `structure` are reserved for categorized and pivot tables, which version 1.0 doesn’t support.

## Topics

### Enumerations
- [type Table.TransformationInfo.Structure](./table.transformationinfo.structure.md)
  The structural transformation of a table.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.transformation-info`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `base_table` (Table): The source data this table was derived from. It’s reserved for categorized and pivot tables, which version 1.0 doesn’t support. Its rows and columns carry their own identifiers, independent of the ones this table’s `content`, `column_headers`, and `merges` use.
- `structure` (Table.TransformationInfo.Structure): The structural shape of this table, reserved for categorized and pivot tables, which version 1.0 doesn’t support. Without it, the table is a plain grid of rows and columns, which may still have `filter_set` or `sort`.
- `filter_set` (Table.FilterSet): The filter configuration applied to this table, grouped by column. When it’s present, rows whose `Table.Row.visibility_state` is `filtered` didn’t pass the set.
- `sort` (Table.Sort): The sort rules applied to this table, independent of `filter_set`. The rows in `content` are already in sorted order.

## See Also

### Tables
- [object Table](./table.md)
  A table of cells, nested two levels deep.
- [type ColumnMetrics](./columnmetrics.md)
  The arrangement of a text area into columns, and the width of the gutters between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.transformationinfo)*