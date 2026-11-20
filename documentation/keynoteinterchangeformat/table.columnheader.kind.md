# Table.ColumnHeader.Kind

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The structural role of a column.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(object | string("body" | "grand_total" | "group_subtotal")) Table.ColumnHeader.Kind
```



**Allowed Types**: `object`, `string("body" | "grand_total" | "group_subtotal")`

## Overview

The default is `body`; the other cases are reserved for pivot tables, which version 1.0 doesn’t support.

A pivot table’s group-label column, which version 1.0 doesn’t support. Its `GroupLabel` value holds the grouping row identifier and the group value.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.column-header.kind`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `group_label` (Table.ColumnHeader.GroupLabel) *(required)*: A pivot table’s group-label column, which version 1.0 doesn’t support. Its `GroupLabel` value holds the grouping row identifier and the group value.

## See Also

### Enumerations
- [type Table.ColumnHeader.VisibilityState](./table.columnheader.visibilitystate.md)
  A string that indicates whether a column is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.columnheader.kind)*